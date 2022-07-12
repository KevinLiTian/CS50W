""" View Functions """

import random

from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util, forms


def index(request):
    """ Home Page """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    """ Any Wiki Page """
    content = util.get_entry(title).strip()

    if request.method == "GET":
        # Page Not Found
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "title": "404",
                "content": "Page Not Found"
            })

        # Render the corresponding page
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": markdown(content)
        })

    # If is POST, take to edit page
    form = forms.EditPageForm(initial={"title": title, "content":content})
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": form
    })

def search(request):
    """ Search for a Wiki Page """
    if request.method == "POST":
        query = request.POST.get('q').lower()
        entries = [entry.lower() for entry in util.list_entries()]

        # If query is in entries, redirect to that page
        if query in entries:
            return redirect('page', title=query)

        # Check if query is substring of any entries
        # Reformat the entries
        candidates = [entry for entry in entries if query in entry]
        for idx, entry in enumerate(candidates):
            if entry in ("html", "css"):
                candidates[idx] = entry.upper()
            else:
                candidates[idx] = entry.capitalize()

        # Show all candidates
        return render(request, "encyclopedia/search.html", {
            "candidates": candidates
        })

    return index(request)

def new(request):
    """ Create a New Wiki Page """
    # If using GET method, just render the page
    if request.method == "GET":
        form = forms.NewPageForm()
        return render(request, "encyclopedia/new.html", {
            "form": form
        })

    # Otherwise is during form submission (POST)
    form = forms.NewPageForm(request.POST)

    # Server-side validation
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]

        # Check for existance
        # Render error page if exists
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "title": "Page Exist",
                "content": "There is already a Wiki page with this title"
                })

        # Save New if new
        util.save_entry(title, content)
        return redirect('page', title=title)

    return redirect('page', title=title)

def edit(request):
    """ Edit Wiki Page Done (POST) """
    form = forms.EditPageForm(request.POST)

    # Server-side validation
    if form.is_valid():
        title = form.cleaned_data["title"].strip()
        content = form.cleaned_data["content"].strip()

        util.save_entry(title, content)
        util.remove_newline(title)
        return redirect('page', title=title)

    return redirect('page', title=title)

def rand():
    """ Randomly Redirect to a Wiki Page """
    return redirect('page', title=random.choice(util.list_entries()))

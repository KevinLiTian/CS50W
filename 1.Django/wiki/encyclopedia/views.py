from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util


def index(request):
    """ Home Page """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    """ Any Wiki Page """
    content = util.get_entry(title)

    # Page Not Found
    if content is None:
        return render(request, "encyclopedia/404.html")

    # Render the corresponding page
    return render(request, "encyclopedia/page.html", {
        "title": title,
        "content": markdown(content)
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

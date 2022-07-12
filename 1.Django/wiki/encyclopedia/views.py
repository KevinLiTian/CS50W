from django.shortcuts import render
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

    if content is None:
        return render(request, "encyclopedia/404.html")

    return render(request, "encyclopedia/page.html", {
        "title": title,
        "content": markdown(content)
    })

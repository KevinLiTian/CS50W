""" Utility Functions """

import re
import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        file = default_storage.open(f"entries/{title}.md")
        return file.read().decode("utf-8")
    except FileNotFoundError:
        return None

def remove_newline(title):
    """
    Found a problem when editing the Wiki pages
    Newlines get piled up whenver edits are saved
    This function removes extra newlines in a md file
    """
    # Read from current file and write to another temp file
    filename = os.path.join("entries", f"{title}.md")
    temp = os.path.join("entries", "temp.txt")

    with open(filename, encoding="utf-8") as file:
        with open(temp, 'w', encoding='utf-8') as output:
            for line in file:
                # If line does not start with newline, write to new file
                if not line.startswith('\n'):
                    output.write(line)

    # Replace original file with the new file content
    os.replace(temp, filename)

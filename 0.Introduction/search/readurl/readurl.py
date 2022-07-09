""" Python script that reads URL from a txt file and split the URL into pieces """

import sys


def main():
    """ Main function
    Read from a command line argument txt file
    Crawl the URL and split it into pieces
    """
    if len(sys.argv) != 2:
        sys.exit("Usage: python readurl.py url.txt")

    print("Processing URL ...")
    loadurl(sys.argv[1])


def loadurl(filename):
    """ Helper function to read txt file and write to a new file """
    # Read a url from txt file
    with open(filename, encoding='utf-8') as file:
        url = file.read()

    # Split into params and write to separate lines
    with open("result.txt", "w", encoding='utf-8') as file:
        for param in url.split("&"):
            file.write(param+'\n')

if __name__ == "__main__":
    main()

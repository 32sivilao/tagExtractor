import requests
import subprocess
from bs4 import BeautifulSoup
import pyperclip
import parser


def extractTags(url):
    if(url[:21] == "https://gelbooru.com/"):
        # Send a GET request to the URL to get the HTML content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract all the links from the HTML file
            links = [link.get("href") for link in soup.find_all("a")]

            # Remove "/wiki_pages/" from the links and store the remaining part in the `tags` list
            tags = [link.replace("index.php?page=wiki&s=list&search=", "").replace("_", " ") for link in links if
                    link.startswith("index.php?page=wiki&s=list&search=")]

            # remove artist
            tags = tags[1:-1]

        else:
            # If the request was not successful, print an error message
            print("Failed to retrieve the HTML content.")

    else:
        # Send a GET request to the URL to get the HTML content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract all the links from the HTML file
            links = [link.get("href") for link in soup.find_all("a")]

            # Remove "/wiki_pages/" from the links and store the remaining part in the `tags` list
            tags = [link.replace("/wiki_pages/", "")[:-4].replace("_", " ") for link in links if link.startswith("/wiki_pages/") and not link.startswith("/wiki_pages/help:") and not link.startswith("/wiki_pages/about:")]

        else:
            # If the request was not successful, print an error message
            print("Failed to retrieve the HTML content.")

    return tags


#run the command
url = pyperclip.paste()
tags = extractTags(url)

parsedtags = parser.parse(tags)

# Join the remaining elements in the `tags` list with commas
output = ", ".join(parsedtags)
print(output)

# Copy the output to the system's clipboard
process = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
process.communicate(output.encode('utf-8'))


import argparse
import requests
from bs4 import BeautifulSoup
import html2text

def search_wikipedia(search_type, search_term):
    parser = argparse.ArgumentParser(description='Search Wikipedia')
    parser.add_argument(search_type, help='Wikipedia page URL or search term')
    args = parser.parse_args([search_term])

    url = args.url or 'https://en.wikipedia.org/wiki/' + args.search

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')

    title = soup.find('h1', id='firstHeading').text

    # Check if the first paragraph exists
    first_paragraph_elem = soup.find('div', class_='mw-parser-output').id
    if first_paragraph_elem:
        first_paragraph = first_paragraph_elem.text
    else:
        first_paragraph = 'No text found.'

    # Use html2text to remove the HTML syntax from the plain text
    text = html2text.html2text(response.text)

    print(title)
    print(first_paragraph)
    print(text)

while True:
    print("Select an option:")
    print("1. Search Wikipedia by URL")
    print("2. Search Wikipedia by term")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        url = input("Enter the Wikipedia page URL: ")
        search_wikipedia("--url", url)
    elif choice == "2":
        term = input("Enter the search term: ")
        search_wikipedia("--search", term)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
import argparse
import requests
from bs4 import BeautifulSoup
import html2text

parser = argparse.ArgumentParser(description='Search Wikipedia')
parser.add_argument('--url', help='Wikipedia page URL')
parser.add_argument('--search', help='Search term')
args = parser.parse_args()

if args.url:
    url = args.url
elif args.search:
    url = 'https://en.wikipedia.org/wiki/' + args.search
else:
    print('Please specify a Wikipedia page URL or a search term')
    exit()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')

title = soup.find('h1', id='firstHeading').text

# Check if the first paragraph exists
first_paragraph_elem = soup.find('div', class_='mw-parser-output')
if first_paragraph_elem:
    first_paragraph = first_paragraph_elem.find('p').text
else:
    first_paragraph = 'No text found.'

# Use html2text to remove the HTML syntax from the plain text
text = html2text.html2text(response.text)

print(title)
print(first_paragraph.encode('utf-8'))
# print(text)
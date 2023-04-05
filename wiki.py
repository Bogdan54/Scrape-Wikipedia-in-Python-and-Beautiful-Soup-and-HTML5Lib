import argparse
import requests
from bs4 import BeautifulSoup
import html5lib

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
first_paragraph = soup.find('div', class_='mw-parser-output').p.text

print(title)
print(first_paragraph)
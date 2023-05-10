# Uni-Project
Uni-Project is a Python project that allows users to search for Wikipedia pages and retrieve the title and first paragraph of a page.

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Features](#Features)
- [Authors](#Authors)
- [Acknowledgments](#Acknowledgments)
- [Example](#Example)

## Installation
To install Uni-Project, you can clone the GitHub repository:
> git clone https://github.com/Bogdan54/Uni-Project.git

Then, navigate to the Uni-Project directory:
> cd Uni-Project
Uni-Project requires the following dependencies:

* argparse
* requests
* BeautifulSoup
* html2text
You can install them using pip:

> pip install argparse requests beautifulsoup4 html2text

## Usage
To use the graphical user interface, run the gui.py script:

> python gui.py
The GUI will open and allow you to search and parse Wikipedia pages.

You can also use the --url or --search command-line arguments to specify the page to search:

> python gui.py --url https://en.wikipedia.org/wiki/Python_(programming_language)

or

> python gui.py --search Python programming language
The output will be displayed in the GUI.

## Features
Uni-Project provides the following features:

* Ability to search for Wikipedia pages by title or URL
* Retrieval of the title and first paragraph of a Wikipedia page
* HTML syntax removal using html2text
* Contributing
* Contributions to Uni-Project are welcome! You can contribute by:

## Authors
Uni-Project was created by Bogdan & Bogdan.

## Acknowledgments
Thanks to the developers of argparse, requests, BeautifulSoup, and html2text for their contributions to this project.

## Example
Here is an example of how to use Uni-Project to search for the Wikipedia page for Python (programming language):

> python gui.py --search "Python (programming language)"

The output will be:

> Python (programming language) - Wikipedia
>
> Python is an interpreted, high-level, general-purpose programming language. Created by Guido va

## Reporting issues or bugs

Submitting feature requests
Forking the repository and submitting pull requests with your changes
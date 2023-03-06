# web scraping 
# fetch data from a website

import requests, os, time
from bs4 import BeautifulSoup

while True:
    os.system('cls')
    query = str(input('paste your query: \n'))
    url = f'#website link{query}'
    print(f'searching for {query}...')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.title)
    # Find the first <p> element in the page content
    first_paragraph = soup.find("div", class_="def ddef_d db")

    # Check if a paragraph was found
    if first_paragraph is not None:
        # Print the text content of the <p> element
        print(first_paragraph.get_text())
    else:
        print("No content found.")
    time.sleep(1)
    a = input('\n\nPress any button to search another, or press q to quit: ')
    if a.lower() == 'q':
        break
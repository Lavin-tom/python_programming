# web scraping
# fetch data from a website

import requests, os, time
from bs4 import BeautifulSoup
# clear the screen 
os.system('cls')  
query = str(input('Paste url to get update: \n'))
count = 0
while(True):
    os.system('cls')        # clear the screeen
    url = f'{query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #to get teams details
    for team in soup.find_all(class_ = 'cb-list-item ui-header ui-branding-header'):
        print(team.get_text())

    #to get score
    for score in soup.find_all(class_="miniscore-teams ui-bat-team-scores"):
        print(score.get_text())

    # to get current run rate
    for crr in soup.find_all(class_="crr"):
        print(crr.get_text())
    print('\n')

    # display the current players on crease
    table = soup.find(class_ = 'table-responsive')
    rows = table.find_all('tr')

    # Loop through each row and print its data
    for row in rows:
        # Find all <td> tags within the row
        cells = row.find_all('td')
        # Loop through each cell and print its text
        for cell in cells:
            print(cell.text, end=' ')
        print('\n')

    # for commentry
    for commentry in soup.find_all("p",class_="commtext"):
        print(commentry.get_text())
        count += 1
        if count == 10:
            count = 0
            break
    time.sleep(10)      #for 10 second delay
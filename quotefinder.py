from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def famousquotes(quote):
    #quote = input('Type in the quote: ')
    query = quote
    query = query.replace(' ', '+')
    URL = "https://google.com/search?q=" + query

    User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/72.0"
    headers = {"user-agent" : User_agent}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                "title": title,
                "link": link
                }
                #results.append(item)
                print(item)
        #print(item)
        return
famousquotes("batman")
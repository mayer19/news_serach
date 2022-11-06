from bs4 import BeautifulSoup
import requests

reuters_url = "https://www.reuters.com/world/"
cnbc_url = "https://www.cnbc.com/world/?region=world"

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def reuters_parser(soup):
    results = soup.find_all("a", {'data-testid': 'Heading'})
    print(f'{len(results)} articles found.')
    news_dic = {'title': [], 'link': []}
    for idx, news in enumerate(results):
        news_dic['title'].append(str(news.find("span")).replace("<span>", "").replace("</span>", ""))
        news_dic['link'].append("https://www.reuters.com"+ news["href"])
        print(news_dic['title'][idx])
        print(news_dic['link'][idx])


def cnbc_parser(soup):
    results = soup.find_all("a", {'class': 'LatestNews-headline'})
    print(len(results))
    for news in results:
        print(news.text)
        print(news["href"])

url = 99

while url != 0:
    print(""" Menu
    1- Reuters
    2- CNBC
    """)
    url = int(input("What website do want to see the news? "))
    if url == 1:
        soup = get_data(reuters_url)
        reuters_parser(soup)
    elif url == 2:
        soup = get_data(cnbc_url)
        cnbc_parser(soup)
    elif url == 0:
        break
    else:
        print("Choose a valid option please.")

#{}
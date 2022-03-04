from bs4 import BeautifulSoup
import requests
import csv


test_url = '/'

url_list = ['/2021-03-06/','2020-03-06/', '2019-03-06/', '2018-03-06/', '2017-03-06/', '2016-03-06/', '2015-03-06/', '2014-03-06/', '2013-03-06/']

filename = 'fullscrape.txt'
myfile = open(filename, 'w')
list = [ ]

def scrape_chart(chart_url):
    url = 'https://www.billboard.com/charts/hot-100' + chart_url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    container = soup.find_all("ul", class_="o-chart-results-list-row")
    for item in container:
        rank = item.find("span", class_="a-font-primary-bold-l").text
        song = item.find("h3", class_="c-title").text
        artist = item.find("span", class_="u-max-width-230@tablet-only").text
        list.append(rank)
        list.append(song)
        list.append(artist)
        print(list)

#def write_to_csv(url_list):
    #chart_writer = csv.writer(myfile)
    #chart_writer.writerow(["rank", "song", "artist"])
    #for url in url_list:
        #results = scrape_chart(url)
        #chart_writer.writerow(results)

#write_to_csv(url_list)
scrape_chart(test_url)
myfile.close()

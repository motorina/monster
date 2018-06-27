import requests
from bs4 import BeautifulSoup
import csv
import string



def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='col-xs-12').find('ul', class_='alphabetical-list').find_all('a')
    #total_pages = pages.split('=')[1].split('&')[0] #разделяет

    return str(pages)


def write_csv(data):
    with open('monster.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title']) )



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('ul', class_='card-columns').find_all('li')

    for ad in ads:
        try:
            title = ad.find('h3').text #отсекает переносы строк
        except:
            title = ''

        

        data = {'title': title} 

        write_csv(data)
                      
 
def main():
    url = 'https://www.monster.com/jobs/job-title/A'
    base_url = 'https://www.monster.com/jobs/job-title/'
    page_part = ''
    

    total_pages = get_total_pages(get_html(url))
    
    for i in string.ascii_uppercase:   #нумерация страниц по буквам алфавита
        url_gen = base_url + page_part + i
        #print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)



if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

html_request = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'framebar'})

soup = BeautifulSoup(html_request.text, 'html.parser')

popular_area = soup.find(attrs={'class':'grid-row list-content'})

title = popular_area.findAllNext(attrs={'class','media__title'})
images = popular_area.findAllNext(attrs={'class','media__image'})

for image in images:
    print(image.find('a').find('img'))

# print(title)
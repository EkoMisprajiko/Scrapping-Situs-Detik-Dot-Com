import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/popular')
def detik_popular():
    html_request = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'})

    soup = BeautifulSoup(html_request.text, 'html.parser')

    popular_area = soup.find(attrs={'class': 'grid-row list-content'})

    title = popular_area.findAllNext(attrs={'class', 'media__title'})
    images = popular_area.findAllNext(attrs={'class', 'media__image'})

    return render_template('index.html', images=images)



if __name__ == '__main__':
    app.run(debug=True)
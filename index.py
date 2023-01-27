from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        search_term = request.form['user_input']
        source = requests.get('https://rule34.xxx/?page=post&s=list&tags='+search_term).text
        soup = BeautifulSoup(source, 'html.parser')
        images = soup.find_all('img', {'class': 'preview'})
        return render_template('index.html', images=images)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
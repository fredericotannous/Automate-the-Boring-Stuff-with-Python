from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top/')

    #brings error if the website does not exist
    source.raise_for_status() 

    #take the html from the content, than parse it
    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    print(len(movies))

    for movie in movies:
        print(movie)




except Exception as e:
    print(e)
from bs4 import BeautifulSoup
import requests, openpyxl

#create an excel file
excel = openpyxl.Workbook()
sheet = excel.active

#changing sheet title
sheet.title = 'Top Rated Movies'

#add the columns headers
sheet.append(['Rank', 'Movie Name', 'Release Date', 'IMDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/top/')

    #brings error if the website does not exist
    source.raise_for_status() 

    #take the html from the content, than parse it
    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    #print(len(movies))

    #.a access the tag <a, while .text gets the text on the referenced tag
    for movie in movies:
        
        name = movie.find('td', class_='titleColumn').a.text     

        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]   

        year = movie.find('td', class_='titleColumn').span.text.strip('()')

        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])


except Exception as e:
    print(e)

excel.save('Top Rated Movies by IMDB')  
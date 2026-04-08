import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
top_100_movies_webpage = response.text
soup = BeautifulSoup(top_100_movies_webpage, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
movies_list = [movie.text for movie in reversed(movie_titles)]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
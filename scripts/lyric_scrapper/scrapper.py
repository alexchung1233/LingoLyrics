import bs4
import urllib.request as request
import re
import os

BeautifulSoup = bs4.BeautifulSoup


def get_genius_urls(filename: str) -> list[str]:

    song_urls_path =  f"{os.path.dirname(os.path.realpath(__file__))}/{filename}"
    urls = []
    with open(song_urls_path, "r") as file:
        urls = file.readlines()
    return urls



def scrape_genius_song_lyrics(url: str) -> list[str]:

    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = request.urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    verses = soup.find_all('div', attrs={'class', re.compile(r'Lyrics__Container*')})
    lyrics = []
    for verse in verses:
        lyrics.extend(verse.stripped_strings)
    return lyrics


def main():
    urls = get_genius_urls(filename="genius-song-urls.txt")

    for url in urls:
        lyrics = scrape_genius_song_lyrics(url=url)
        print(lyrics)


if __name__  == "__main__":
    main()

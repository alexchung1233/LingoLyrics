import bs4
import urllib.request as request
import re

BeautifulSoup = bs4.BeautifulSoup

url = 'https://genius.com/Heize-and-july-lyrics'

req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})


html_page = request.urlopen(req).read()

soup = BeautifulSoup(html_page, 'html.parser')

verses = soup.find_all('div', attrs={'class', re.compile(r'Lyrics__Container*')})
lyrics = []
for verse in verses:
    lyrics.extend(verse.stripped_strings)

# lyrics = [verse for verse in verses.contents if verse != "<br/>"]
for lyric in lyrics:
    print(f'{lyric}')
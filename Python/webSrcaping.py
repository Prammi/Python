import requests
import bs4

_domain="https://example.com/"
results=requests.get(_domain)

# print(type(results))
# print(results.text)

# soup=bs4.BeautifulSoup(results.text,"lxml")
# print(soup)
# print(soup.select('title'))
# print(soup.select('title')[0].getText())
# print(soup.select('p')[0].getText())
# print(soup.select('h1'))


results=requests.get("https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam")
wiki_soup=bs4.BeautifulSoup(results.text,"lxml")
#print(wiki_soup.select('#footer'))
#print(wiki_soup.select('#footer')[0])
print(wiki_soup.select('.toctext'))







from BeautifulSoup import BeautifulSoup
import requests
from urllib2 import urlopen
url='http://www.theguardian.com/profile/editorial?page=55'

url_of_all_article=[]
def all_pages(url):
	html_source_code=urlopen(url).read()
	soup=BeautifulSoup(html_source_code)
	mydivs = soup.findAll("div", { "class" : "fc-item__content" })
	for item in mydivs:
		temp1=item.findAll('a')[0]['href']
		url_of_all_article.append(temp1)


	next_page=soup.findAll('link',{'rel':"next"})
	if next_page:
		next_page_url=next_page[0]['href']
		return all_pages(next_page_url)
all_pages(url)
print url_of_all_article[0]



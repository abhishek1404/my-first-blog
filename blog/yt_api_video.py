from apiclient.discovery import build #pip install google-api-python-client
from apiclient.errors import HttpError #pip install google-api-python-client
from oauth2client.tools import argparser
import argparse #pip install oauth2client

import json
import csv
from BeautifulSoup import BeautifulSoup
import requests
from urllib2 import urlopen



DEVELOPER_KEY = 'AIzaSyBhxLBOS3mGUOsIYTleo1dXXtDfXMeyFa0'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_videos_by_keyword(query):
	parser=argparse.ArgumentParser()
	parser.add_argument("--q", help="efwef", default=query)
	parser.add_argument("--max-results", help="maxResults", default=50)


	args = parser.parse_args()
	options = args

	next_page=''
	
	i=0
	while i<9:
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
		search_response = youtube.search().list(q=options.q, type="video", part="id,snippet", maxResults=options.max_results,pageToken=next_page).execute()
#########====================
	
		next_page=search_response['nextPageToken']
		print next_page
		print i

		with open('records.csv', 'a') as csvfile:
			fieldnames = ['type_p','title','thumbnail','video']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for item in search_response['items']:
				type_p=item['id']['kind'].split('#')[1]
				title=item['snippet']['title']
				thumbnail=item['snippet']['thumbnails']['medium']['url']
				video="https://www.youtube.com/watch?v="+item['id']['videoId']
				writer.writerow({'type_p':type_p.encode("utf8"), 'title': title.encode("utf8"),'thumbnail':thumbnail.encode("utf8"),'video':video.encode("utf8")})
		i=i+1
	
def video_info(url):
	

	html_source_code=urlopen(url).read()
	soup=BeautifulSoup(html_source_code)
	mydivs = soup.findAll("meta")
	tempdict={}
	for item in mydivs:
		a=item.attrs
		tempdict[a[0][1]]=a[1][1]
	

	#print tempdict

	url1='https://www.youtube.com/embed/'+url.split('=')[1]
	with open('video_info.csv', 'a') as file_t:
		fieldnames = ['title','url','description','keywords',
		'duration','view_count','datePublished','genre']
		writer = csv.DictWriter(file_t,fieldnames)
			
		writer.writerow({'title':tempdict['title'].encode("utf8"),
			'url':url1.encode("utf8"),
			'description':tempdict['description'].encode("utf8"),
			'keywords':tempdict['keywords'].encode("utf8"),
			'duration':tempdict['duration'].encode("utf8"),
			'view_count':tempdict['interactionCount'].encode("utf8"),
			'datePublished':tempdict['datePublished'].encode("utf8"),
			'genre':tempdict['genre'].encode("utf8")})
	#==on the run compute=====
	#mydivs=soup.findAll("div", { "class" : "content-wrapper" })
	#mydivs[0]('a')[0]['href']
	#mydivs[0]('a')[0]['title']
	#mydivs[0]('span')[1].contents
	#mydivs[0]('span')[2].contents
def all_video_url():
	rdr = csv.reader(open("people.csv", 'rU'), dialect='excel')
	for row in rdr:
		
		query=row[1]+"interview"
		get_videos_by_keyword(query)
def all_video_info():
	rdr = csv.reader(open("records.csv", 'rU'), dialect='excel')
	for row in rdr:
		
		if row[3]!="video":
			row[3]
			video_info(row[3])



#https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=IN&key='AIzaSyBhxLBOS3mGUOsIYTleo1dXXtDfXMeyFa0'


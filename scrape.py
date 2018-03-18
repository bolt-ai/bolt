import requests
import json
import urllib
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--apikey')
parser.add_argument('--cx')
parser.add_argument('--keyword')

args = parser.parse_args()

searchTerm = args.keyword
startIndex = '1'
key = args.apikey
cx = args.cx
searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
    searchTerm + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
    "&searchType=image&count=1"
r = requests.get(searchUrl)
response = r.content.decode('utf-8')
result = json.loads(response)
g=result['items'].pop()
if g['mime'] == 'image/jpeg':
	ext='.jpg'
elif g['mime'] == 'image/png':
	ext='.png'
	
noww=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
urllib.request.urlretrieve(g['link'], 'random/'+noww+'_'+searchTerm+ext)

print('downloaded 1 image of a '+searchTerm+'.')

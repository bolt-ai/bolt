from apiclient.discovery import build
import urllib

service = build("customsearch", "v1",
               developerKey="AIzaSyCCzersxy-m-v7G_ZaeKf4GjKAZnC9GpN8")

res = service.cse().list(
    q='butterfly',
    cx='000253225706237899251:rykc6k4woyc',
    searchType='image',
    num=3,
    imgType='clipart',
    fileType='png',
    safe= 'off'
).execute()

if not 'items' in res:
    print 'No result !!\nres is: {}'.format(res)
else:
    for item in res['items']:
        print('{}:\n\t{}'.format(item['title'], item['link']))
        urllib.urlretrieve(item, "00000001.jpg")

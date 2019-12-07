from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime,timedelta

def date_Format(count):
    now = datetime.now()
    dateGroup = []

    for i in range(count):
        time = datetime(now.year,now.month,now.day)-timedelta(days=i*20)
        print(time.strftime('%Y%m%d'))
        dateGroup.append(str(time.strftime('%Y%m%d')))

    return dateGroup

def id_tokenize(tag):
    movie_id=None
    tag_str = str(tag)
    id_token = tag_str.split('"')
    #print(id_token)
    movie_id = id_token[1].split('=')
    #print(movie_id[1])

    return movie_id[1]

def id_Crawling(date):
    global id
    url = urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date="+date)
    bs = BeautifulSoup(url, 'html.parser')
    body = bs.body

    target = body.find('tbody')
    list = target.find_all('tr')

    for i in range(1, 6):
        id.append(id_tokenize(list[i].find('a')))
        #print("영화추가")


def movieCrawling(count):
    global id

    date = date_Format(count)
    print(date)
    for day in date:
        id_Crawling(day)
    #print("중복제거 전 개수: ",len(id))
    id = list(set(id))
    #print("중복제거 후 개수: ",len(id))

    print(id)

    return id

id=[]

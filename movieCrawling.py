from bs4 import BeautifulSoup
from urllib.request import urlopen

import reviewData
import movieLoad
import reviewCrawling

def review_word(id,title, check,movieGroup,release_date):
    try:
        reviewData.review_analysis(id, title, check,movieGroup,release_date)
    except:
        print("reviewData Error")
#영화 정보 유무확인
def confirm_File(id):
    check = False
    if movieLoad.idmovies_select(id)==1:
        check = True
    return check

def titleCrawling(tag):
    title = tag.find(class_='h_movie').find_all('a')

    return title[0].getText()

def infoCrawling(tag):
    info = []
    group = tag.find_all('span')
    info.append("".join((group[0].text).split()))
    Release_date = ("".join((group[3].text).split())).split('.')
    info.append(Release_date[0] + Release_date[1]+ Release_date[2][:2])
    print(info)
    return info

#영화 크롤링을 위해 페이지 이동
def movieinfo_Crawling(id):
    check = 0
    url = urlopen("https://movie.naver.com/movie/bi/mi/basic.nhn?code="+id)
    bs = BeautifulSoup(url, 'html.parser')
    body = bs.body

    id_target = body.find(class_="mv_info")

    title = titleCrawling(id_target)
    print(title)
    info_target = body.find(class_="info_spec")
    info = infoCrawling(info_target)
    movieGroup = info[0]
    release_date = info[1]
    try:
        if confirm_File(id):
            print("파일이 이미 있습니다.")
            check = 1
        else:
            print("\n크롤링start\n")
            reviewCrawling.reviewWrite(id)
            review_word(id, title, check, movieGroup, release_date)
    except Exception:
        print("id :\t 정보 없음")

    print('review_word() 함수 호출')


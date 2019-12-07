from bs4 import BeautifulSoup
from urllib.request import urlopen

def writeReview(review):
    global f
    f.write(format(review))

def review_Crawling(id):
    global f

    page=0
    search = True


    while search:
        count = 0
        page = page+1
        review_url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code="+str(id)+"&type=after&page="+str(page)
        print("페이지:",review_url)
        review_open = urlopen(review_url)
        review_bs = BeautifulSoup(review_open, 'html.parser')
        review_body = review_bs.body
        review_target = review_body.find(class_="score_result")
        review_pages = review_body.find(class_="paging") #마지막 페이지 확인
        review_list = review_target.find_all('li')
        try:
            review_targetpage = review_pages.find_all('a')
            currentPage = review_targetpage[-2].find('span').getText()
        except:
            print('review_pages = review_body.find(class_="paging") Error')
        print("totalPage:", currentPage)
        for i in range(0,len(review_list)):
            score = review_list[i].find(class_="star_score").find("em").getText()
            print("평점:",score)
            review = review_list[i].find(class_="score_reple").find("p").getText().strip().rstrip('\n')
            if '관람객' in review[:5] or '스포일러가' in review[:30]:
                review = review[30:].strip()
            print("내용:",review)
            for char in review:
                if char=='\"' or char=='\\' or char=='\n' or char=="\t"\
                        or char=="" or char =="" or char=="" or char=="" or char==""\
                        or char=="¿":
                    review=" "
            contents = "{\"score\":"+score+", \"review\":\""+review+"\"}"
            #print(contents)
            writeReview(contents)
            count = count + 1

            if len(review_list) > 9 or count<len(review_list):
                print('리뷰길이:',len(review_list))
                f.write(format(", "))
            elif count !=len(review_list):
                f.write(format(", "))
            print(page, "페이지 리뷰 수 :", count)

        # currentPage 토크나이저 1,000을 1000으로 만들기 위해
        Pagetoken = currentPage.split(',')
        Pagecount = ''
        for token in Pagetoken:
            Pagecount = Pagecount + token
        # 마지막 페이지가 10개일 경우를 대비
        if page > int(Pagecount):
            print("마지막:",Pagecount)
            break


#크롤링 시작함수
def reviewWrite(id):   #영화 id를 받는다
    global f
    print("크롤링시작!!")
    reviewFile = "reviews\\" + id + ".json"  #json파일 만들기
    f = open(reviewFile, 'w', encoding='utf-8')
    f.write(format("{\"reviews\":["))
    review_Crawling(id)  #페이지 크롤링해서 json파일에 입력
    print("검색 끝!")
    f.write(format("]}"))
    f.close()

f = None
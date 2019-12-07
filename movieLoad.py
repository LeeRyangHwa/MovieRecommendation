import pymysql
from datetime import datetime

def sqlconn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='fidghk123',
        db='moviedb',
        charset='utf8'
    )
    return conn

def sql_query(query):
    conn = sqlconn()
    curs = conn.cursor()
    curs.execute(query)
    try:
        conn.commit()
    except:
        print()
    conn.close()

    return curs

def idmovies_select(id):
    check = 0
    curs = sql_query("SELECT * FROM movies WHERE idmovies="+str(id))
    rows = curs.fetchall()
    for i in rows:
#        print(i) #불러오기
 #       print("영화개봉일: ",i[5]) #영화 개봉 날짜 가져오기
        check =1

        if daycheck(i[5]): #영화가 개봉한지 3달이 되지 않은 영화면 check = 0
            check = 0
            print("not")
    print("idmovies_select성공")


    return check

def movietitle_select(title):
    curs = sql_query("SELECT * FROM movies WHERE title="+"'"+title+"'")
    rows = curs.fetchall()
    for i in rows:
        print(i)
    print("movietitle_select성공")

def movie_insert(id, reviewcount, score, title, movieGroup,release_date): # id  reviewCount  score  title
    try:
        query = "INSERT INTO movies (idmovies, reviewcount, Averagescore, title, moviegroup, releasedate)VALUES ("+str(id)+","+str(reviewcount)+','+str(score)+","+"'"+title+"'"+", '"+movieGroup+"', "+"'"+release_date+"')"
        print(query)
        curs = sql_query(query)
        print("insert성공")
    except:
        print("insert 오류")


def keyword_update(id, keyword, wordCount):
    print("id: ",id,"  keyword: ",keyword)
    try:
        print("!!")
#        query = "UPDATE movies SET keyword ='"+keyword+"' WHERE id="+str(id)
#        query = "UPDATE movies SET keyword1 ='"+ keyword[0][0] +"', keyword2 ='"+ keyword[1][0] +"', keyword3 ='"+ keyword[2][0] +"', keyword4 ='"+ keyword[3][0] +"', keyword5 ='"+ keyword[4][0] +"' WHERE idmovies="+str(id)
        for word in keyword:
            word_value = round((word[1]/wordCount*100),3)
            query = "INSERT INTO movie_word (movie_id, word, word_value)VALUES ("+str(id)+",'"+word[0]+"',"+str(word_value)+")"
            print(query)
            curs = sql_query(query)
        print("keyword_update 성공")
    except:
        print("keyword_update 오류")

#오늘 날짜
def nowdate():
    nowday = int(datetime.today().strftime("%Y%m%d"))
    return nowday

#개봉일과 날짜 차이
def daycheck(release):
    check = False
    releaseday = int(release)
    if (nowdate() - releaseday) < 300:
        check = True
    return check
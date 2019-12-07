import movieRankCrawling
import movieCrawling
from datetime import datetime
import time

# 영화 id 가져오기
id_info = movieRankCrawling.movieCrawling(200)  # 인자값으로 날짜 수 입력

# 크롤링
for id in id_info:
    movieCrawling.movieinfo_Crawling(id)

while(True):
    now = datetime.now()
    now_hour = now.hour
    print(now_hour)

    if now_hour <1:
        try:
                   # 영화 id 가져오기
            id_info = movieRankCrawling.movieCrawling(1)  # 인자값으로 날짜 수 입력

            # 크롤링
            for id in id_info:
                movieCrawling.movieinfo_Crawling(id)

            time.sleep(3600)

        except:
            print("Python Crawling error")

    # 대기
    time.sleep(3600)
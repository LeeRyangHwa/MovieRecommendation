#MovieRecommendation Web

### 서비스에 개요
-------------------------------
1. 자신이 좋아하는 영화를 통해 비슷하 영화를 추천해주는 서비스
2. 현재 상영하고 있느 영화를 자신의 성향에 맞게 추천해주는 서비스


### 구현 사항
-------------------------------
**데이터 수집**
-------------------------------
1. 파이썬을 이용하여 네이버영화 페이지를 크롤링
   - 모듈 BeautifulSoup를 사용하여 크롤링
   - 각 영화별 고유코드를 이용하여 영화의 리뷰페이지에 접근
   - 해당 페이지의 평점과 리뷰를 크롤링
   
2. 크롤링한 데이터를 json파일로 정리
   - {score: ,review: } 형태로 정리
   - 영화의 코드번호를 파일이름으로 데이터를 가져오기 쉽게 저장
   
3. json파일 속 리뷰를 형태소 분석을 통해 명사단위로 나눕니다.
   - Twitter 모듈을 사용하여 리뷰를 명사로 분리

4. 긍정단어로 분류 될 수 있는 단어를 추출
   - 해당 단어들을 함께 크롤링한 평점을 통해 긍정 단어와 부정 단어 분류
   - 단어 중 필요없는 단어를 제거하기위한 작업
   - 정확하 긍정단어를 가져오기위해 부정단어와 겹치는 단어 제외

5. 데이터베이스에 저장합니다.

**서버 구축**
-------------------------------
1. springboot를 사용하여 서버를 만들고 jsp로 만들어진 페이지와 데이터를 주고 받음
2. 데이터베이스는 jpa를 사용하여 접근
3. 페이지는 bootstrap을 사용하여 페이지구성
4. char.js를 이용하여 사용자 데이터 시각화


**영화 추천과정**
-------------------------------
1. springboot에서 사용자가 좋아하는 영화 데이터가져옴
2. 가지고 온 단어들 중에 가장 비슷한 단어를 포함하고 있는 영화를 추출
3. 가져온 영화 중 평점이 높은 순서로 추천을 해주고 최신 영화는 사용자가 많이 찾는 장르 위주로 추천

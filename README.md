# MovieRecommendation
영화추천 웹페이지 만들기 프로젝트

springboot를 이용하여 서버구축

python에서 네이버 영화를 데이터 크롤링하여 데이터 수집

데이터 수집과정
- 네이버영화 페이지에 사람들이 적은 리뷰와 평점을 크롤링하여 json파일로 정리를 합니다.
- json파일 속 리뷰를 형태소 분석을 통해 명사단위로 나눕니다.
- 해당 단어들 중 긍정 단어로 분류 될 수 있는 단어를 추출하여 추출된 단어중 많이 나온 단어를 데이터베이스에 저장합니다.


영화 추천과정
- 현재 내가 좋아하고 있는 영화들의 긍정단어들을 데이터베이스에서 가져옵니다.
- 가지고 온 단어들 중에 가장 비슷한 단어를 포함하고 있는 영화를 추출하여 추천합니다.

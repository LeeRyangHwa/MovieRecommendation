import json
from konlpy.tag import Twitter
import movieLoad
import movieKeywords

def review_wordNouns(review, check):
    global positive_nouns
    global negative_nouns
    twt = Twitter()
    nouns = twt.nouns(review)
    for noun in nouns:
        if len(noun) != 1 and check == 1:
            positive_nouns.append(noun)
        elif len(noun) !=1 and check == 0:
            negative_nouns.append(noun)

def review_analysis(id, title, check, movieGroup,release_date):
    print('review_analysis()실행')
    json_filename = 'reviews\\'+id+'.json' #json 읽기
    global except_word
    #except_word = []
    #except_word.append(title) #template
    print('제목:' ,title)
    with open(json_filename,encoding='utf8')as jsonText:
        json_data = json.load(jsonText)
        #print(json_data)

    global positive_nouns
    global negative_nouns
    positive_nouns = []
    negative_nouns = []
    count =0
    TotalScore=0

    for review in json_data["reviews"]:
        count = count + 1
        score = review['score']
        reviewText = review["review"]
        TotalScore = TotalScore+score
        #print("점수: ", score)
        #print("리뷰: ", reviewText)
        if score > 7:
            review_wordNouns(reviewText,1)
        elif score < 4:
            review_wordNouns(reviewText,0)

    print("\n")
    print("총 ",count,"개의 리뷰")
    AvgScore = round(TotalScore/count,2)
    print("점수 평균: ",AvgScore)
    print("check: ", check)

    if check == 0:
        print("insert 호출")
        movieLoad.movie_insert(id, count, AvgScore, title, movieGroup, release_date)
    print("insert 호출")
    #movieLoad.movie_insert(id, count, AvgScore, title, movieGroup, release_date)

    print("긍정단어:", positive_nouns)
    print("부정단어:", negative_nouns)

    movieKeywords.keywords(positive_nouns,negative_nouns, title, id)

positive_nouns = []
negative_nouns = []
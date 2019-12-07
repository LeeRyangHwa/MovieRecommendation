from collections import Counter
import ReviewGraph
import movieLoad

def GraphDraw(Nouns, title):
    ReviewGraph.graphDraw(Nouns, title)

def NounCounter(Noun):
    data = []
    count = Counter(Noun)
    Nouns = count.most_common(NounCount)

    print("총 단어 수:",len(Noun))
    print("단어 수: ",Nouns)

    data=[len(Noun),Nouns]

    return data

def ketwordClassification(nouns_A, nouns_B):
    check = True

    for i in range(NounCount):
        check = True
        for j in range(NounCount):
            if nouns_B[j][0] != None:

                if nouns_A[i][0] in nouns_B[j][0]:
                    check = False
        if check:
            keyword_nouns.append(nouns_A[i])

def Remove_UnnecessaryWords():
    count =0
    for i in range(len(keyword_nouns)):
        for noun in keyword_nouns:
            if noun[0] in Unnecessary_words:
                keyword_nouns.remove(noun)

def KeywordUpdate(id, keywords,wordCount):

    movieLoad.keyword_update(id, keywords,wordCount)

def keywords(positive_nouns, negative_nouns, title, id):
    global keyword_nouns
    keyword_nouns=[]
    print('keyword() 실행')

    positive = NounCounter(positive_nouns)
    negative = NounCounter(negative_nouns)

    ketwordClassification(positive[1], negative[1])
    Remove_UnnecessaryWords()

    count = 0
    for i in keyword_nouns:
        count  = count+i[1]

    print("단어 10개:",keyword_nouns[:10])
    #KeywordUpdate(id, keyword_nouns[:5],positive[0])
    KeywordUpdate(id, keyword_nouns[:5], count)
    GraphDraw(keyword_nouns[:10],title)



keyword_nouns = []
NounCount = 50
Unnecessary_words = ['역시', '최고', '영화로', '부분', '이상', '나름', '존잼','대안','대박','관람객','추천','다른',
                     '기대', '개인','다시','끼리','보기','우리','정말','올해','다음','아주','조금','간만','한번',
                     '연기력','다가','대한','세상','완전','장기','비교','때문','연기','마지막', '정도','강추','내용'
                     '모습','댓글','중간','처음','후반','전편','보고','생각','한국영','진짜','약간','그냥','위해',
                     '지금','평점','최고다','후회','제일','역대','계속','초반','이번','라면','이제','존재','대해',
                     '모든', '모두']

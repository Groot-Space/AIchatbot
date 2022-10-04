from konlpy.tag import Komoran

class Preprocess:
    '''
    preprocess 클래스가 생성될 때 형태소 분석기 인스턴스 객체를 생성.
    여기서 형태소 분석기는 코모란을 사용.
    userdic 인자에는 사용자 정의 사전 파일의 경로를 입력 가능.
    '''
    def __init__(self, userdic=None):
        #형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        #제외할 품사
        '''
        형태소 분석기 인스턴스 객체 생성 이후 어떤 품사를 불용어로 정의할지 클래스 맴버 변수인 exclusion_tags 리스트에 정의
        즉, 해당 리스트에 정의된 품사들은 불용어로 정의되어 핵심 키워드에서 제외 됨.
        '''
        #참조 : https://docs.komoran.kr/firststep/postypes.html
        #관계언 제거, 기호 제거
        #어미 제거
        #접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG','JKO','JKB','JKV','JKQ',
            'JX','JC',
            'SF','SP','SS','SE','SO',
            'XSN','XSV','XSA'
        ]

        #형태소 분석기 POS 태거
        '''
        코모란 형태소 분석기의 POS 태거를 호출하는 메서드.
        이 메서드는 Preprocess 클래스 외부에서는 코모란 형태소 분석기 객체를 직접적으로 호출할 일이 없게 하기 위해 정의한 래퍼 함수.
        형태소 분석기 종류를 바꾸게 될 경우 이 래퍼 함수 내용만 변경하면 되므로 유지보수 측면에서 장점이 많음.
        '''
    def pos(self, sentence):
        return self.komoran.pos(sentence)

        #불용어 제거 후 필요한 품사 정보만 가져오기
    '''
    불용어를 제거한 후 핵심 키워드 정보만 가져오는 함수.
    생성자에서 정의한 self.exclusion_tags 리스트에 해당하지 않는 품사 정보만 키워드로 저장.
    '''
    def get_keywords(self, pos, without_tag = False):
        f = lambda x : x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list
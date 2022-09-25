import pymysql

db = None
try :
    db = pymysql.connect(
        host = '127.0.0.1', #데이터 베이스가 존재하는 호스트 주소
        user = 'root', #데이터베이스 로그인 유저
        passwd = 'MNonstyle39', #데이터베이스 로그인 패스워드
        db='chatbotdb', #데이터베이스 명
        charset ='utf8' #데이터베이스에서 사용할 charset 인코딩
    )

    #db.close() db를 이용한 다음에는 반드시 db를 닫아야 함. 데이터베이스 서버에 한동안 연결이 남아 있기 때문에 서버 리소스 활용에 좋지가 않음.
    print('DB 연결 성공')

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print('DB 연결 닫기 성공')
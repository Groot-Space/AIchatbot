import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host = '127.0.0.1', #데이터 베이스가 존재하는 호스트 주소
        user = 'root', #데이터베이스 로그인 유저
        passwd = 'MNonstyle39', #데이터베이스 로그인 패스워드
        db='chatbotdb', #데이터베이스 명
        charset ='utf8' #데이터베이스에서 사용할 charset 인코딩
    )

    # 데이터 삽입 sql 정의
    sql = '''
    INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    '''

    # 데이터 삽입
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
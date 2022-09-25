import pymysql
import pandas as pd

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

    # 데이터 정의
    students = [
        {'name': 'Kei', 'age': 36, 'address' : 'PUSAN'},
        {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
        {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
        {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
        {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    ]

    # 데이터 db에 추가
    for s in students:
        with db.cursor() as cursor:
            sql = '''
                    insert tb_student(name, age, address) values("%s",%d,"%s")
                    ''' % (s['name'], s['age'], s['address'])
            cursor.execute(sql)
    db.commit() # 커밋

    # 30대 학생만 조회
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
        select * from tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall() #검색 결과를 받아오는 함수. 딕셔너리 형태로 반환.
    print(results)

    # 이름 검색
    cond_name = 'Grace'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
        select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone() # 1개의 행만 받아오는 함수.
    print(result['name'], result['age'])

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
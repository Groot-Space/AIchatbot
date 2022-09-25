import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='MNonstyle39',
        db='homestead',
        charset='utf8'
    )

    # 테이블 생성 sql 정의
    sql = '''
    CREATE TABLE tb_student (
        id int primary key auto_increment not null,
        name varchar(32),
        age int,
        address varchar(32)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    '''
    연결한 DB와 상호작용을 위한 cursor 객체
    cursor 객체는 우리가 임의로 생성할 수 없으며, 반드시 DB 호스트에 연결된 객체(db)의 cursor()함수로 cursor객체를 받아와야 함.
    cursor 객체의 execute()함수로 sql구문을 실행함. with 구문 내에서 cursor 객체를 사용하기 때문에 사용 후에는 자동으로 메모리에서 해제됩니다.
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
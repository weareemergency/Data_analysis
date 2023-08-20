import mysql.connector

# MySQL 서버에 연결
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mirror"
)

# 커서 생성
cursor = db_connection.cursor()

# 여러 데이터를 추가할 데이터 목록
data_to_insert = [
('yyb', '1234', '양유빈'),  
('ljs', '1234', '이지석'),
('kbc', '1234', '김병찬'),
('ydh', '1234', '윤동현'),
('pms', '1234', '박민성'),
('lmj', '1234', '이민준'),
('sjw', '1234', '손정웅'),
('lyc', '1234', '이윤찬')
]

# 여러 데이터 추가를 위한 SQL 쿼리
insert_query = "INSERT INTO user (user_id, user_pw, user_name) VALUES (%s, %s, %s)"

# 데이터 추가 실행
cursor.executemany(insert_query, data_to_insert)

# 변경사항 커밋
db_connection.commit()

# 커넥션과 커서 닫기
cursor.close()
db_connection.close()

print("데이터 추가 완료")

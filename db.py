#xampp 사용해서 테이블에 값 넣기
import mysql.connector

# MySQL 서버 연결 설정
db_config = {
    "host": "localhost",
    "user": "root",       # 사용자명
    "password": "",       # 비밀번호
    "database": "mirror"  # 사용할 데이터베이스명
}

# MySQL 서버에 연결
conn = mysql.connector.connect(**db_config)

# 커서 생성
cursor = conn.cursor() # db와  상호작용 중재하며 데이터를 쿼리하고 조작 할수 있음

# 새 데이터 추가
insert_query = "INSERT INTO user (user_id, user_pw, user_name) VALUES (%s, %s, %s)"
data_to_insert = [
    ("yyb", "1234", "양유빈"),  # 적절한 데이터 값 입력
    ("ljs", "1234", "이지석"),
    ("kbc", "1234", "김병찬"),
    ("ydh", "1234", "윤동현"),
    ("bms", "1234", "박민성"), 
    ("lmj", "1234", "이민준"),
    ("sjw", "1234", "손정웅"),
    ("lyc", "1234", "이윤찬")
]
cursor.execute(insert_query, data_to_insert)
conn.commit()  # 변경 사항 저장

# # SQL 쿼리 실행
# select_query = "SELECT * FROM user"
# cursor.execute(select_query)

# # 결과 출력
# for row in cursor:
#     user_id, user_pw, user_name = row
#     print(f"User ID: {user_id}, User Name: {user_name}, User Password: {user_pw}")


# 연결 종료
cursor.close()
conn.close()

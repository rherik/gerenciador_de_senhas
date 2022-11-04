import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM ')


conexao.close()

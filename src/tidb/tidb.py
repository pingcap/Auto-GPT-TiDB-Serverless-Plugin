import os
import pymysql
import pymysql.cursors

def get_conn():
    return pymysql.connect(
        host=os.getenv('TIDB_HOST'),
        port=int(os.getenv('TIDB_PORT')),
        user=os.getenv('TIDB_USER'),
        password=os.getenv('TIDB_PASSWORD'),
        database=os.getenv('TIDB_DATABASE'),
        charset=os.getenv('TIDB_CHARSET', 'utf8mb4'),
        ssl_ca=os.getenv('SSL_CA_PATH', '/etc/ssl/cert.pem'),
    )

def tidb_sql_executor(sql: str):
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        field_names = tuple(i[0] for i in cursor.description)
        result = list(result)
        result.insert(0, field_names)
        return result
    except pymysql.err.ProgrammingError as e:
        return str(e)



if __name__ == '__main__':
    print(tidb_sql_executor('show databases;'))

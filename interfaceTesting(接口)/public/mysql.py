import pymysql

def datasql(self):
    try:
        conn = pymysql.connect(
                host = '192.168.117.9',
                port = 3306,
                user = 'mysql',
                password = '123',
                db = 'jforum',
                charset = 'utf8'
            )
    except Exception as e:
        print(e)

    obj = conn.cursor(cursor=pymysql.cursors.DictCursor)

    obj.execute(self)
    data = obj.fetchmany()
    return data

if __name__ == "__main__":
    # sql = "SELECT COUNT(post_id) from jforum_posts;"

    sql = "SELECT count(post_id) from jforum_posts;"


    accept = datasql(sql)
    print(accept)
    print(accept[0]['count(post_id)'])
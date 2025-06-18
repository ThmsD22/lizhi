import pymysql


def get_cursor():
    connect = pymysql.connect(
        user='root',
        password='000000',
        host='127.0.0.1',
        database='vue'
    )
    cursor = connect.cursor()
    return cursor


def get_tuijian():
    cursor = get_cursor()
    sql = 'select * from tuijian'
    cursor.execute(sql)
    result = cursor.fetchall()
    data = [{
        'id': item[0],
        'title': item[1]
    } for item in result]
    return data


def get_hot():
    cursor = get_cursor()
    sql = 'select * from redu'
    cursor.execute(sql)
    result = cursor.fetchall()
    data = [{
        'id': item[0],
        'title': item[1]
    } for item in result]
    return data


def get_jiaoyi():
    cursor = get_cursor()
    sql = 'select * from jiaoyi'
    cursor.execute(sql)
    result = cursor.fetchall()
    data = [{
        'id': item[0],
        'title': item[1]
    } for item in result]
    return data


if __name__ == '__main__':
    print(get_tuijian())

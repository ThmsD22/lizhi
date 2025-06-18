import json

import pymysql


def get_mian_data():
    connect = pymysql.connect(
        user='root',
        password='000000',
        host='127.0.0.1',
        database='vue'
    )
    cursor = connect.cursor()

    sql = "select * from main"
    cursor.execute(sql)
    res = cursor.fetchall()
    dict_list = [
        {
            'img': item[0],
            'title': item[1],
            # 'date': item[5],
            # 'author': item[6],
            # 'text': item[7],
            # 'type': item[9],
            'date': item[2],
            'author': item[3],
            'text': item[4],
            'type': item[5],
        }
        for item in res
    ]
    # print(dict_list)
    return dict_list



if __name__ == '__main__':
    get_mian_data()

import pymysql


# login
def login(email, password):
    """
    :param username: username
    :param password: password
    :return: username, avatar
    """
    connect = pymysql.connect(
        user='root',
        password='000000',
        host='127.0.0.1',
        database='vue'
    )
    cursor = connect.cursor()
    sql1 = 'select email from user where email=%s'
    cursor.execute(sql1, (email,))
    result1 = cursor.fetchone()
    if not result1:
        connect.close()
        pass
    else:
        sql = 'select username, avatar from user where email=%s and password=%s'
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()
        if result:
            return {"user": {
                "name": result[0],
                "avatar": result[1]
            }}


# register
def register(username, email, password):
    """
    :param username:
    :param email:
    :param password:
    :return:
    """
    # 数据库查询，如果用户存在就返回已存在，否则就注册
    msg = {
        'msg': '',
        'code': 0
    }
    connect = pymysql.connect(
        user='root',
        password='000000',
        host='127.0.0.1',
        database='vue'
    )
    cursor = connect.cursor()
    sql = 'select email from user where email=%s'
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    if result:
        connect.close()
        msg['msg'] = '用户已存在'
    else:
        sql = 'insert into user(username, email, avatar, password) values(%s, %s,%s, %s)'
        cursor.execute(sql, (username, email, '', password))
        connect.commit()
        connect.close()
        msg['msg'] = '注册成功'
    return msg


if __name__ == '__main__':
    print(login('3139312973@qq.com', '123456'))
    # print(register('lx1', '3139312972@qq.com', '123456'))

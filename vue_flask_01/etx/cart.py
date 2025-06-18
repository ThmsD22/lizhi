import pymysql


def get_cart():
    connect = pymysql.connect(
        user='root',
        password='000000',
        host='127.0.0.1',
        database='vue'
    )
    cursor = connect.cursor()

    sql = "select * from cart"
    cursor.execute(sql)
    res = cursor.fetchall()
    dict_list = [
        {
            'storeName': item[0],
            'img': item[1],
            'info': item[2],
            'count': item[3],
            'price': item[4]
        }
        for item in res
    ]
    # print(dict_list)
    return dict_list


"""
创建cart表

CREATE TABLE cart 
(
    storeName	VARCHAR(512),
    img	VARCHAR(512),
    info	VARCHAR(512),
    count   INT,
    price	INT
);

INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');
INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');
INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');
INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');
INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');
INSERT INTO cart (storeName, img, info, count, price) VALUES ('成都理工', 'https://tse4-mm.cn.bing.net/th/id/OIP-C.sTDIe3Whf-vX9_-JNCOBeAHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7', '12435678980-', '1', '199');

"""

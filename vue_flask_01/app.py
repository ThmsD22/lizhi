from etx.product import get_mian_data
from etx.cart import get_cart
from etx.auth import login, register
from etx.home import get_tuijian, get_hot, get_jiaoyi
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '12344'
CORS(app)



# 注册
@app.post('/register')
def register_():
    data = request.get_json()
    print("----------------------------")
    name = data["name"]
    email = data["email"]
    password = data["password"]
    # assume that the password and email address will be saved by flask
    # return the register successful message
    data = register(name, email, password)
    return jsonify(data)


# 登录
@app.post('/login')
def login_():
    data = request.get_json()
    # email & password
    email = data["email"]
    password = data["password"]
    data = login(email, password)
    msg = {
        "msg": "登陆成功",
        "code": 0,
        "user": ''
    }
    if email and data:
        msg["user"] = data
        # assume that the password and email address are verified here
        return jsonify(msg)
    else:
        return jsonify({
            "msg": "用户不存在",
            "code": -1
        })


# store界面
@app.get('/product')
def product():
    product_data = get_mian_data()
    return {
        "data": product_data,
        "code": 0
    }


# 购物车
@app.get('/cart_data')
def cart():
    cart_data = get_cart()
    return {
        "data": cart_data,
        "code": 0
    }


@app.get('/home')
def home():
    data = {
        'tuijian': get_tuijian(),
        'jiaoyi': get_jiaoyi(),
        'redu': get_hot()
    }
    return data


if __name__ == '__main__':
    app.run(port=55555, debug=True)

from flask import Flask
from jinja2 import evalcontextfilter, Markup, escape
from flask import render_template
from view import views
from templates import *
from flask import session
from flask import redirect,url_for,request
from model.verification_code import verification_code
from io import StringIO,BytesIO

app = Flask(__name__, template_folder='../templates',static_folder="",static_url_path="")
app.secret_key = 'djstl'

vc = verification_code(100,30)
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sign_up')
def sign_up():
    return "sign_up"


@app.route('/sign_in')
def sign_in():
    return render_template("signin.html")

async def validate(username, password, verify_code):
    await False

@app.route('/auth', methods=['post','get'])
def auth():
    username = request.form["username"]
    password = request.form["password"]
    verify_code = request.form["vc_input"]
    vr = validate(username,password,verify_code)
    if vr == True:
        return redirect(url_for("sign_in"))
    else:
        session["username"] = username
        session["password"] = password
        return redirect(url_for("u", user_name=username))


@app.route('/u/<user_name>', methods=['get','post'])
def u(user_name: str):
    # session 无值？？
    # return "welcome "+session["username"]
    return render_template("main.html",user_name=user_name)


def test_args(*args, **kwargs):
     return render_template("main_bak.html", title="test_template" , \
                           users= [{"url": "url1", "username":"u1"}, {"url": "url2", "username":"u2"}])
    #return render_template("args.html", args=args, kwargs=kwargs)


@app.route('/test_template')
def test_template():
    # 可变参数的调用方式
    return test_args("u1", "u2", u1="url1", u2="url2")
    #return render_template("template_t.html", title="test_template" , \
    #                      users= [{"url": "url1", "username":"u1"}, {"url": "url2", "username":"u2"}])


"""
@app.route('/A')
def A():
    return  redirect(location='./B')


@app.route('/B')
def B():
    return "this is b"
"""

@app.route('/verify_code')
def verify_code():
    """生成验证码数据"""
    image, str = vc.draw()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = str
    print(session['image'])
    return response
    # return app.make_response(str)

#if __name__ == '__main__':
#    app.run()
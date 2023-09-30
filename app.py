from flask import Flask, render_template, url_for, request ,session
from flask_session import Session
from flask_wtf.csrf import CSRFProtect ,generate_csrf
from .config import SECRET_KEY

#Flaskのインスタンスを生成
#flaskでアプリを作りますよってやつ。

app = Flask(__name__, static_folder="./templates/imagebox")
app.config['SECRET_KEY'] = '306cf1aff2196801ea027556d43b6f618323d62238e1849ec9193a2157eb35c0'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

var = session.get('result')   #キーがない可能性がある場合
session["result"] = var       #キーが存在する場合


csrf = CSRFProtect()



@app.route("/debug")
def debug():
    return render_template("debug.html")

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")


# html一からではなく、問題集から取ってくる形式にすると大幅削減
# 辞書型で保存して、HTML内でジンジャーテキスト使う



@app.route("/question1", methods=["GET", "POST"])
def question1():
    csrf_token = generate_csrf()

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question1.html")
    else:

        answer=request.form.get("python")
        # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
        cleaned_text = answer.replace('\n', '').replace('\r', '')
        # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
        if cleaned_text == 'print("Hello World!")':
            return render_template('correct1.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)
            # ポストされた時に、テキストをrequest.form.get()で読み込む。


# question1.htmlを正解した時の遷移先。
@app.route("/correct1")
def correct1():
    csrf_token = generate_csrf()
    return render_template("correct1.html", csrf_token=csrf_token)

@app.route('/question2', methods=["GET", "POST"])
def question2():
    csrf_token = generate_csrf()
    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question2.html")
    else:
        answer=request.form.get("python")
        # pythonっていう名前のFormから取ってくるよってこと。question2.htmlから。
        cleaned_text = answer.replace('\n', '').replace('\r', '')

        if cleaned_text == 'print(7)print(9+3)print("9+3")':
            return render_template('correct2.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)


@app.route("/correct2")
def correct2():
    csrf_token = generate_csrf()
    return render_template("correct2.html", csrf_token=csrf_token)

@app.route('/question3', methods=["GET", "POST"])
def question3():
    csrf_token = generate_csrf()
    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question3.html")
    else:
        answer=request.form.get("python")
        # pythonっていう名前。question3.htmlから。
        cleaned_text = answer.replace('\n', '').replace('\r', '')
        if cleaned_text == 'print("7-3")print(2*6)print(24/3)print(12%5)':
            return render_template('correct3.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)

@app.route("/correct3")
def correct3():
    csrf_token = generate_csrf()
    return render_template("correct3.html", csrf_token=csrf_token)

@app.route('/question4', methods=["GET", "POST"])
def question4():
    csrf_token = generate_csrf()
    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question4.html")
    else:
        answer=request.form.get("python")
        # pythonっていう名前。question2.htmlから。
        cleaned_text = answer.replace('\n', '').replace('\r', '')
        if cleaned_text == 'mojiretu = "あいうえお"suuti = 8print(mojiretu)print(suuti)':
            return render_template('correct4.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)

@app.route("/correct4")
def correct4():
    csrf_token = generate_csrf()
    return render_template("correct4.html", csrf_token=csrf_token)



@app.route('/question5', methods=["GET", "POST"])
def question5():
    csrf_token = generate_csrf()
    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question5.html")
    else:
        answer=request.form.get("python")
        # pythonっていう名前。question2.htmlから。
        cleaned_text = answer.replace('\n', ' ').replace('\r', ' ')
        clean = cleaned_text.replace(' ', '').replace(' ', '')
        if "=5" in clean and "=3" in clean and "print" in clean and "python" in clean and "楽しい" in clean and "+" in clean:
            return render_template('correct5.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)

@app.route("/correct5")
def correct5():
    csrf_token = generate_csrf()
    return render_template("correct5.html", csrf_token=csrf_token)



@app.route('/question6', methods=["GET", "POST"])
def question6():
    csrf_token = generate_csrf()
    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question6.html")
    else:
        answer=request.form.get("python")
        # pythonっていう名前。question2.htmlから。
        cleaned_text = answer.replace('\n', ' ').replace('\r', ' ')
        clean = cleaned_text.replace(' ', '').replace(' ', '')
        if "=5" in clean and "=3" in clean and "print" in clean and "python" in clean and "楽しい" in clean and "+" in clean:
            return render_template('correct6.html', csrf_token=csrf_token)
        else:
            return render_template('error.html', csrf_token=csrf_token)

@app.route("/correct6")
def correct6():
    csrf_token = generate_csrf()
    return render_template("correct6.html", csrf_token=csrf_token)









# ページを作るときは、app.py に def 記述して、その後に html を作る。それだけでいい。

# 不正解の時の遷移先
@app.route("/error")
def error():
    csrf_token = generate_csrf()
    return render_template("error.html", csrf_token=csrf_token)

if __name__=="__main__":
    #CSRF保護を初期化。CSRF拡張機能を用いて、CSRF保護を追加する。
    csrf.init_app(app)

    #デバッグモード有効化はTrue,無効化がFalse。
    app.run(debug=False)


from flask import Flask,render_template,request

server = Flask(__name__,static_url_path='')
port=5500
ip="192.168.3.50:%s"%port

@server.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@server.route('/', methods=["get"])
def index():
    return render_template("index.html",**{"local":ip})

@server.route('/check', methods=["get"])
def check():
    music_name = request.args.get("usr")+".mp3"
    tip = request.args.get("pwd")
    print(music_name,tip)
    import os
    files = os.listdir('static')
    print(files)
    mp3s = []
    for file in files:
        if ".mp3" in file:
            mp3s.append(file)
    print(mp3s)
    check=(music_name in mp3s) and (int(tip)>=5)
    if check:
        return music_name
    else:
        return "0"

@server.route('/play', methods=["get"])
def play():
    file = request.args.get("file")
    music_file="http://"+ip+"/%s"%file
    print(music_file)
    return render_template("music.html", **{"music_file":music_file})



if __name__ == "__main__":
    server.run(host="0.0.0.0",port=port)

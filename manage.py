# -*-coding:utf-8-*-
from flask import Flask, render_template
from flask import request
import time

app = Flask(__name__)

# 首页面
@app.route("/")
def index():
	return render_template("index.html")

# 结束录音
@app.route("/stopSpeech", methods=["GET", "POST"])
def stopRecorder():
	print("停止录音……")
	speechRecorder.stop()
	end = time.time()
	return "200"



if __name__ == '__main__':
	# 启动多线程参数，加快资源请求，快速响应用户
	app.run(debug = True, host='127.0.0.1', port=5000, threaded = True)

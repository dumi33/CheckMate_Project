import json
from flask import Flask, make_response, render_template, request, jsonify, redirect
import pymongo
from config import CLIENT_ID, REDIRECT_URI
from controller import Oauth
from model import UserModel, UserData
from PIL import ImageGrab, Image
import pyautogui as pag
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    get_jwt_identity, jwt_required,
    set_access_cookies, set_refresh_cookies, 
    unset_jwt_cookies, create_refresh_token
)


import os # aim_model이 같은 디렉토리에 있어서 path를 앞에 붙임 
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ai_model import Embedding
#print(p_dir.exists())
#from ai_model.Embedding import Create_Embedding
#from ai_model import Embedding
from flask_cors import CORS

#from mongodb import Class
app = Flask(__name__) # 객체 생성
CORS(app, resources={r'*': {'origins': '*'}})
 

conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')
mydb = conn.CHECKMATE
Class =mydb.Class
Student =mydb.Student
Attendance =mydb.Attendance
CaptureImg =mydb.CaptureImg


# 버튼을 클릭하면 여기로 
@app.route('/oauth/url')
def oauth_url_api():
    """
    Kakao OAuth URL 가져오기
    """
    kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
       % (CLIENT_ID, REDIRECT_URI)
    # return jsonify(
    #     kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
    #     % (CLIENT_ID, REDIRECT_URI)
    # )
    return redirect(kakao_oauth_url)

# redirect된 주소 
@app.route("/oauth")
def oauth_api():
    # 사용자로부터 authorization code를 인자로 받음
    code = str(request.args.get('code'))
    
    # 전달받은 authorization code를 통해서
    # access_token, refresh_token을 발급
    oauth = Oauth()
    auth_info = oauth.auth(code)
    
    # access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    # 해당 식별 정보를 서비스 DB에 저장 (회원가입)
    # 만약 이미 있을 경우, 과정 스킵
    user = UserData(user)
    UserModel().upsert_user(user)

    # 사용자 식별 id를 바탕으로 서비스 전용 access_token, refresh_token 발급
     
    # resp = make_response(render_template('index2.html'))
    # access_token = create_access_token(identity=user.id)
    # refresh_token = create_refresh_token(identity=user.id)
    # resp.set_cookie("logined", "true")
    # set_access_cookies(resp, access_token)
    # set_refresh_cookies(resp, refresh_token)

    return render_template('index2.html')



@app.route("/")
def hello() :
    return "<h1>HELLO CHECKMATE!</h1>"
    

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")



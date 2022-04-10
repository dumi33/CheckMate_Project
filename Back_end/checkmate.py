import json
from sre_constants import SUCCESS
import numpy as np
from flask import Flask, make_response, render_template, request, jsonify, redirect
import pymongo
from tkinter import filedialog
from config import CLIENT_ID, REDIRECT_URI
from controller import Oauth
from model import UserModel, UserData
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

#from mongodb import Class
app = Flask(__name__) # 객체 생성 


conn = pymongo.MongoClient()
mydb = conn.CHECKMATE
Class =mydb.Class
Student =mydb.Student
User = mydb.Users


@app.route("/")
def index():
    return render_template('index2.html')


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


@app.route("/class")
def hello() :
    return "<h1>HELLO CHECKMATE!</h1>"

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



@app.route("/class/login")
def helloUser() :
    return render_template('Create_class.html')

def AddStduentImg () :
            dir_path = filedialog.askdirectory(initialdir="/",title='Please select a directory')
            return dir_path
        
        
#  auto increment # studentIdx을 반환
def getNextSequence() :
    Student.update_one(
          {'studentIdx': 'stdIdx'},
          {
              '$inc': 
              {
                'seq': 1}
            }
          , upsert=False
    )
    
    value = Student.find_one({"studentIdx": 'stdIdx'})
    return value['seq']

# student 추가 
@app.route("/students",methods=['POST']) # 라우팅경로
def CreateStduentEmbedding() :
    if request.method =='POST' :
        Img_students_addr = AddStduentImg() # 학생들의 사진 폴더를 선택 
        evaluation_embs, evaluation_labels = Embedding.Create_Embedding(Img_students_addr)
        embedding_value = list(evaluation_embs[0])
        print(embedding_value)
        Student.insert_one(
                {
                    "embedding" : embedding_value
                }
            ) 
        
        # for i in range(len(evaluation_labels)) : 
        #     Student.insert_one(
        #         {
        #             "studentIdx" : getNextSequence(),
        #             "name": evaluation_labels[i],
        #             "embedding" : list(evaluation_embs[i])
        #         }
        #     ) 
        
        return make_response(jsonify(SUCCESS=True),200)
    
# Class 추가
@app.route("/classes",methods=['POST']) # 라우팅경로
def ClassCreate() :
    if request.method =='POST' :
        data = request.get_json()
        Class.insert_one(data)
        return make_response(jsonify(SUCCESS=True),200)
    
    
# Class 이름변경
@app.route("/classes/<int:classIdx>",methods=['PATCH']) # 라우팅경로
def ClassNameChange(classIdx) :
    if request.method =='PATCH' :
        data = request.get_json()
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"name" : data['name']}
                }
            ) 
        return make_response(jsonify(SUCCESS=True),200)
    


    

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")



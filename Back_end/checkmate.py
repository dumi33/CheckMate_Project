import json
from sre_constants import SUCCESS
import numpy as np
from flask import Flask, make_response, render_template, request, jsonify, redirect
import pymongo
from tkinter import filedialog
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

from bson import json_util
import os # aim_model이 같은 디렉토리에 있어서 path를 앞에 붙임 
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ai_model import Embedding
#print(p_dir.exists())
#from ai_model.Embedding import Create_Embedding
#from ai_model import Embedding

#from mongodb import Class
app = Flask(__name__) # 객체 생성 


#conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.35.24.5:27017')
conn = pymongo.MongoClient()
mydb = conn.CHECKMATE
Class =mydb.Class
Student =mydb.Student
User = mydb.Users
ClassList = mydb.ClassList


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
def getNextSequenceSTD() :
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

#  auto increment # studentIdx을 반환
def getNextSequenceCLA() :
    Class.update_one(
          {'classIdx': 'classIdx'},
          {
              '$inc': 
              {
                'seq': 1}
            }
          , upsert=False
    )
    
    value = Class.find_one({"classIdx": 'classIdx'})
    return value['seq']

# student 추가 
@app.route("/students/<int:classIdx>",methods=['POST']) # 라우팅경로
def CreateStduent(classIdx) :
    if request.method =='POST' :
        label = []
        Img_students_addr = AddStduentImg() # 학생들의 사진 폴더를 선택 
        evaluation_labels = os.listdir(Img_students_addr) # 사진들의 이름을 추출
        for evaluation_label in evaluation_labels :  # 확장자 제거 
            label.append(evaluation_label.rsplit('_')[0])
        studentList = []
        for i in range(len(label)) :
            seq = getNextSequenceSTD()
            student= {"studentIdx" : seq,
                    "name": label[i],
                    "classIdx" : classIdx,
                    "status" : 'active'}
            Student.insert_one({
                    "studentIdx" : seq,
                    "name": label[i],
                    "classIdx" : classIdx,
                    "status" : 'active'}) 
            
            studentList.append(student)
        
        
        return make_response(jsonify(SUCCESS=True,data=studentList),200)
    
# student 제거  
# status를 deleted로 변경 
@app.route("/students/<int:studentIdx>",methods=['PATCH'])
def DeleteStduent(studentIdx) :
    if request.method =='PATCH' :
        Student.update_one({"studentIdx" : studentIdx}, 
                {   "$set" :
                    {"status" : 'deleted'}
                }
            ) 
        return make_response(jsonify(SUCCESS=True),200)
    
    
# student 조회
@app.route("/students/<int:classIdx>",methods=['GET'])
def GetStduent(classIdx) :
    if request.method =='GET' :
        Students=list(Student.find({"classIdx" : classIdx},{"_id" : 0}))
            
    return jsonify(Students)

# @app.route("/classes/students/<int:classIdx>",methods=['GET'])
# def GetClassStduent(classIdx) :
#     if request.method =='GET' :
#         classess=list(Student.find({"classIdx" : classIdx},{"_id" : 0}))
#         # for student in Students[1:] : # auto increment를 위한 element 제외 
#         #     temp = {'studentIdx' : student['studentIdx'],'name' : student['name'],'status' :student['status']}
#         #     student_info.append(temp)
            
#     return jsonify(classess[1:])

    
# Class 추가
@app.route("/classes",methods=['POST']) # 라우팅경로
def ClassCreate() :
    if request.method =='POST' :
        data = request.get_json() # 입력받은 class 정보  
        seq = getNextSequenceCLA()
        class_info= {"classIdx" : seq, # 저장할 값 
                "className": data['className'],
                "userIdx" : data['userIdx'],
                "studentIdx" : data['studentIdx'],
                "status" : 'active'}
        Class.insert_one(
            {
                "classIdx" : seq,
                "className": data['className'],
                "userIdx" : data['userIdx'],
                "studentIdx" : data['studentIdx'],
                "status" : 'active'
            }
        ) 
        return make_response(jsonify(SUCCESS=True,data=class_info),200)
    
    
# Class 이름변경
@app.route("/classes/classname/<int:classIdx>",methods=['PATCH']) # 라우팅경로
def ClassNameChange(classIdx) :
    if request.method =='PATCH' :
        data = request.get_json() # 이름을 변경할 이름을 입력받음 
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"className" : data['className']}
                }
            ) 
        return make_response(jsonify(SUCCESS=True,data = data['className']),200)
    
# class 조회
@app.route("/classes/<int:userIdx>",methods=['GET'])
def GetClass(userIdx) :
    if request.method =='GET' :
        classes=list(Class.find({"userIdx" : userIdx},{"_id" : 0}))
            
    return jsonify(classes)


    



# class 제거  
# status를 deleted로 변경 
@app.route("/classes/<int:classIdx>",methods=['PATCH'])
def DeleteClass(classIdx) :
    if request.method =='PATCH' :
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"status" : 'deleted'}
                }
            ) 
        return make_response(jsonify(SUCCESS=True,data = {"status" : 'deleted'}),200)
    
    

# 캡쳐  
@app.route("/checks",methods=['POST'])
def PostCapture() :
    if request.method =='POST' :
        img = ImageGrab.grab()
        img.save('capture_img.png')
        
        return make_response(jsonify(SUCCESS=True),200)
    

# 출석확인  
@app.route("/checks/attendance",methods=['POST'])
def PostCheck() :
    if request.method =='POST' :
        global dir_path 
        capture_addr = 'C:/Users/dumi3/checkmate_project2/CheckMate_Project/capture_img.png'
        # 학생들의 임베딩값 추출 & 출석확인 
        result = Embedding.Create_Check(dir_path, capture_addr)
        return make_response(jsonify(SUCCESS=True,data = result),200)

    

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")



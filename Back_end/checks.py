from flask import Blueprint, make_response, render_template, request, jsonify, redirect
import pymongo
from PIL import ImageGrab
from ai_model import Embedding

blue_check=Blueprint("check", __name__, url_prefix="/checks")

conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.39.108.76:27017')
mydb = conn.CHECKMATE
Class =mydb.Class

# 캡쳐  
# /checks
@blue_check.route("/",methods=['POST'])
def CreateCapture() :
    if request.method =='POST' :
        img = ImageGrab.grab()
        img.save('capture_img.png')
        
        return make_response(jsonify(SUCCESS=True),200)

    
    
# 출석확인  
# /checks/attendance/<classIdx>
@blue_check.route("/attendance/<int:classIdx>",methods=['GET'])
def CreatesCheck(classIdx) :
    if request.method =='GET' :
        capture_addr = 'C:/Users/dumi3/checkmate_project2/CheckMate_Project/capture_img.png'
        data = list(Class.find({"classIdx" : classIdx})) # 해당 클래스정보 
        student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
        # 학생들의 임베딩값 추출 & 출석확인
        Embedding.Create_Check(student_img_addr, capture_addr)
        return make_response(jsonify(SUCCESS=True),200)
    
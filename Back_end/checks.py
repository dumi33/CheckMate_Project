from flask import Blueprint, make_response, render_template, request, jsonify, redirect
import pymongo
from PIL import ImageGrab
import datetime as dt


import os # aim_model이 같은 디렉토리에 있어서 path를 앞에 붙임 
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ai_model import Embedding

blue_check=Blueprint("check", __name__, url_prefix="/checks")

conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.39.108.76:27017')
mydb = conn.CHECKMATE
Class =mydb.Class
Student =mydb.Student
Attendance =mydb.Attendance


# # 캡쳐  
# # for test 
# @blue_check.route("/hi",methods=['GET'])
# def fortest() :
#     if request.method =='GET' :
#         print(os.getcwd())

#         return make_response(jsonify(SUCCESS=True),200)


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
@blue_check.route("/attendance/<int:classIdx>",methods=['POST'])
def CreatesCheck(classIdx) :
    if request.method =='POST' :
        capture_addr = os.getcwd() +'\capture_img.png'
        data = list(Class.find({"classIdx" : classIdx})) # 해당 클래스정보 
        student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
        # 학생들의 임베딩값 추출 & 출석확인
        students =Embedding.Create_Check(student_img_addr, capture_addr) # 출석한 학생의 레이블 
        print("출석한 학생은 {}입니다.".format(students))
        classStudentList=list(Student.find({"classIdx" : classIdx},{"_id" : 0, "name":1}))
        
        studentList = [] # 학생의 이름만을 추출 
        for i in range(len(classStudentList)) :
            studentList.append(classStudentList[i]['name'])
            
        noattendance = list(set(studentList) - set(students)) # 모든 학생 중 안온학생을 구함 
        print("출석하지 않은 학생은 {}입니다.".format(noattendance))
        
        x = dt.datetime.now()
        date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
        Attendance.update_one({"classIdx" : classIdx}, # 날짜와 출석하지 않은 학생 DB에 저장 
                {   "$set" :
                    {date : noattendance }
                }
            ) 
        
        return make_response(jsonify(출석=students,미출석=noattendance),200)
    
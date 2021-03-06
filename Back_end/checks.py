from sre_constants import SUCCESS
from flask import Blueprint, make_response, render_template, request, jsonify, redirect
import pymongo
from PIL import ImageGrab, Image
import datetime as dt
from s3_img import *
from s3_img import s3_connection
from config import AWS_S3_BUCKET_NAME
from tkinter import filedialog
from io  import BytesIO
from deepface import DeepFace
import uuid
from retinaface import RetinaFace
import matplotlib.pyplot as plt

import os # aim_model이 같은 디렉토리에 있어서 path를 앞에 붙임 
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ai_model import Embedding
from ai_model import forRetinaFace

blue_check=Blueprint("check", __name__, url_prefix="/checks")

conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')
mydb = conn.CHECKMATE
Class =mydb.Class
Student =mydb.Student
Attendance =mydb.Attendance
CaptureImg =mydb.CaptureImg


s3 = s3_connection()
s4 = s4_connection() # read_image_from_s4 이용을 위해 

## 날짜에 입력된 파일 이름 값 불러오기 
@blue_check.route("/fortest/<int:classIdx>",methods=['GET'])
def fortest3(classIdx) :
    if request.method =='GET' :
        x = dt.datetime.now()
        date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
        #capture_imgList=list(Class.find({"classIdx" : classIdx},{"_id" : 0, "captureImg":1}))
        # capture_imgList=list(CaptureImg.find({"classIdx" : classIdx},{date : {'$exists' : True}}))
        capture_imgList = CaptureImg.find({"$and":[ {date:{"$exists": True}}, {"classIdx":classIdx}]},{"_id" : 0, date:1})
        #capture_imgList=list(CaptureImg.find({"classIdx" : classIdx},{"_id" : 0, date:1}))
        capture_imgList=list(capture_imgList)
        capture_imgList = capture_imgList[0].values()
        capture_imgList = list(capture_imgList)[0]
        #result =capture_imgList[0].values()
        #result=list(result)[0]
        #capture_imgList=capture_imgList[date]
        
        return make_response(jsonify(SUCCESS=True ),200)

## Deepface가 경로가 아닌 이미지로 비교할 수 있을까?
@blue_check.route("/hii",methods=['GET'])
def fortest2() :
    if request.method =='GET' :
        #img=read_image_from_s3(s3,'fortest.jpg')
        # file_name = os.getcwd() +'\capture_img.png' 
        # img = Image.open(file_name)
        # img.show()
        #handle_upload_img(s3,'irene')
        img=read_image_from_s4(s4,'capture_image/irene.jpg')

        buffer = BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)
        
        url_generator = str(uuid.uuid4()) 
        result = DeepFace.verify(img1_path = img, img2_path = "december.jpg")
        print(result)

        
        return make_response(jsonify(SUCCESS=True),200)
    
    
# 캡쳐  
# for test 
@blue_check.route("/hi",methods=['GET'])
def fortest() :
    if request.method =='GET' :
        #img=read_image_from_s3(s3,'fortest.jpg')
        # file_name = os.getcwd() +'\capture_img.png' 
        # img = Image.open(file_name)
        # img.show()
        #handle_upload_img(s3,'irene')
        img=read_image_from_s4(s4,'capture_image/irene.jpg')

        buffer = BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)
        
        url_generator = str(uuid.uuid4()) 
        handle_upload_img2(s3,buffer,url_generator)

        
        return make_response(jsonify(SUCCESS=True),200)

# 캡쳐  
# /checks
@blue_check.route("/hhi",methods=['GET'])
def CreateCaptureimgfortest() :
    if request.method =='GET' :
        
        img = ImageGrab.grab()
        img.save('hi.jpg')
        file_name = os.getcwd() +'\hi.jpg'
        handle_upload_img(s3,'hi')
        # if os.path.isfile(file_name):
        #     os.remove(file_name) 
        return make_response(jsonify(SUCCESS=True),200)
        
###################################################

#cap_num = 0
# 캡쳐  
# /checks
@blue_check.route("/<int:classIdx>",methods=['POST'])
def CreateCapture(classIdx) :
    if request.method =='POST' :
        #global cap_num
        img = ImageGrab.grab()
        url_generator = str(uuid.uuid4()) 
        img = img.convert("RGB")
        img.save(url_generator+'.jpg') # 로컬에 저장 
        #img.save('capture_Img{}'.format(cap_num)+'.jpg') # 로컬에 저장
        #cap_num +=1 
        
        handle_upload_img(s3,url_generator) # s3에 저장 
        
        x = dt.datetime.now()
        date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
        
        url_generatorList = []
        url_generatorList.append(url_generator)
        isexist = list(CaptureImg.find({"$and":[ {date:{"$exists": True}}, {"classIdx":classIdx}]}))
        if len(isexist)==0 :  # 이미지를 처음 저장 
            CaptureImg.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {date : url_generatorList}
                }
        ) 
            
        else : # 이미지 처음 저장이 아님 
            CaptureImg.update_one({"classIdx" : classIdx}, 
                {   "$push" :
                    {date : url_generator}
                }
            ) 
        
        # #capture_imgList=list(CaptureImg.find({"classIdx" : classIdx},{"_id" : 0, date:1}))
    
        
        #file_name = os.getcwd() +'\capture_img.jpg'
        
        # if os.path.isfile(file_name):
        #     os.remove(file_name) 
        return make_response(jsonify(url=url_generatorList),200)
    
# 캡쳐 이미지 주소 반환 
# /checks/img
@blue_check.route("/img/<int:classIdx>",methods=['GET'])
def GetCapture(classIdx) :
    if request.method =='GET' :
        x = dt.datetime.now()
        date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
        
        capture_imgList=list(CaptureImg.find({"classIdx" : classIdx},{"_id" : 0, date:1}))
        print('capture imglist : ')
        print(capture_imgList)
        result =capture_imgList[0].values()
        print('result 1 : ')
        print(result)
        result=list(result)[0]
        print('result 2 : ')
        print(result)
        
        img_url_list = []
        for name in result : 
            img_url_list.append(s3_get_image_url(s3,name))
    
        return make_response(jsonify(img_url=img_url_list),200)



def extract_capture_img_url(classIdx) : 
    x = dt.datetime.now()
    date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
    capture_imgList = CaptureImg.find({"$and":[ {date:{"$exists": True}}, {"classIdx":classIdx}]},{"_id" : 0, date:1})
    capture_imgList=list(capture_imgList)
    capture_imgList = capture_imgList[0].values()
    capture_imgList = list(capture_imgList)[0]
    return capture_imgList
    
# 출석체크  
# /checks/attendance/<classIdx>
@blue_check.route("/attendance/<int:classIdx>",methods=['POST'])
def CreatesCheck(classIdx) :
    if request.method =='POST' :
        url = extract_capture_img_url(classIdx)
        print("캡처된 이미지는 {}장 입니다.".format(len(url)))
        students = []
        for i in range(len(url)) :  # 캡처한 사진 개수만큼 
            capture_addr = url[i] + '.jpg'
            data = list(Class.find({"classIdx" : classIdx})) # 해당 클래스정보 
            student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
            
            # 학생들의 임베딩값 추출 & 출석확인
            #students =Embedding.Create_Check(student_img_addr, capture_addr) # 출석한 학생의 레이블 
            #print("출석한 학생은 {}명입니다.".format(students))
            
            students.extend(forRetinaFace.reidentification(capture_addr,student_img_addr))
        classStudentList=list(Student.find({"classIdx" : classIdx},{"_id" : 0, "name":1}))
        
        if len(classStudentList) == 0 : 
            print("수업에 등록된 학생이 없습니다.")
            return make_response(jsonify(SUCCESS=False),400)
        else  :
            print("출석한 학생은 {}입니다.".format(students))
            studentList = [] # 학생의 이름만을 추출 
            for i in range(len(classStudentList)) :
                studentList.append((classStudentList[i]['name'].rsplit('.')[0])) # 확장자 제거 
            
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
    
    
# 출석 학생 확인   
# /checks
@blue_check.route("/attendance/<int:classIdx>",methods=['GET'])
def GetCheck(classIdx) :
    if request.method =='GET' :
        attendanceStudentList=list(Attendance.find({"classIdx" : classIdx},{"_id" : 0, "status":0,'classIdx':0}))
        
        return make_response(jsonify(attendanceStudentList),200)
    
    

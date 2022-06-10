from flask import Blueprint, make_response, render_template, request, jsonify, redirect
import pymongo
import os 
from tkinter import filedialog
blue_student=Blueprint("student", __name__, url_prefix="/students")


conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')
# conn = pymongo.MongoClient()
mydb = conn.CHECKMATE
Student =mydb.Student
Class =mydb.Class



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

    
    
# student 추가 
# /students/<classIdx> 
@blue_student.route("/<int:classIdx>",methods=['POST']) # 라우팅경로
def CreateStduent(classIdx) :
    if request.method =='POST' :
        label = []
        Img_students_addr = AddStduentImg() # 학생들의 사진 폴더를 선택 
        evaluation_labels = os.listdir(Img_students_addr) # 사진들의 이름을 추출 
        for evaluation_label in evaluation_labels :  # 확장자 제거 
            label.append(evaluation_label.rsplit('_')[0])
        studentList = []
        studentIdxlist = []
        for i in range(len(label)) :
            
            if label[i] == 'representations' :  # 이미지 controlfile(?)일경우 저장 X 
                continue
            seq = getNextSequenceSTD()
            student= {"studentIdx" : seq,
                    "name": label[i][0], # 이름이 한글자인 경우 
                    "classIdx" : classIdx,
                    "status" : 'active'}
            
            Student.insert_one({
                    "studentIdx" : seq,
                    "name": label[i][0], # 이름이 한글자인 경우 
                    "classIdx" : classIdx,
                    "status" : 'active'}) 
            
            studentList.append(student)
            studentIdxlist.append(seq)
        #  학생들을 입력받을 때 
        
        # class에 학생들의 사진경로를 추가
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                     {"studentImgAddr" : Img_students_addr}
                }
            ) 
         # class에 학생들의 idx 추가 
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                     {"studentList" : studentIdxlist }
                }
            )
        
        return make_response(jsonify(SUCCESS=True,data=studentList),200)
    
    
    
# student 조회 
# /students/<classIdx> 
@blue_student.route("/<int:classIdx>",methods=['GET'])
def GetStduent(classIdx) :
    if request.method =='GET' :
        Students=list(Student.find({"classIdx" : classIdx},{"_id" : 0}))
            
    return jsonify(Students)


# student 제거  
# status를 deleted로 변경 
# /students/<studentIdx> 
@blue_student.route("/<int:studentIdx>",methods=['PATCH'])
def DeleteStduent(studentIdx) :
    if request.method =='PATCH' :
        Student.update_one({"studentIdx" : studentIdx}, 
                {   "$set" :
                    {"status" : 'deleted'}
                }
            ) 
        return make_response(jsonify(SUCCESS=True),200)
from flask import Blueprint, make_response, render_template, request, jsonify, redirect
import pymongo

blue_class=Blueprint("class", __name__, url_prefix="/classes")


conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.39.108.76:27017')
mydb = conn.CHECKMATE
Class =mydb.Class
Attendance =mydb.Attendance
CaptureImg =mydb.CaptureImg


#  auto increment # classIdx을 반환
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


# Class 추가
# /classes
@blue_class.route("/",methods=['POST']) # 라우팅경로
def CreateClass() :
    if request.method =='POST' :
        data = request.get_json() # 입력받은 class 정보 
        seq = getNextSequenceCLA()
        class_info= {"classIdx" : seq, # 저장할 값 
                "className": data['className'],
                "userIdx" : int(data['userIdx']),
                "status" : 'active'}
        Class.insert_one(
            {
                "classIdx" : seq,
                "className": data['className'],
                "userIdx" : int(data['userIdx']),
                "status" : 'active'
            }
        ) 
        Attendance.insert_one(
            {
                "classIdx" : seq,
                "status" : 'active'
            }
        )
        CaptureImg.insert_one(
            {
                "classIdx" : seq,
                "status" : 'active'
            }
        )
        return make_response(jsonify(SUCCESS=True,data=class_info),200)
    
    
# class 조회
# /classes/<userIdx>
@blue_class.route("/<int:userIdx>",methods=['GET'])
def GetClass(userIdx) :
    if request.method =='GET' :
        classes=list(Class.find({"userIdx" : userIdx},{"_id" : 0}))
            
    return jsonify(classes)


# Class 이름변경
# /classes/classname/<classIdx>
@blue_class.route("/classname/<int:classIdx>",methods=['PATCH']) # 라우팅경로
def PatchClassName(classIdx) :
    if request.method =='PATCH' :
        data = request.get_json() # 이름을 변경할 이름을 입력받음 
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"className" : data['className']}
                }
            ) 
        return make_response(jsonify(SUCCESS=True,data = data['className']),200)


# class 제거  
# status를 deleted로 변경 
# /classes/<classIdx>
@blue_class.route("/<int:classIdx>",methods=['PATCH'])
def DeleteClass(classIdx) :
    if request.method =='PATCH' :
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"status" : 'deleted'}
                }
            ) 
        return make_response(jsonify(SUCCESS=True,data = {"status" : 'deleted'}),200)

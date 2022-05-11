from library import arcface_onnx
from library import model_zoo
from library import face_analysis
from library import model_func
import forRetina_arc
import onnxruntime


import os 
import pymongo

conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.39.108.76:27017')
mydb = conn.CHECKMATE



def Create_Check(Img_students_addr,Img_capture_addr) :
    app = forRetina_arc.model_prepare('models')
    # 저장된 학생 사진의 임베딩과 학생사진 
    evaluation_embs, evaluation_labels = forRetina_arc.embs_result(Img_students_addr, app)
    # 캡쳐 이미지와 저장된 학생의 사진과 비교 
    result =forRetina_arc.print_ID_results(evaluation_embs, app,Img_capture_addr,evaluation_labels,verbose=True)
    return result # 출석결과 레이블 반환 


Class =mydb.Class
data = list(Class.find({"classIdx" : 9})) # 해당 클래스정보 
student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
capture_addr = os.getcwd() +'\capture_img.png'
check_result=Create_Check(student_img_addr, capture_addr)
print(check_result)
from deepface import DeepFace
import os 
import re 
import pymongo

conn = pymongo.MongoClient('mongodb://user:checkmate12!@3.39.108.76:27017')
mydb = conn.CHECKMATE
Class =mydb.Class

file_name = os.getcwd() +'\capture_img.jpg'

data = list(Class.find({"classIdx" : 9})) # 해당 클래스정보 
student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
df = DeepFace.find(img_path = file_name, db_path = student_img_addr)

print(df.head())
# person = df['identity'][0]
# person = 'C:/img_for_checkmate/irene.jpg'
# end=person.find('.')
# start = [n for n in range(len(person)) if person.find('/', n) == n]

# print(person[start[-1]+1:end])

result = DeepFace.verify(img1_path = file_name, img2_path = "아이린.jpg")
print(result)
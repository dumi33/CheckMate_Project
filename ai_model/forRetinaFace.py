from retinaface import RetinaFace
import os
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2
from deepface import DeepFace


detectors = ['opencv', 'mtcnn', 'retinaface']
models = ['VGG-Face', 'Facenet', 'Facenet512', 'ArcFace', 'SFace']
metrics = ['cosine', 'euclidean', 'euclidean_l2']



# face detection and crop 
#img_path = os.getcwd() +'\capture_img.jpg'
##faces = RetinaFace.detect_faces(img_path)
# faces = RetinaFace.extract_faces(img_path = img_path, align = True)
# length=len(faces)
# detector = detectors[2]
# addr_path = "C:" + "/" + "img_for_checkmate"
# print("출석한 학생은 {}명입니다.".format(len(faces)))

# for idx,face in enumerate(faces) : 
#     plt.imshow(face)
#     plt.savefig('face{}.jpg'.format(idx))

# for i in range(0,length) : 
#     df = DeepFace.find('face{}.jpg'.format(i), db_path =addr_path) 
# print(df.head())

def reidentification (img_path1,addr_path ) : 
    # face detection and crop 
    #img_path = os.getcwd() +'\capture_img.jpg'
    #faces = RetinaFace.detect_faces(img_path)
    faces = RetinaFace.extract_faces(img_path = img_path1, align = True)
    length=len(faces)
    detector = detectors[2]
    #addr_path = "C:" + "/" + "img_for_checkmate"
    print("캡처이미지에 있는 학생은 {}명입니다.".format(len(faces)))
    attendent_student = []
    for idx,face in enumerate(faces) : 
        plt.imshow(face)
        plt.savefig('face{}.jpg'.format(idx))

    for i in range(0,length) : 
        df = DeepFace.find('face{}.jpg'.format(i), db_path =addr_path) 
        full_name=df['identity'][0] # 가장 닮은 인물만 넣는다.
        end=full_name.find('.')
        start = [n for n in range(len(full_name)) if full_name.find('/', n) == n]
        attendent_student.append(full_name[start[-1]+1:end])
        
        
        # 아래 코드는 여러명이 제안 되었을 때 모두 반환함 
        # for i in range(len(df['identity'])) : 
        #     full_name=df['identity'][i]
        #     end=full_name.find('.')
        #     start = [n for n in range(len(full_name)) if full_name.find('/', n) == n]
        #     attendent_student.append(full_name[start[-1]+1:end])
    return attendent_student


    
#for face in faces : 
    # addr_path = "C:" + "/" + "img_for_checkmate"
    # img1 = cv2.imread(face) 
    # df = DeepFace.find(img1, db_path =addr_path) 
    # print(df.head())

# bboxlist = []
# for i in range(1,len(faces)+1) : 
#     bboxlist.append(faces['face_{}'.format(i)]['facial_area']) # 각 얼굴별 랜드마크, bbox를 출력
# print(bboxlist)

# kpslist = []
# for i in range(1,len(faces)+1) : 
#     tmp = []
#     tmp.append(faces['face_{}'.format(i)]['landmarks']['right_eye']) # 각 얼굴별 랜드마크, bbox를 출력
#     tmp.append(faces['face_{}'.format(i)]['landmarks']['left_eye']) 
#     tmp.append(faces['face_{}'.format(i)]['landmarks']['nose'])
#     tmp.append(faces['face_{}'.format(i)]['landmarks']['mouth_right'])
#     tmp.append(faces['face_{}'.format(i)]['landmarks']['mouth_left'])
#     kpslist.append(tmp)
# print(kpslist)

# faces = RetinaFace.extract_faces(img_path = img_path, align = True)
# for face in faces:
#   plt.imshow(face)
#   plt.show()
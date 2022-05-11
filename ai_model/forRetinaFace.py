from retinaface import RetinaFace
import os
import matplotlib.pyplot as plt

img_path = os.getcwd() +'\capture_img.png'

faces = RetinaFace.detect_faces(img_path)
print("출석한 학생은 {}명입니다.".format(len(faces)))

bboxlist = []
for i in range(1,len(faces)+1) : 
    bboxlist.append(faces['face_{}'.format(i)]['facial_area']) # 각 얼굴별 랜드마크, bbox를 출력
print(bboxlist)

kpslist = []
for i in range(1,len(faces)+1) : 
    tmp = []
    tmp.append(faces['face_{}'.format(i)]['landmarks']['right_eye']) # 각 얼굴별 랜드마크, bbox를 출력
    tmp.append(faces['face_{}'.format(i)]['landmarks']['left_eye']) 
    tmp.append(faces['face_{}'.format(i)]['landmarks']['nose'])
    tmp.append(faces['face_{}'.format(i)]['landmarks']['mouth_right'])
    tmp.append(faces['face_{}'.format(i)]['landmarks']['mouth_left'])
    kpslist.append(tmp)
print(kpslist)

# faces = RetinaFace.extract_faces(img_path = img_path, align = True)
# for face in faces:
#   plt.imshow(face)
#   plt.show()
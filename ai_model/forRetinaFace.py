from retinaface import RetinaFace
import os
import matplotlib.pyplot as plt

img_path = os.getcwd() +'\capture_img.png'

faces = RetinaFace.detect_faces(img_path)
print("출석한 학생은 {}명입니다.".format(len(faces)))
print(faces) # 각 얼굴별 랜드마크, bbox를 출력 
# faces = RetinaFace.extract_faces(img_path = img_path, align = True)
# for face in faces:
#   plt.imshow(face)
#   plt.show()
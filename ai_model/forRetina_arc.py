from sklearn.neighbors import NearestNeighbors
import numpy as np
from PIL import Image
from library.face_analysis import *
import cv2
import os
from typing import List
from tqdm import tqdm
import sys 


def filter_empty_embs(img_set: List, img_labels: List[str]):
    # filtering where insightface could not generate an embedding
    good_idx = [i for i,x in enumerate(img_set) if x]
    
    if len(good_idx) == len(img_set):
        clean_embs = [e[0].embedding for e in img_set]
        clean_labels = img_labels
        
    else:
        # filtering eval set and labels based on good idx
        clean_labels = np.array(img_labels)[good_idx]
        clean_set = np.array(img_set, dtype=object)[good_idx]
        
        # generating embs for good idx
        clean_embs = [e[0].embedding for e in clean_set]
    
    return clean_embs, clean_labels


# 저장된 학생 사진의 임베딩값과 레이블 추출 
def embs_result(dir_path : str,  app : FaceAnalysis):
    files = os.listdir(dir_path)[0:] # 이미지 파일 리스트
    files.sort()

    eval_set = list()
    eval_labels = list()
    IMAGES_PER_IDENTITY = 11
    
    # 이미지 파일 내에서 각각의 이미지에 대하여 추출
    for i in tqdm(range(1, len(files), IMAGES_PER_IDENTITY), unit_divisor=True):
        # store eval embs and labels
        # eval_set_t, eval_labels_t = generate_embs(app,img_path)
        
        eval_set_t = list()
        eval_labels_t = list()
        
        # 각각의 이미지에 대한 임베딩값 추출
        for img_fpath in files:
                    
            # read grayscale img
            img = Image.open(os.path.join(dir_path, img_fpath)) 
            img_arr = np.asarray(img)  
            
            # convert grayscale to rgb
            im = Image.fromarray((img_arr * 255).astype(np.uint8))
            rgb_arr = np.asarray(im.convert('RGB'))       
        
            # generate Insightface embedding
            res = app.get(rgb_arr)          
            # append emb to the eval set
            eval_set_t.append(res)          
            # append label to eval_label set
            eval_labels_t.append(img_fpath.split("_")[0])  
        
        eval_set.extend(eval_set_t)
        eval_labels.extend(eval_labels_t)
    
    evaluation_embs, evaluation_labels = filter_empty_embs(eval_set, eval_labels)
    return evaluation_embs, evaluation_labels
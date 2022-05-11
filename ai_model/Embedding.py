from ai_model.library import arcface_onnx
from ai_model.library import model_zoo
from ai_model.library import face_analysis
from ai_model.library import model_func
import onnxruntime

def Create_Check(Img_students_addr,Img_capture_addr) :
    app = model_func.model_prepare('models')
    # 저장된 학생 사진의 임베딩과 학생사진 
    evaluation_embs, evaluation_labels = model_func.embs_result(Img_students_addr, app)
    # 캡쳐 이미지와 저장된 학생의 사진과 비교 
    result = model_func.print_ID_results(evaluation_embs, app,Img_capture_addr,evaluation_labels,verbose=True)
    return result # 출석결과 레이블 반환 
    

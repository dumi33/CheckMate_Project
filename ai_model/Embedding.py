from ai_model.library import arcface_onnx
from ai_model.library import model_zoo
from ai_model.library import face_analysis
from ai_model.library import model_func
import onnxruntime
        
def Create_Check(Img_students_addr,Img_capture_addr) :
    app = model_func.model_prepare('models')
    evaluation_embs, evaluation_labels = model_func.embs_result(Img_students_addr, app)
    result = model_func.print_ID_results(Img_capture_addr, app)
    return result
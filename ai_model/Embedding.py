from ai_model.library import arcface_onnx
from ai_model.library import model_zoo
from ai_model.library import face_analysis
from ai_model.library import model_func
import onnxruntime
        
def Create_Embedding(Img_students_addr) :
    app = model_func.model_prepare('models')
    evaluation_embs, evaluation_labels = model_func.embs_result(Img_students_addr, app)
    return evaluation_embs, evaluation_labels 

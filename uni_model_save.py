import tensorflow as tf
from tensorflow.keras.models import load_model

def load_saved_model():
    # 저장된 모델 로드
    loaded_model = load_model('my_model.h5')
    return loaded_model

loaded_model = load_saved_model()
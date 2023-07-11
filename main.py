from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class InputData(BaseModel):
    gre: float
    gpa: float
    rank: float

app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
	return item

from uni_model_save import loaded_model
import numpy as np

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[data.gre, data.gpa, data.rank]])
    
    # 모델을 사용하여 예측
    prediction = loaded_model.predict(input_array)
    # 이진 분류라서 예측 확률 0 또는 1로 변환
    result = 1 if prediction[0][0] >= 0.5 else 0
    
    return {"prediction": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
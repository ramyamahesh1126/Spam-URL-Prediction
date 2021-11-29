import uvicorn
import pickle
import sklearn
from fastapi import FastAPI
from feature import feature_extraction

with open('model1.pickle','rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Detecting Spam URL'}

@app.get('/predict/')
def predict(url: str):
    df=feature_extraction(url)
    return {'output': model.predict(df).tolist()}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)

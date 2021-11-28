import uvicorn
import pickle
import sklearn
from fastapi import FastAPI
from feature import url_length
from feature import at_present
from feature import dash_present
from feature import redirect_present
from feature import check_domain_length
from feature import no_of_subdomains

with open('model.pickle','rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Detecting Spam URL'}

@app.get('/predict/{url}')
def predict(url: str):
    feature_1=url_length(url)
    feature_2=at_present(url)
    feature_3=dash_present(url)
    feature_4=redirect_present(url)
    feature_5=check_domain_length(url)
    feature_6=no_of_subdomains(url)
    return {'output': model.predict([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6]]).tolist()}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)

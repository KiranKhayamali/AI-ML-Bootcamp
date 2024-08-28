from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib

#Inintialize FastAPI app 
app = FastAPI()

#Load the trained model 
model = joblib.load('iris_logistics_regression.pkl')

#Define request model
class Features(BaseModel):
    features : conlist(float, min_length=4, max_length=4) #Ensure the feature list has exactly 4 float values

#Define a route for the prediction API
@app.post('/predict')
def predict(data : Features):
    try :
        #Predict using the model 
        prediction = model.predict([data.features])
        return {'prediction' : int(prediction[0])}
    except Exception as e:
        #Handle eroor during prediction
        raise HTTPException(status_code=500, detail=str(e))
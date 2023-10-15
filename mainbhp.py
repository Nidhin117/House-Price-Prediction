from fastapi import FastAPI,Request, status
from typing import Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import utils
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
utils.load_saved_artifacts()

#This function will return an exception to the client in case of errors with the Request being passed to POST APIs
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

#Following code block is to enable CORS when making API requests from
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/') 
def index():   
    return {'data':"Bangalore Price predictor"}

@app.get('/about')
def about():    
    return {'data':{'ML model that can predict House prices'}}

@app.get('/location_names')
def get_locn_names():
    response = {
        'locations' : utils.get_location_names()
    }
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=response, status_code=200,headers=headers) 

class HouseParameters(BaseModel):
    location : str
    sqft : int
    bath: int
    balcony :int
    bhk :int

@app.post('/estimate_houseprice')
def est_blrhouseprice(request:HouseParameters):
    price = utils.get_estimated_price(request.location,request.sqft,request.bhk,request.balcony,request.bath)
    print(price)
    response = { 'estimated_price' : price }
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=response, status_code=201,headers=headers)


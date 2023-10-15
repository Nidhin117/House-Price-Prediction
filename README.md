# HousePricePrediction
A static website that predicts house prices based on the locality, area, number of rooms, baths and balcony. The predictions are  made by a machine learning model that has been hyper paramter tuned.
The website uses FastAPI to interact with the server where the machine learning model resides.
Some aspects such as hyperparameter tuning used during training of the model was inspired by CodeBasics(YouTube channel) tutorial and the Jupyter notebook related to model training is - bengaluru-house-price.ipynb file.
However, the backend server code and front end UI code is completely original and the python file mainbhp.py is the main file where the code for FastAPI resides.
The JS file app.js has Jquery code to make API calls to the backend server and render the results on the screen.

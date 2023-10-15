# HousePricePrediction
Machine Learning model used as back end for a static website that allows estimation of property prices in Bangalore. The website uses FastAPI to interact with the server where the machine learning model resides.
Some aspects such as hyperparameter tuning in training of the model was inspired by CodeBasics tutorial and the Jupyter notebook related to model training is - bengaluru-house-price.ipynb file.
However, the backend server code and front end UI code is completely original and the python file mainbhp.py is the main file where the code for FastAPI resides.
The JS file app.js has Jquery code to make API calls to the backend server and render the results on the screen.

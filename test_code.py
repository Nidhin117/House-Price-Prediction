#from flask import Flask, request, jsonify
import utils

utils.load_saved_artifacts()
print("Locations are as follows")
print(utils.get_location_names())
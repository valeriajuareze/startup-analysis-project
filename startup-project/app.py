import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


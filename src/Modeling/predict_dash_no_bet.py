from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import pickle
from dash import Dash, dash_table, html, dcc, Input, Output
import time

random_forest_model = pickle.load(open('src/Modeling/Random_forest_model_no_bet.sav', 'rb'))


import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

df = pd.read_csv('amazon_reviews_us_Gift_Card_v1_00.tsv', delimiter='\t')
frequency = df['star_rating'].value_counts().sort_index()
frequency.plot(color=['purple'], kind ='bar', xlabel = 'Stars', ylabel = 'Frequency')
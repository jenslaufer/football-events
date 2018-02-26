import numpy as np
import pandas as pd

print('loading data sets...')

events = pd.read_csv('../data/events.csv')

events = events.merge(pd.read_csv('../data/ginf.csv'), how='inner')

print('loading data sets succeeded.')

events_cont = pd.get_dummies(events)

print(events.head())





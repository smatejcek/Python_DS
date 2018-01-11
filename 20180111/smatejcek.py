import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.plotting import scatter_matrix
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from itertools import combinations
import csv

df = pd.read_csv("Advertising.csv", index_col = 0)

with open()

dependent = "sales"

columns = [c for c in list(df) if c != dependent]
results = []
for i in range(1, len(columns) + 1):
    combos = list(combinations(columns, i))
    for c in combos:
        y = df[dependent]
        X = pd.DataFrame(df, columns = c) #Alternative assignment method
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
        for j in range(2):
#            model = linear_model.LinearRegression(fit_intercept = j == 1).fit(X_train, y_train)
            model = linear_model.LinearRegression(fit_intercept = j).fit(X_train, y_train)
            score = model.score(X_test, y_test)
#            results.append([score, "Intercept: {}".format(j == 1), c, "Coef: {}".format(model.coef_), "Int: {}".format(model.intercept_)])
            results.append([score, "Intercept: {}".format(j), c, "Coef: {}".format(model.coef_), "Int: {}".format(model.intercept_)])

print (max(results))

# [0.85934788575176313, 'Intercept: True', ('TV', 'radio'), 'Coef: [ 0.04473962  0.19935546]', 'Int: 2.8673545339377267']

#y = 2.8674 + .0447TV + .1993Radio

#y = 2.8674 + .0477(199) + .1993(32) = 18.1403

dependent = "horsepower"

temp = []
with open("auto-mpg.data.txt") as file:
    reader = csv.reader(file)
    for line in reader:
        temp.append(line).split("\y")

df = pd.DataFrame(temp)


columns = [c for c in list(df) if c != dependent and c!= "car name"]
results = []
for i in range(1, len(columns) + 1):
    combos = list(combinations(columns, i))
    for c in combos:
        y = df[dependent]
        X = pd.DataFrame(df, columns = c) #Alternative assignment method
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
        for j in range(2):
#            model = linear_model.LinearRegression(fit_intercept = j == 1).fit(X_train, y_train)
            model = linear_model.LinearRegression(fit_intercept = j).fit(X_train, y_train)
            score = model.score(X_test, y_test)
            results.append([score, "Intercept: {}".format(j == 1), c, "Coef: {}".format(model.coef_), "Int: {}".format(model.intercept_)])

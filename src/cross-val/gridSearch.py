import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import scale
from warnings import filterwarnings
filterwarnings("ignore")

# Cross Validation Function for Random Forest
def RandomForest(x_df, y_df, cv, n):
    model = RandomForestClassifier(random_state=100, verbose=True)
    params = {"n_estimators": [400, 1000],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}
    grid_search = GridSearchCV(model, param_grid=params, cv=cv, n_jobs=n)
    grid_fit = grid_search.fit(x_df, y_df)
    print(grid_fit.cv_results_)
    print(f"Best Cross-Validated Accuracy: {round(grid_fit.best_score_*100,2)}%")
    print(f"Best Model Parameters: {grid_fit.best_params_}")
    return grid_fit

# Cross Validation Function for Logistic Regression Non-SGD
def noSGDLogisticRegression(x_df, y_df, cv, n):
    model = LogisticRegression(random_state=100, verbose=True)
    params = {"penalty": ['l1', 'l2']}
    grid_search = GridSearchCV(model, param_grid=params, cv=cv, n_jobs=n)
    grid_fit = grid_search.fit(x_df, y_df)
    print(grid_fit.cv_results_)
    print(f"Best Cross-Validated Accuracy: {round(grid_fit.best_score_*100,2)}%")
    print(f"Best Model Parameters: {grid_fit.best_params_}")
    return grid_fit

# Cross Validation Function for Logistic Regression SGD

def SGDLogisticRegression(x_df, y_df, cv, n):
    model = SGDClassifier(loss='log', random_state=100, verbose=True)
    params = {"penalty": ['l1', 'l2', 'elasticnet'],
              "l1_ratio": [0.15, 0.25],
              "shuffle": [True, False],
              "learning_rate": ['constant', 'adaptive']
              }
    grid_search = GridSearchCV(model, param_grid=params, cv=cv, n_jobs=n)
    grid_fit = grid_search.fit(x_df, y_df)
    print(grid_fit.cv_results_)
    print(f"Best Cross-Validated Accuracy: {round(grid_fit.best_score_*100,2)}%")
    print(f"Best Model Parameters: {grid_fit.best_params_}")
    return grid_fit

# Cross Validation Function for Neural Network

def NeuralNetwork(x_df, y_df, cv, n):
    model = MLPClassifier(random_state=100, verbose=True)
    params = {"hidden_layer_sizes": [(100,), (200,), (300,)],
              "activation": ['logistic', 'relu'],
              "solver": ['sgd', 'adam'],
              "alpha": [1e-4, 1e-12],
              "learning_rate": ['constant', 'adaptive'],
              "shuffle": [True, False]
              }
    grid_search = GridSearchCV(model, param_grid=params, cv=cv, n_jobs=n)
    grid_fit = grid_search.fit(x_df, y_df)
    print(grid_fit.cv_results_)
    print(f"Best Cross-Validated Accuracy: {round(grid_fit.best_score_*100,2)}%")
    print(f"Best Model Parameters: {grid_fit.best_params_}")
    return grid_fit

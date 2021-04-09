#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:30:10 2021

@author: Jesimar da Silva Arantes
@email: jesimar.arantes@gmail.com

Código para fazer a desenvolver o modelo de Aprendizado de Máquina.

"""

import warnings

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier

def classifcador_rna_simples():
    X = [[0., 0.], [1., 1.]]
    y = [0, 1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1)
    print(clf.fit(X, y))
    new_instance = [[2., 2.], [-1., -2.]]
    print(clf.predict([new_instance[0]]))
    print([coef.shape for coef in clf.coefs_])

#Exemplo retirado de: https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html#sphx-glr-auto-examples-neural-networks-plot-mnist-filters-py
def example_mnist():
    # Load data from https://www.openml.org/d/554
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    X = X / 255.
    
    # rescale the data, use the traditional train/test split
    X_train, X_test = X[:60000], X[60000:]
    y_train, y_test = y[:60000], y[60000:]
    
    #print(X_train)
    #print(y_train)
    #print(X_test)
    #print(y_test)
    #print(len(X_train))
    #print(len(X_train[0]))
    
    mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                        solver='sgd', verbose=10, random_state=1,
                        learning_rate_init=.1)
    
    # this example won't converge because of CI's time constraints, so we catch the
    # warning and are ignore it here
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=ConvergenceWarning,
                                module="sklearn")
        mlp.fit(X_train, y_train)
    
    print("Training set score: %f" % mlp.score(X_train, y_train))
    print("Test set score: %f" % mlp.score(X_test, y_test))
    print([coef for coef in mlp.coefs_])

    fig, axes = plt.subplots(4, 4)
    # use global min / max to ensure all weights are shown on the same scale
    vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
    for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
        ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
                   vmax=.5 * vmax)
        ax.set_xticks(())
        ax.set_yticks(())
    plt.show()

def mlp_problema_linhas_tensao():
    if os.getcwd().endswith('/src'):
        os.chdir('..')
    df = pd.read_csv(os.path.join('models', 'model-features2.csv'), sep=';')
    size_train = 90
    size_test = 30
    size_validation = 167 - size_train - size_test
    vx = []
    vy = []
    for i in range(size_train + size_test):
        instance = df.values[i][1:-1]
        target = df.values[i][len(df.values[0])-1]
        vx.append(instance)
        vy.append(target)
    X = pd.DataFrame(vx)
    y = pd.DataFrame(vy)
    #print(X)
    #print(y)
    X_train, X_test = X[:size_train], X[size_train:]
    y_train, y_test = y[:size_train], y[size_train:]
    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.transpose().values[0]
    y_test = y_test.transpose().values[0]
    
    #print(X_train)
    #print(y_train)
    #print(X_test)
    #print(y_test)
    
    #print('treinamento')
    #print(len(X_train))
    #print(len(X_train[0]))
    
    #print('teste')
    #print(len(X_test))
    #print(len(X_test[0]))
    
    mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=100, alpha=1e-5,
                        solver='sgd', verbose=10, random_state=1,
                        learning_rate_init=.01)
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=ConvergenceWarning,
                                module="sklearn")
        mlp.fit(X_train, y_train)
    
    print("Training set score: %f" % mlp.score(X_train, y_train))
    print("Test set score: %f" % mlp.score(X_test, y_test))
    #print([coef for coef in mlp.coefs_])
    
    nvx = []
    nvy = []
    for i in range(size_train + size_test, 167):
        instance = df.values[i][1:-1]
        target = df.values[i][len(df.values[0])-1]
        nvx.append(instance)
        nvy.append(target)
    X_validation = pd.DataFrame(nvx)
    y_validation = pd.DataFrame(nvy)
    #print(X_validation)
    #print(y_validation)
    X_validation = X_validation.to_numpy()
    y_validation = y_validation.transpose().values[0]
    count_acertos = 0
    count_erros = 0
    for i in range(size_validation):
        #print(X_validation[i])
        #print(y_validation[i])
        vpredito = mlp.predict([X_validation[i]])
        if y_validation[i] == vpredito[0]:
            count_acertos += 1
        else:
            count_erros += 1
            print('instance-{}.csv'.format(i+size_train+size_test+1))
            print('     errou')
        #print()
    print('quantidade de acertos: {}'.format(count_acertos))
    print('quantidade de erros: {}'.format(count_erros))
    #mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2))
        
    
# ============= Experimentos do Modelo de Aprendizado de Máquina =============

#classifcador_rna_simples()
#example_mnist()

mlp_problema_linhas_tensao()


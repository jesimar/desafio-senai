#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:30:10 2021

@author: Jesimar da Silva Arantes
@email: jesimar.arantes@gmail.com

Código do modelo de Aprendizado de Máquina Multi-Layer Perceptron (MLP).

"""

import os
import random
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

def mlp_for_voltage_lines_problem(file_model):
    if os.getcwd().endswith('/src'):
        os.chdir('..')
    
    df = pd.read_csv(file_model, sep=';')
    size_train = 100
    size_test = 67
    vx = []
    vy = []
    for i in range(size_train + size_test):
        instance = df.values[i][1:-1]
        target = df.values[i][len(df.values[0])-1]
        vx.append(instance)
        vy.append(target)
    X = pd.DataFrame(vx)
    
    #normalização da base das instâncias de entrada
    X = (X - X.min()) / (X.max() - X.min())
    y = pd.DataFrame(vy)
    
    X_train, X_test = X[:size_train], X[size_train:]
    y_train, y_test = y[:size_train], y[size_train:]
    
    #balanceamento da base de dados
    list_anormal = [1, 67, 76, 90, 93, 95, 98]
    for i in range(86): #100 = 93 normal    e 7 anormal    -> 186 dados de treinamento
        index = list_anormal[i % len(list_anormal)]
        df2 = pd.DataFrame(X_train.values[index]).transpose()
        dfy2 = pd.DataFrame(y_train.values[index]).transpose()
        X_train = X_train.append(df2)
        y_train = y_train.append(dfy2)
    
    #reordenação da base de treinamento para que fiquem aleatorios as instâncias normais e anormais
    for i in range(186):
        index1 = random.randint(0, 185)
        index2 = random.randint(0, 185)
        ndf1, ndf2 = X_train.iloc[index1], X_train.iloc[index2]
        X_train.iloc[index1], X_train.iloc[index2] = ndf2, ndf1        
        ndfy1, ndfy2 = y_train.iloc[index1], y_train.iloc[index2]
        y_train.iloc[index1], y_train.iloc[index2] = ndfy2, ndfy1
    
    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.transpose().values[0]
    y_test = y_test.transpose().values[0]    
    
    
    mlp = MLPClassifier(hidden_layer_sizes=(5, ), max_iter=1000, alpha=1e-3,
                        solver='sgd', verbose=1, random_state=1, learning_rate_init=0.1)
    
    mlp.fit(X_train, y_train)
    score_train = mlp.score(X_train, y_train)
    score_test = mlp.score(X_test, y_test)
    print('Acurácia no treinamento (score): {}'.format(score_train))
    print('Acurácia no teste (score): {}'.format(score_test))
    
    size_train = 186
    list_anormal_test = [136, 144, 145, 152]
    count_hits = 0
    count_errors = 0
    y_pred = []
    vp = 0
    fp = 0
    vn = 0
    fn = 0
    for i in range(size_test):
        vpredito = mlp.predict([X_test[i]])
        y_pred.append(vpredito[0])
        if y_test[i] == vpredito[0]:
            count_hits += 1
            if y_test[i] == 1:
                vp += 1
                #print('instance-{}.csv -> acertou defeito'.format(100 + i + 1))
            else:
                vn += 1
                #print('instance-{}.csv -> acertou normalidade'.format(100 + i + 1))
        else:
            count_errors += 1
            if y_test[i] == 1:
                fn += 1
                #print('instance-{}.csv -> errou defeito'.format(100 + i + 1))
            else:
                fp += 1
                #print('instance-{}.csv -> errou normalidade'.format(100 + i + 1))
    print('VP: {}'.format(vp))
    print('VN: {}'.format(vn))
    print('FP: {}'.format(fp))
    print('FN: {}'.format(fn))
    print('Quantidade total de acertos: {}'.format(count_hits))
    print('quantidade total de erros: {}'.format(count_errors))
    
# ============= Experimentos do Modelo de Aprendizado de Máquina =============

mlp_for_voltage_lines_problem(os.path.join('models', 'model-features.csv'))

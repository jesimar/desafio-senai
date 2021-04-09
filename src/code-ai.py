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
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

def mlp_for_voltage_lines_problem(file_model, debug=False):
    if os.getcwd().endswith('/src'):
        os.chdir('..')
    
    #leitura do arquivo com as features das instâncias
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
    y = pd.DataFrame(vy)
    
    #normalização da base das instâncias de entrada
    X = (X - X.min()) / (X.max() - X.min())
    
    #separação das instâncias em conjunto de treinamento e teste
    X_train, X_test = X[:size_train], X[size_train:]
    y_train, y_test = y[:size_train], y[size_train:]
    
    #balanceamento da base de dados
    #Existem 100 instâncias para treinamento onde 93 normal e 7 anormal
    #O objetivo aqui é ter 186 instâncias para treinamento onde 93 são normais e 93 são anormais
    #A extratégia para isso foi a replicação dos dados anormais na base de dados.
    list_anormal_train = [1, 67, 76, 90, 93, 95, 98]
    size_data_duplicated = 86
    for i in range(size_data_duplicated):
        index = list_anormal_train[i % len(list_anormal_train)]
        new_dfx = pd.DataFrame(X_train.values[index]).transpose()
        new_dfy = pd.DataFrame(y_train.values[index]).transpose()
        X_train = X_train.append(new_dfx)
        y_train = y_train.append(new_dfy)
    
    #reordenação da base de treinamento para que fiquem aleatorios as instâncias normais e anormais
    for i in range(size_train + size_data_duplicated):
        index1 = random.randint(0, size_train + size_data_duplicated - 1)
        index2 = random.randint(0, size_train + size_data_duplicated - 1)
        newdf_x1, newdf_x2 = X_train.iloc[index1], X_train.iloc[index2]
        X_train.iloc[index1], X_train.iloc[index2] = newdf_x2, newdf_x1
        newdf_y1, newdf_y2 = y_train.iloc[index1], y_train.iloc[index2]
        y_train.iloc[index1], y_train.iloc[index2] = newdf_y2, newdf_y1
    
    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.transpose().values[0]
    y_test = y_test.transpose().values[0]    
    
    #criação da rede MLP
    mlp = MLPClassifier(hidden_layer_sizes=(5, ), max_iter=1000, alpha=1e-3,
                        solver='sgd', verbose=0, random_state=1, learning_rate_init=0.1)
    #verbose=1
    mlp.fit(X_train, y_train)
    
    # analisa o modelo treinado
    count_hits = 0
    count_errors = 0
    vp = 0
    fp = 0
    vn = 0
    fn = 0
    #list_anormal_test = [136, 144, 145, 152]
    for i in range(size_test):
        vpredicted = mlp.predict([X_test[i]])
        if y_test[i] == vpredicted[0]:
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
    score_train = mlp.score(X_train, y_train)
    score_test = mlp.score(X_test, y_test)
    if debug:
        print('Acurácia no treinamento (score): {}'.format(score_train))
        print('Acurácia no teste (score): {}'.format(score_test))
        print('Quantidade total de acertos: {}'.format(count_hits))
        print('quantidade total de erros: {}'.format(count_errors))
        print('VP: {}'.format(vp))
        print('VN: {}'.format(vn))
        print('FP: {}'.format(fp))
        print('FN: {}'.format(fn))
    else:
        print('{};{};{};{};{};{};{};{}'.format(score_train, score_test, 
                                               count_hits, count_errors, 
                                               vp, vn, fp, fn))
    
def experiment_simple():
    print('{};{};{};{};{};{};{};{}'.format('score_train', 'score_test', 
                                           'count_hits', 'count_errors', 
                                           'vp', 'vn', 'fp', 'fn'))
    mlp_for_voltage_lines_problem(os.path.join('models', 'model-features.csv'))
    
def experiment_validation1():
    print('{};{};{};{};{};{};{};{}'.format('score_train', 'score_test', 
                                           'count_hits', 'count_errors', 
                                           'vp', 'vn', 'fp', 'fn'))
    for i in range(100):
        mlp_for_voltage_lines_problem(os.path.join('models', 'model-features.csv'))

def experiment_validation2():
    print('{};{};{};{};{};{};{};{}'.format('score_train', 'score_test', 
                                           'count_hits', 'count_errors', 
                                           'vp', 'vn', 'fp', 'fn'))
    for i in range(100):
        mlp_for_voltage_lines_problem(os.path.join('models', 'model-features-simples.csv'))

# ============= Experimentos do Modelo de Aprendizado de Máquina =============

experiment_simple()
#experiment_validation1()
#experiment_validation2()
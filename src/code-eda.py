#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:57:20 2021

@author: Jesimar da Silva Arantes
@email: jesimar.arantes@gmail.com

Código para fazer a Análise Explatória dos Dados (EDA) para conhecer melhor o problema.

"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kurtosis
from scipy.stats import skew

def get_class_instance(filename):
    df = pd.read_csv(os.path.join('..', 'data', 'instances', filename))
    class_instance = df.iloc[0][800002]
    return class_instance

def experiment_analyze_problem_classes():
    classes = []
    for i in range(1, 168):
        vclass = get_class_instance('instance-{}.csv'.format(i))
        classes.append(vclass)
        print('instance = {} -> class = {}'.format(i, vclass))
    print(classes)

def simplification_of_instances(filename, n_line_init=10000):
    #cria arquivos com cerca de 160 KB facilitando a manipulação
    df = pd.read_csv(os.path.join('..', 'data', 'instances', filename), header=None)
    df_save = pd.DataFrame()
    for i in range(0, 3):
        df_init = df.iloc[i][:n_line_init]
        df_final = df.iloc[i][800001:800003] #foi removido também o signal_id (800000), pois ele não faz sentido no problema
        df_simple = df_init.append(df_final)
        df_save = df_save.append(df_simple)
    df_save.to_csv(os.path.join('..', 'data', 'instances-simplificadas', filename), 
                   index=False, header=False, index_label=False)

def experiment_simplification_of_instances():
    # instâncias sem problemas
    simplification_of_instances('instance-1.csv')
    simplification_of_instances('instance-3.csv')
    simplification_of_instances('instance-4.csv')
    simplification_of_instances('instance-5.csv')
    simplification_of_instances('instance-6.csv')
    
    # instâncias com problemas
    simplification_of_instances('instance-2.csv')
    simplification_of_instances('instance-68.csv')
    simplification_of_instances('instance-77.csv')
    simplification_of_instances('instance-91.csv')
    simplification_of_instances('instance-94.csv')

def simplification_of_instances_moving_average(filename, size_ma=1000):
    df = pd.read_csv(os.path.join('..', 'data', 'instances', filename), header=None)
    df_avg = [[0], [0], [0]]
    for i in range(0, 3):
        df_avg[i] = df.iloc[i].rolling(window=size_ma).mean().values[size_ma::size_ma]
    df_save = pd.DataFrame(df_avg)
    df_save.to_csv(os.path.join('..', 'data', 'instances-moving-average-{}'.format(size_ma), filename), 
                   index=False, header=False, index_label=False)

def experiment_simplification_of_instances_moving_average():
    #cria arquivos com aproximadamente 17 KB facilitando a manipulação.
    # instâncias sem problemas
    simplification_of_instances_moving_average('instance-1.csv')
    simplification_of_instances_moving_average('instance-3.csv')
    simplification_of_instances_moving_average('instance-4.csv')
    simplification_of_instances_moving_average('instance-5.csv')
    simplification_of_instances_moving_average('instance-6.csv')
    
    # instâncias com problemas
    simplification_of_instances_moving_average('instance-2.csv')
    simplification_of_instances_moving_average('instance-68.csv')
    simplification_of_instances_moving_average('instance-77.csv')
    simplification_of_instances_moving_average('instance-91.csv')
    simplification_of_instances_moving_average('instance-94.csv')

def creating_image_by_timeseries(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    red   = df.values[0][:-2]
    green = df.values[1][:-2]
    blue  = df.values[2][:-2]
    max_r = 40  #300  #max(red)
    min_r = -40 #-150 #min(red)
    max_g = 40  #300  #max(green)
    min_g = -40 #-150 #min(green)
    max_b = 40  #300  #max(blue)
    min_b = -40 #-150 #min(blue)
    red   = 255 * (red - min_r)/(max_r - min_r)
    green = 255 * (green - min_g)/(max_g - min_g)
    blue  = 255 * (blue - min_b)/(max_b - min_b)
    dimx = 894
    dimy = 894
    pixels = np.zeros((dimx, dimx, 3), dtype=np.uint8)
    v = 0
    for i in range(dimx):
        for j in range(dimy):
            red[v] = max(min(red[v], 255), 0)
            green[v] = max(min(green[v], 255), 0)
            blue[v] = max(min(blue[v], 255), 0)
            if red[v] == 255 or green[v] == 255 or blue[v] == 255:
                pixels[i][j] = [255, 255, 255]
                #pixels[i][j] = [0, 0, 0]
            elif red[v] == 0 or green[v] == 0 or blue[v] == 0:
                pixels[i][j] = [255, 255, 255]
                #pixels[i][j] = [0, 0, 0]
            else:
                pixels[i][j] = [red[v], green[v], blue[v]]
            v += 1
            if v > 800000: 
                break
        if v > 800000: 
            break
    # Converte os pixels em um array usando numpy
    array = np.array(pixels, dtype=np.uint8)
    # Use PIL para criar uma imagem do novo array de pixel
    new_image = Image.fromarray(array)
    new_image.save('image-{}.png'.format(filename.replace('.csv', '')))

def experiment_create_images_by_timeseries():
    path = os.path.join('..', 'data', 'instances')
    # instâncias sem problemas
    creating_image_by_timeseries(path, 'instance-1.csv')
    creating_image_by_timeseries(path, 'instance-3.csv')
    creating_image_by_timeseries(path, 'instance-4.csv')
    creating_image_by_timeseries(path, 'instance-5.csv')
    creating_image_by_timeseries(path, 'instance-6.csv')
    creating_image_by_timeseries(path, 'instance-7.csv')
    creating_image_by_timeseries(path, 'instance-8.csv')
    creating_image_by_timeseries(path, 'instance-9.csv')
    creating_image_by_timeseries(path, 'instance-10.csv')
    creating_image_by_timeseries(path, 'instance-11.csv')
    creating_image_by_timeseries(path, 'instance-12.csv')
    
    # instâncias com problemas
    creating_image_by_timeseries(path, 'instance-2.csv')
    creating_image_by_timeseries(path, 'instance-68.csv')
    creating_image_by_timeseries(path, 'instance-77.csv')
    creating_image_by_timeseries(path, 'instance-91.csv')
    creating_image_by_timeseries(path, 'instance-94.csv')
    creating_image_by_timeseries(path, 'instance-96.csv')
    creating_image_by_timeseries(path, 'instance-99.csv')
    creating_image_by_timeseries(path, 'instance-137.csv')
    creating_image_by_timeseries(path, 'instance-145.csv')
    creating_image_by_timeseries(path, 'instance-146.csv')
    creating_image_by_timeseries(path, 'instance-153.csv')

def plot_timeseries_from_file(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    phase0 = df.iloc[0]
    phase1 = df.iloc[1]
    phase2 = df.iloc[2]
    plt.plot(phase0)
    plt.plot(phase1)
    plt.plot(phase2)

def experiment_plot_timeseries():
    #path = os.path.join('..', 'data', 'instances-moving-average-8000')
    #plot_timeseries_from_file(path, 'instance-1.csv')
    
    path = os.path.join('..', 'data', 'instances-moving-average-1000')
    # instâncias sem problemas
    plot_timeseries_from_file(path, 'instance-1.csv')
    #plot_timeseries_from_file(path, 'instance-3.csv')
    #plot_timeseries_from_file(path, 'instance-4.csv')
    #plot_timeseries_from_file(path, 'instance-5.csv')
    #plot_timeseries_from_file(path, 'instance-6.csv')
    
    # instâncias com problemas
    #plot_timeseries_from_file(path, 'instance-2.csv')
    #plot_timeseries_from_file(path, 'instance-68.csv')
    #plot_timeseries_from_file(path, 'instance-77.csv')
    #plot_timeseries_from_file(path, 'instance-91.csv')
    #plot_timeseries_from_file(path, 'instance-94.csv')

    #path = os.path.join('..', 'data', 'instances')
    # instâncias sem problemas
    #plot_timeseries_from_file(path, 'instance-1.csv')
    #plot_timeseries_from_file(path, 'instance-3.csv')
    #plot_timeseries_from_file(path, 'instance-4.csv')
    #plot_timeseries_from_file(path, 'instance-5.csv')
    #plot_timeseries_from_file(path, 'instance-6.csv')
    # instâncias com problemas
    #plot_timeseries_from_file(path, 'instance-2.csv')
    #plot_timeseries_from_file(path, 'instance-68.csv')
    #plot_timeseries_from_file(path, 'instance-77.csv')
    #plot_timeseries_from_file(path, 'instance-91.csv')
    #plot_timeseries_from_file(path, 'instance-94.csv')

#Relações lineares
#A correlação de Pearson, assume que os dados sejam normalmente distribuídos.
def correlation_pearson_r(data1, data2):
    corr, pvalue = pearsonr(data1, data2)
    alpha = 0.05
    print("Teste Correlação de Pearson R:")
    print("    coeficiente da correlação R: {:.4f}".format(corr))
    print("    p-value reference (alpha): {:.4f}".format(alpha))
    print("    p-value: {:.4f}".format(pvalue))
    if pvalue <= alpha:
        print("    Interpretação: Baixa probabilidade da correlação ser ao acaso")
    else:
        print("    Interpretação: Alta probabilidade da correlação ser ao acaso")
    if 0.9 <= abs(corr) <= 1.0:
        print("    Interpretação: Correlação muito forte")
    elif 0.7 <= abs(corr) < 0.9:
        print("    Interpretação: Correlação forte")
    elif 0.4 <= abs(corr) < 0.7:
        print("    Interpretação: Correlação moderada")
    elif 0.2 <= abs(corr) < 0.4:
        print("    Interpretação: Correlação fraca")
    if 0.0 <= abs(corr) < 0.2:
        print("    Interpretação: Correlação muito fraca")

#Relações não lineares monotonas
#Diferentemente da correlação de Pearson, a correlação de Spearman não 
#assume que os dois conjuntos de dados sejam normalmente distribuídos. 
def correlation_spearman_rho(data1, data2):
    corr, pvalue = spearmanr(data1, data2)
    alpha = 0.05
    print("Teste Correlação de Spearman R:")
    print("    coeficiente da correlação R: {:.4f}".format(corr))
    print("    p-value reference (alpha): {:.4f}".format(alpha))
    print("    p-value: {:.4f}".format(pvalue))
    if pvalue <= alpha:
        print("    Interpretação: Baixa probabilidade da correlação ser ao acaso")
    else:
        print("    Interpretação: Alta probabilidade da correlação ser ao acaso")
    if 0.9 <= abs(corr) <= 1.0:
        print("    Interpretação: Correlação muito forte")
    elif 0.7 <= abs(corr) < 0.9:
        print("    Interpretação: Correlação forte")
    elif 0.4 <= abs(corr) < 0.7:
        print("    Interpretação: Correlação moderada")
    elif 0.2 <= abs(corr) < 0.4:
        print("    Interpretação: Correlação fraca")
    if 0.0 <= abs(corr) < 0.2:
        print("    Interpretação: Correlação muito fraca")

def analyze_correlation_between_timeseries(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    phase_0 = df.values[0][:-2]
    phase_1 = df.values[1][:-2]
    phase_2 = df.values[2][:-2]
    correlation_pearson_r(phase_0, phase_1)
    correlation_pearson_r(phase_1, phase_2)
    correlation_pearson_r(phase_2, phase_0)
    correlation_spearman_rho(phase_0, phase_1)
    correlation_spearman_rho(phase_1, phase_2)
    correlation_spearman_rho(phase_2, phase_0)

def analyze_correlation_between_timeseries_shift(path, filename, shift=266667):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    phase_0 = df.values[0][:-2]
    phase_1 = df.values[1][:-2]
    phase_2 = df.values[2][:-2]
    nphase_1 = []
    for i in range(len(phase_1)):
        if i+shift < len(phase_1):
            nphase_1.append(phase_1[i + shift])
        else:
            nphase_1.append(phase_1[i - (len(phase_1) - shift)])
    nphase_2 = []
    for i in range(len(phase_2)):
        if i+2*shift < len(phase_2):
            nphase_2.append(phase_2[i + 2*shift])
        else:
            nphase_2.append(phase_2[i - (len(phase_2) - 2*shift)])
    correlation_pearson_r(phase_0, nphase_1)
    correlation_pearson_r(nphase_1, nphase_2)
    correlation_pearson_r(nphase_2, phase_0)
    correlation_spearman_rho(phase_0, nphase_1)
    correlation_spearman_rho(nphase_1, nphase_2)
    correlation_spearman_rho(nphase_2, phase_0)

def experiment_analyze_correlation():
    path = os.path.join('..', 'data', 'instances')
    # instâncias sem problemas
    analyze_correlation_between_timeseries(path, 'instance-1.csv')
    analyze_correlation_between_timeseries(path, 'instance-3.csv')
    analyze_correlation_between_timeseries(path, 'instance-4.csv')
    analyze_correlation_between_timeseries(path, 'instance-5.csv')
    analyze_correlation_between_timeseries(path, 'instance-6.csv')
    
    # instâncias com problemas
    analyze_correlation_between_timeseries(path, 'instance-2.csv')
    analyze_correlation_between_timeseries(path, 'instance-68.csv')
    analyze_correlation_between_timeseries(path, 'instance-77.csv')
    analyze_correlation_between_timeseries(path, 'instance-91.csv')
    analyze_correlation_between_timeseries(path, 'instance-94.csv')
    
    # instâncias sem problemas
    analyze_correlation_between_timeseries_shift(path, 'instance-1.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-3.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-4.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-5.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-6.csv')
    # instâncias com problemas
    analyze_correlation_between_timeseries_shift(path, 'instance-2.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-68.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-77.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-91.csv')
    analyze_correlation_between_timeseries_shift(path, 'instance-94.csv')

def stats_extraction_of_timeseries(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    phase_0 = df.values[0][:-2]
    phase_1 = df.values[1][:-2]
    phase_2 = df.values[2][:-2]
    mean_0 = np.mean(phase_0)
    mean_1 = np.mean(phase_1)
    mean_2 = np.mean(phase_2)
    median_0 = np.median(phase_0)
    median_1 = np.median(phase_1)
    median_2 = np.median(phase_2)
    rms_0 = np.sqrt(np.mean(phase_0**2))
    rms_1 = np.sqrt(np.mean(phase_1**2))
    rms_2 = np.sqrt(np.mean(phase_2**2))
    std_0 = np.std(phase_0, ddof=0)
    std_1 = np.std(phase_1, ddof=0)
    std_2 = np.std(phase_2, ddof=0)
    kurtosis_0 = kurtosis(phase_0)
    kurtosis_1 = kurtosis(phase_1)
    kurtosis_2 = kurtosis(phase_2)
    skew_0 = skew(phase_0)
    skew_1 = skew(phase_1)
    skew_2 = skew(phase_2)
    min_0 = np.min(phase_0)
    min_1 = np.min(phase_1)
    min_2 = np.min(phase_2)
    max_0 = np.max(phase_0)
    max_1 = np.max(phase_1)
    max_2 = np.max(phase_2)
    print('mean0; {}'.format(mean_0))
    print('mean1; {}'.format(mean_1))
    print('mean2; {}'.format(mean_2))
    print('median0; {}'.format(median_0))
    print('median1; {}'.format(median_1))
    print('median2; {}'.format(median_2))
    print('rms0; {}'.format(rms_0))
    print('rms1; {}'.format(rms_1))
    print('rms2; {}'.format(rms_2))
    print('std0; {}'.format(std_0))
    print('std1; {}'.format(std_1))
    print('std2; {}'.format(std_2))
    print('kurtosis0; {}'.format(kurtosis_0))
    print('kurtosis1; {}'.format(kurtosis_1))
    print('kurtosis2; {}'.format(kurtosis_2))
    print('skew0; {}'.format(skew_0))
    print('skew1; {}'.format(skew_1))
    print('skew2; {}'.format(skew_2))
    print('min0; {}'.format(min_0))
    print('min1; {}'.format(min_1))
    print('min2; {}'.format(min_2))
    print('max0; {}'.format(max_0))
    print('max1; {}'.format(max_1))
    print('max2; {}'.format(max_2))

def experiment_stats_extraction_of_timeseries():
    path = os.path.join('..', 'data', 'instances')
    # instâncias sem problemas
    stats_extraction_of_timeseries(path, 'instance-1.csv')
    stats_extraction_of_timeseries(path, 'instance-3.csv')
    stats_extraction_of_timeseries(path, 'instance-4.csv')
    stats_extraction_of_timeseries(path, 'instance-5.csv')
    stats_extraction_of_timeseries(path, 'instance-6.csv')
    
    # instâncias com problemas
    stats_extraction_of_timeseries(path, 'instance-2.csv')
    stats_extraction_of_timeseries(path, 'instance-68.csv')
    stats_extraction_of_timeseries(path, 'instance-77.csv')
    stats_extraction_of_timeseries(path, 'instance-91.csv')
    stats_extraction_of_timeseries(path, 'instance-94.csv')

def print_hearder():
    formatter_header = '{};' * 38 + '{}'
    print(formatter_header.format('instance', 'mean_sum', 'mean_sum_abs', 'mean_sum2',
                                  'rms_sum', 'rms_sum_abs', 'rms_sum2', 
                                  'std_sum', 'std_sum_abs', 'std_sum2',
                                  'kurtosis_sum', 'kurtosis_sum_abs', 'kurtosis_sum2',
                                  'skew_sum', 'skew_sum_abs', 'skew_sum2',
                                  'min_sum', 'min_sum2', 'max_sum2',
                                  'intensity', 'cont', 'intensity_quad', 'cont_quad',
                                  'rms_phase0', 'rms_phase1', 'rms_phase2',
                                  'std_phase0', 'std_phase1', 'std_phase2',
                                  'kurtosis_phase0', 'kurtosis_phase1', 'kurtosis_phase2',
                                  'skew_phase0', 'skew_phase1', 'skew_phase2',
                                  'corr_phase0_phase1', 'corr_phase1_phase2', 'corr_phase2_phase0',
                                  'target'
                                  ))

def features_extraction_of_data(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    phase_0 = df.values[0][:-2]
    phase_1 = df.values[1][:-2]
    phase_2 = df.values[2][:-2]
    
    vsum = phase_0 + phase_1 + phase_2
    vsum_abs = abs(vsum)
    vsum2 = phase_0 * phase_0 + phase_1 * phase_1 + phase_2 * phase_2
    
    mean_sum = np.mean(vsum)
    mean_sum_abs = np.mean(vsum_abs)
    mean_sum2 = np.mean(vsum2)
    rms_sum = np.sqrt(np.mean(vsum**2))
    rms_sum_abs = np.sqrt(np.mean(vsum_abs**2))
    rms_sum2 = np.sqrt(np.mean(vsum2**2))
    std_sum = np.std(vsum, ddof=0)
    std_sum_abs = np.std(vsum_abs, ddof=0)
    std_sum2 = np.std(vsum2, ddof=0)
    kurtosis_sum = kurtosis(vsum)
    kurtosis_sum_abs = kurtosis(vsum_abs)
    kurtosis_sum2 = kurtosis(vsum2)
    skew_sum = skew(vsum)
    skew_sum_abs = skew(vsum_abs)
    skew_sum2 = skew(vsum2)
    min_sum = np.min(vsum)
    min_sum2 = np.min(vsum2)
    max_sum2 = np.max(vsum2)
    
    cont = 0.0
    intensity = 0.0
    cont_quad = 0.0
    intensity_quad = 0.0
    thresold = 15
    thresold_quad = 800
    for i in range(len(vsum)):
        if abs(vsum[i]) > thresold: 
            cont += 1
            intensity += abs(vsum[i]) - thresold
    for i in range(len(vsum2)):
        if abs(vsum2[i]) > thresold_quad: 
            cont_quad += 1
            intensity_quad += abs(vsum2[i]) - thresold_quad
    intensity = intensity / len(vsum)
    cont = (100.0 * cont) / len(vsum)
    intensity_quad = intensity_quad / len(vsum2)
    cont_quad = (100.0 * cont_quad) / len(vsum2)
    
    rms_phase0 = np.sqrt(np.mean(phase_0**2))
    rms_phase1 = np.sqrt(np.mean(phase_1**2))
    rms_phase2 = np.sqrt(np.mean(phase_2**2))
    
    std_phase0 = np.std(phase_0, ddof=0)
    std_phase1 = np.std(phase_1, ddof=0)
    std_phase2 = np.std(phase_2, ddof=0)
    
    kurtosis_phase0 = kurtosis(phase_0)
    kurtosis_phase1 = kurtosis(phase_1)
    kurtosis_phase2 = kurtosis(phase_2)
    
    skew_phase0 = skew(phase_0)
    skew_phase1 = skew(phase_1)
    skew_phase2 = skew(phase_2)
    
    shift = 266667  # 800000/3
    nphase_1 = []
    nphase_2 = []
    for i in range(len(phase_1)):
        if i+shift < len(phase_1):
            nphase_1.append(phase_1[i + shift])
        else:
            nphase_1.append(phase_1[i - (len(phase_1) - shift)])
        if i+2*shift < len(phase_2):
            nphase_2.append(phase_2[i + 2*shift])
        else:
            nphase_2.append(phase_2[i - (len(phase_2) - 2*shift)])
    
    corr_phase0_phase1, _ = pearsonr(phase_0, nphase_1)
    corr_phase1_phase2, _ = pearsonr(nphase_1, nphase_2)
    corr_phase2_phase0, _ = pearsonr(nphase_2, phase_0)
    target = df.iloc[0][800002]
    
    df_sum = pd.DataFrame(vsum)
    df_sum_abs = pd.DataFrame(vsum_abs)
    df_sum.to_csv(os.path.join('..', 'data', 'instances-features', 'soma_{}'.format(filename)), 
                  index=False, header=False, index_label=False)
    df_sum_abs.to_csv(os.path.join('..', 'data', 'instances-features', 'soma_abs_{}'.format(filename)), 
                      index=False, header=False, index_label=False)
    
    header = '{};' * 38 + '{}'
    print(header.format(filename, mean_sum, mean_sum_abs, mean_sum2,
                        rms_sum, rms_sum_abs, rms_sum2, 
                        std_sum, std_sum_abs, std_sum2,
                        kurtosis_sum, kurtosis_sum_abs, kurtosis_sum2,
                        skew_sum, skew_sum_abs, skew_sum2,
                        min_sum, min_sum2, max_sum2, intensity, cont,
                        intensity_quad, cont_quad,
                        rms_phase0, rms_phase1, rms_phase2,
                        std_phase0, std_phase1, std_phase2,
                        kurtosis_phase0, kurtosis_phase1, kurtosis_phase2,
                        skew_phase0, skew_phase1, skew_phase2,
                        corr_phase0_phase1, corr_phase1_phase2, corr_phase2_phase0,
                        target
                        ))
    #print('instance; {}'.format(filename))
    #print('mean_sum; {}'.format(mean_sum))
    #print('mean_sum_abs; {}'.format(mean_sum_abs))
    #print('mean_sum_quad; {}'.format(mean_sum2))
    #print('rms_sum; {}'.format(rms_sum))
    #print('rms_sum_abs; {}'.format(rms_sum_abs))
    #print('rms_sum_quad; {}'.format(rms_sum2))
    #print('std_sum; {}'.format(std_sum))
    #print('std_sum_abs; {}'.format(std_sum_abs))
    #print('std_sum_quad; {}'.format(std_sum2))
    #print('kurtosis_sum; {}'.format(kurtosis_sum))
    #print('kurtosis_sum_abs; {}'.format(kurtosis_sum_abs))
    #print('kurtosis_sum_quad; {}'.format(kurtosis_sum2))
    #print('skew_sum; {}'.format(skew_sum))
    #print('skew_sum_abs; {}'.format(skew_sum_abs))
    #print('skew_sum_quad; {}'.format(skew_sum2))
    #print('min_sum; {}'.format(min_sum))
    #print('min_sum_quad; {}'.format(min_sum2))
    #print('max_sum_quad; {}'.format(max_sum2))
    #print('intensidade_sum; {}'.format(intensidade))
    #print('cont_sum; {}'.format(cont))
    #print('intensidade_sum_quad; {}'.format(intensidade_quad))
    #print('cont_sum_quad; {}'.format(cont_quad))
    #print('rms_phase0; {}'.format(rms_phase0))
    #print('rms_phase1; {}'.format(rms_phase1))
    #print('rms_phase2; {}'.format(rms_phase2))
    #print('std_phase0; {}'.format(std_phase0))
    #print('std_phase1; {}'.format(std_phase1))
    #print('std_phase2; {}'.format(std_phase2))
    #print('kurtosis_phase0; {}'.format(kurtosis_phase0))
    #print('kurtosis_phase1; {}'.format(kurtosis_phase1))
    #print('kurtosis_phase2; {}'.format(kurtosis_phase2))
    #print('skew_phase0; {}'.format(skew_phase0))
    #print('skew_phase1; {}'.format(skew_phase1))
    #print('skew_phase2; {}'.format(skew_phase2))
    #print('corr_phase0_phase1; {}'.format(corr_phase0_phase1))
    #print('corr_phase1_phase2; {}'.format(corr_phase1_phase2))
    #print('corr_phase2_phase0; {}'.format(corr_phase2_phase0))

def experiment_features_extraction_of_data():
    path = os.path.join('..', 'data', 'instances')
    print_hearder()
    # instâncias sem problemas
    features_extraction_of_data(path, 'instance-1.csv')
    features_extraction_of_data(path, 'instance-3.csv')
    features_extraction_of_data(path, 'instance-4.csv')
    features_extraction_of_data(path, 'instance-5.csv')
    features_extraction_of_data(path, 'instance-6.csv')
    
    # instâncias com problemas
    features_extraction_of_data(path, 'instance-2.csv')
    features_extraction_of_data(path, 'instance-68.csv')
    features_extraction_of_data(path, 'instance-77.csv')
    features_extraction_of_data(path, 'instance-91.csv')
    features_extraction_of_data(path, 'instance-94.csv')

def experiment_features_extraction_all_instances():
    path = os.path.join('..', 'data', 'instances')
    print_hearder()
    for i in range(1, 168):
        features_extraction_of_data(path, 'instance-{}.csv'.format(i))

def plot_one_timeseries_from_file(path, filename):
    df = pd.read_csv(os.path.join(path, filename), header=None)
    plt.plot(df.transpose().values[0])

def experiment_plot_feature_timeseries():
    path = os.path.join('..', 'data', 'instances-features')
    # instâncias sem problemas
    plot_one_timeseries_from_file(path, 'soma_instance-1.csv')
    plot_one_timeseries_from_file(path, 'soma_instance-3.csv')
    plot_one_timeseries_from_file(path, 'soma_instance-4.csv')
    plot_one_timeseries_from_file(path, 'soma_instance-5.csv')
    plot_one_timeseries_from_file(path, 'soma_instance-6.csv')
    
    # instâncias com problemas
    #plot_one_timeseries_from_file(path, 'soma_instance-2.csv')
    #plot_one_timeseries_from_file(path, 'soma_instance-68.csv')
    #plot_one_timeseries_from_file(path, 'soma_instance-77.csv')
    #plot_one_timeseries_from_file(path, 'soma_instance-91.csv')
    #plot_one_timeseries_from_file(path, 'soma_instance-94.csv')
    
    # instâncias sem problemas
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-1.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-3.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-4.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-5.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-6.csv')
    
    # instâncias com problemas
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-2.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-68.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-77.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-91.csv')
    #plot_one_timeseries_from_file(path, 'soma_abs_instance-94.csv')

# ============= Experimentos da Análise Exploratória do Problema =============

#experiment_analyze_problem_classes()

#experiment_simplification_of_instances()

#experiment_simplification_of_instances_moving_average()

#experiment_create_images_by_timeseries()

experiment_plot_timeseries()

#experiment_analyze_correlation()

#experiment_stats_extraction_of_timeseries()

#experiment_features_extraction_of_data()

#experiment_features_extraction_all_instances()

#experiment_plot_feature_timeseries()
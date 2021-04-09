#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:58:20 2021

@author: Jesimar da Silva Arantes
@email: jesimar.arantes@gmail.com

Conjunto básico de testes de unidade para avaliar as instâncias utilizadas.

"""

from unittest import TestCase, main

import os
import numpy as np
import pandas as pd

class BasicTests(TestCase):
    
    #instancia sem problema
    def test_file_analysis_instance1(self):
        path = os.path.join('data', 'instances', 'instance-1.csv')
        df = pd.read_csv(path, header=None)
        values_init_phase0 = df.iloc[0][:10].values
        values_final_phase0 = df.iloc[0][799999:800003].values
        values_init_phase1 = df.iloc[1][:10].values
        values_final_phase1 = df.iloc[1][799999:800003].values
        values_init_phase2 = df.iloc[2][:10].values
        values_final_phase2 = df.iloc[2][799999:800003].values
        serie_init_phase0 = np.array([18, 18, 17, 18, 18, 18, 19, 18, 18, 17])
        serie_final_phase0 = np.array([17, 0, 0, 0])
        serie_init_phase1 = np.array([1, 0, -1, 1, 0, 0, 1, 0, 0, 0])
        serie_final_phase1 = np.array([0, 1, 1, 0])
        serie_init_phase2 = np.array([-19, -19, -20, -19, -19, -20, -18, -19, -20, -19])
        serie_final_phase2 = np.array([-19, 2, 2, 0])
        self.assertEqual((values_init_phase0 == serie_init_phase0).all(), True)
        self.assertEqual((values_final_phase0 == serie_final_phase0).all(), True)
        self.assertEqual((values_init_phase1 == serie_init_phase1).all(), True)
        self.assertEqual((values_final_phase1 == serie_final_phase1).all(), True)
        self.assertEqual((values_init_phase2 == serie_init_phase2).all(), True)
        self.assertEqual((values_final_phase2 == serie_final_phase2).all(), True)
    
    #instancia com problema
    def test_file_analysis_instance153(self):
        path = os.path.join('data', 'instances', 'instance-153.csv')
        df = pd.read_csv(path, header=None)
        values_init_phase0 = df.iloc[0][:10].values
        values_final_phase0 = df.iloc[0][799999:800003].values
        values_init_phase1 = df.iloc[1][:10].values
        values_final_phase1 = df.iloc[1][799999:800003].values
        values_init_phase2 = df.iloc[2][:10].values
        values_final_phase2 = df.iloc[2][799999:800003].values
        serie_init_phase0 = np.array([-15, -13, -13, -13, -13, -14, -14, -15, -16, -16])
        serie_final_phase0 = np.array([-11, 456, 0, 1])
        serie_init_phase1 = np.array([18, 22, 21, 20, 22, 19, 20, 20, 16, 20])
        serie_final_phase1 = np.array([21, 457, 1, 1])
        serie_init_phase2 = np.array([-7, -3, -4, -6, -3, -6, -5, -5, -8, -5])
        serie_final_phase2 = np.array([-3, 458, 2, 1])
        self.assertEqual((values_init_phase0 == serie_init_phase0).all(), True)
        self.assertEqual((values_final_phase0 == serie_final_phase0).all(), True)
        self.assertEqual((values_init_phase1 == serie_init_phase1).all(), True)
        self.assertEqual((values_final_phase1 == serie_final_phase1).all(), True)
        self.assertEqual((values_init_phase2 == serie_init_phase2).all(), True)
        self.assertEqual((values_final_phase2 == serie_final_phase2).all(), True)
   
if __name__ == '__main__':
    main()

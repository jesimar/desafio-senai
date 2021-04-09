# Resultados Obtidos

## Problema

O problema lida com um sistema trifásico de linhas de tensão. A seguir foi feito um pequeno estudo sobre a teoria do sinal das linhas de tensão e sobre o sinal medido na prática.

### Sinal: Teoria

O sinal em um sistema trifásico de energia de transmissão é um conjunto de três senoides. As senoides estão deslocadas em 120 graus. 
A imagem a seguir ilustra o aspecto geral dos sinais do problema. 

![](./figures/sinal-teoria.png)

A equação de cada um dos sinais é dada por:

```
SinalFase0 = seno(2 * pi * (tempo + 0/3))
SinalFase1 = seno(2 * pi * (tempo + 1/3))
SinalFase2 = seno(2 * pi * (tempo + 2/3))
```

### Sinal: Prática

Um exemplo de sinal de uma linha de tensão em operação normal.

| Com 800000 dados                                      | Com 800 dados (média móvel aplicada)            |
|-------------------------------------------------------|-------------------------------------------------|
| ![](./figures/Sinal800000/Sinal800000-instance1.png)  | ![](./figures/Sinal800/Sinal800-instance1.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance3.png)  | ![](./figures/Sinal800/Sinal800-instance3.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance4.png)  | ![](./figures/Sinal800/Sinal800-instance4.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance5.png)  | ![](./figures/Sinal800/Sinal800-instance5.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance6.png)  | ![](./figures/Sinal800/Sinal800-instance6.png)  |

Um exemplo de sinal de uma linha de tensão em operação ruim.

| Com 800000 dados                                      | Com 800 dados (média móvel aplicada)            |
|-------------------------------------------------------|-------------------------------------------------|
| ![](./figures/Sinal800000/Sinal800000-instance2.png)  | ![](./figures/Sinal800/Sinal800-instance2.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance68.png) | ![](./figures/Sinal800/Sinal800-instance68.png) |
| ![](./figures/Sinal800000/Sinal800000-instance77.png) | ![](./figures/Sinal800/Sinal800-instance77.png) |
| ![](./figures/Sinal800000/Sinal800000-instance91.png) | ![](./figures/Sinal800/Sinal800-instance91.png) |
| ![](./figures/Sinal800000/Sinal800000-instance94.png) | ![](./figures/Sinal800/Sinal800-instance94.png) |

## Teste de Correlação na Instancia 1: Normal

```
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4885
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.5137
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4767
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada

Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4756
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.5000
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4635
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
```

## Teste de Correlação na Instancia 2: Anormal

```
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4911
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.5143
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4785
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada

Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4724
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4961
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4649
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
```

## Teste de Correlação na Instancia 94: Anormal

```
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4305
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.5830
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Pearson R:
    coeficiente da correlação R: -0.4159
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
    
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4273
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.5621
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
Teste Correlação de Spearman R:
    coeficiente da correlação R: -0.4135
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação moderada
```

## Teste de Correlação na Instancia 2: Anormal (Deslocado)

```
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9963
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9960
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9958
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
    
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9921
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9921
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9923
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
```

## Teste de Correlação na Instancia 94: Anormal (Deslocado)

```
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9551
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9612
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Pearson R:
    coeficiente da correlação R: 0.9588
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
    
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9610
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9695
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
Teste Correlação de Spearman R:
    coeficiente da correlação R: 0.9645
    p-value reference (alpha): 0.0500
    p-value: 0.0000
    Interpretação: Baixa probabilidade da correlação ser ao acaso
    Interpretação: Correlação muito forte
```

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

:warning: **Nota:** o valor do sinal também deve ser multiplicado pela tensão máxima do dispositivo gerador.

### Sinal: Prática

**Sem descarga parcial:** A seguir são ilustrados alguns exemplos de sinais de uma linha de tensão em operação normal.

| Com 800000 dados                                      | Com 800 dados (média móvel aplicada)            |
|-------------------------------------------------------|-------------------------------------------------|
| ![](./figures/Sinal800000/Sinal800000-instance1.png)  | ![](./figures/Sinal800/Sinal800-instance1.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance3.png)  | ![](./figures/Sinal800/Sinal800-instance3.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance4.png)  | ![](./figures/Sinal800/Sinal800-instance4.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance5.png)  | ![](./figures/Sinal800/Sinal800-instance5.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance6.png)  | ![](./figures/Sinal800/Sinal800-instance6.png)  |

**Com descarga parcial:** A seguir são ilustrados alguns exemplos de sinais de uma linha de tensão em operação ruim.

| Com 800000 dados                                      | Com 800 dados (média móvel aplicada)            |
|-------------------------------------------------------|-------------------------------------------------|
| ![](./figures/Sinal800000/Sinal800000-instance2.png)  | ![](./figures/Sinal800/Sinal800-instance2.png)  |
| ![](./figures/Sinal800000/Sinal800000-instance68.png) | ![](./figures/Sinal800/Sinal800-instance68.png) |
| ![](./figures/Sinal800000/Sinal800000-instance77.png) | ![](./figures/Sinal800/Sinal800-instance77.png) |
| ![](./figures/Sinal800000/Sinal800000-instance91.png) | ![](./figures/Sinal800/Sinal800-instance91.png) |
| ![](./figures/Sinal800000/Sinal800000-instance94.png) | ![](./figures/Sinal800/Sinal800-instance94.png) |


## Experimento Geração de Imagem a Partir do Sinal

Um experimento de geração de uma imagem em RGB a partir das três fases foi feito.

```
RED = Phase0
GREEN = Phase1
BLUE = Phase2
```

Os valores das fases foram normalizados entre 0 a 255. Com limitações de máximo (40) e mínimo (-40). Valores que ultrapassaram esse limiar foram definidos como sendo a cor branca.

| Sem descarga parcial                                      | Com descarga parcial                                       |
|-----------------------------------------------------------|------------------------------------------------------------|
| ![](./figures/imgs-maxmin-fixo-new/image-instance-1.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-2.png)   |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-3.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-68.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-4.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-77.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-5.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-91.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-6.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-94.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-7.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-96.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-8.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-99.png)  |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-9.png)  | ![](./figures/imgs-maxmin-fixo-new/image-instance-137.png) |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-10.png) | ![](./figures/imgs-maxmin-fixo-new/image-instance-145.png) |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-11.png) | ![](./figures/imgs-maxmin-fixo-new/image-instance-146.png) |
| ![](./figures/imgs-maxmin-fixo-new/image-instance-12.png) | ![](./figures/imgs-maxmin-fixo-new/image-instance-153.png) |

## Teste de Correlação na Instância 1: Normal

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

## Teste de Correlação na Instância 2: Anormal

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

## Teste de Correlação na Instância 94: Anormal

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

## Teste de Correlação na Instância 2: Anormal (Deslocado)

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

## Teste de Correlação na Instância 94: Anormal (Deslocado)

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

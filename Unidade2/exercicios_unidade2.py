from sklearn.preprocessing import StandardScaler
from dataset_unidade2 import estudantes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

#===============================================================================================================================================
print('\n====================== 1_standardization. ======================')

# Separe as variáveis (X) e o alvo (y)
X = estudantes.drop(columns=['resultado'])
y = estudantes['resultado']


# 1. Divida o dataset em treino e teste
X_train, X_test, y_train, y_test =

knn = KNeighborsClassifier(n_neighbors=3)


# 2. Mostre os valores faltantes na coluna resultado
print("\nQuestão 2.")


# 3. Aplique a função fit do knn


# 4. Mostre o acerto do algoritmo
print("\nQuestão 4.")


#===============================================================================================================================================
print('\n====================== 2_log_normalization ======================')

pd.set_option('display.max_columns', None)


# 1. Print as características estatísticas do dataset
print("\nQuestão 1.")


# 2. Aplique a normalização logarítmica na coluna nota_prova


# 3. Print a variância da coluna nota_prova
print("\nQuestão 3.")


# 4. Print a variância da coluna normalizada
print("\nQuestão 4.")


#===============================================================================================================================================
print('\n====================== 3_Scaling_data ======================')

# 1. Inicialize o scaler
scaler =


# 2. Separe as variáveis (X) e o alvo (y)
X =


# 3. Normalize o dataset com scaler
X_norm =


# 4. Obtenha as labels da coluna resultado
y =


# 5. Print a variância de X
print("\nQuestão 5.")


# 6. Print a variância do dataset X_norm
print("\nQuestão 6.")


# 7. Divida o dataset em treino e teste com estratificação
X_train, X_test, y_train, y_test =


# 8. Inicialize o algoritmo KNN
knn =


# 9. Aplique a função fit do KNN


# 10. Verifique o acerto do classificador
print("\nQuestão 10.")
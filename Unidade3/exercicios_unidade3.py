import numpy as np
import matplotlib.pyplot as plt
from dataset_unidade3 import df_academia

#===============================================================================================================================================
print('\n====================== 1_k-Nearest-Neighbors-Fit ======================')

# 1. Importe o KNeighborsClassifier


# 2. Selecione as variáveis explicativas (X) e a variável alvo (y)


# 3. Crie um modelo KNN com 6 vizinhos


# 4. Treine o modelo com os dados


# 5. Crie dados de teste representando novos alunos da academia
X_test = np.array([
    [6, 9],
    [2, 4],
    [4, 6]
])


# 6. Use o modelo treinado para prever se esses clientes vão cancelar


# 7. Exiba as previsões do modelo
print("\nQuestão 7.")



#===============================================================================================================================================
print('\n====================== 2_evaluate_knn. ======================')

# 1. Importe o módulo train_test_split


# 2. Selecione as variáveis explicativas (X) e a variável alvo (y)


# 3. Divida os dados em treino e teste


# 4. Crie um modelo KNN com 5 vizinhos


# 5. Treine o modelo com os dados de treino


# 6. Calcule e exiba a acurácia do modelo no conjunto de teste
print("\nQuestão 6.")



#===============================================================================================================================================
print('\n====================== 3_underfiting_overfiting ======================')

# 1. Teste diferentes valores de k (de 1 a 10)
neighbors = np.arange(1, 11)
train_accuracies = {}
test_accuracies = {}


for neighbor in neighbors:
    # 2. Crie um modelo KNN para cada valor de k


    # 3. Treine o modelo


    # 4. Calcule a acurácia no conjunto de treino e teste


# 5. Exiba os resultados de acurácia
print("\nQuestão 5.")


# 6. Plote o gráfico comparando as acurácias
plt.title("KNN: Variação do número de vizinhos (Academia)")
plt.legend()
plt.xlabel("Número de Vizinhos (k)")
plt.ylabel("Acurácia")
plt.show()
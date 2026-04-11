import numpy as np
from dataset_unidade3 import df_academia

#===============================================================================================================================================
print('\n====================== 1_k-Nearest-Neighbors-Fit ======================')

# 1. Importe o KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier


# 2. Selecione as variáveis explicativas (X) e a variável alvo (y)
X = df_academia[["frequencia_semana", "indice_satisfacao"]].values
# Features escolhidas (2 variáveis para o KNN simples)
y = df_academia["cancelou"].values
# Variável alvo (se cancelou ou não a mensalidade)


# 3. Crie um modelo KNN com 6 vizinhos
knn = KNeighborsClassifier(n_neighbors=6)


# 4. Treine o modelo com os dados
knn.fit(X, y)


# 5. Crie dados de teste representando novos alunos da academia
X_test = np.array([
    [6, 9],   # alta frequência, alta satisfação
    [2, 4],   # baixa frequência, baixa satisfação
    [4, 6]    # média frequência, média satisfação
])


# 6. Use o modelo treinado para prever se esses clientes vão cancelar
y_pred = knn.predict(X_test)


# 7. Exiba as previsões do modelo
print("\nQuestão 7.")
print(y_pred)



#===============================================================================================================================================
print('\n====================== 2_evaluate_knn. ======================')

# 1. Importe o módulo train_test_split
from sklearn.model_selection import train_test_split


# 2. Selecione as variáveis explicativas (X) e a variável alvo (y)
X = df_academia[["tempo_mensalidade_meses", "frequencia_semana", "horas_treino_semana", "indice_satisfacao", "dias_faltados_mes"]].values
y = df_academia["cancelou"].values


# 3. Divida os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


# 4. Crie um modelo KNN com 5 vizinhos
knn = KNeighborsClassifier(n_neighbors=5)


# 5. Treine o modelo com os dados de treino
knn.fit(X_train, y_train)


# 6. Calcule e exiba a acurácia do modelo no conjunto de teste
print("\nQuestão 6.")
print(knn.score(X_test, y_test))



#===============================================================================================================================================
print('\n====================== 3_underfiting_overfiting ======================')

import numpy as np
import matplotlib.pyplot as plt

# 1. Teste diferentes valores de k (de 1 a 10)
neighbors = np.arange(1, 11)
train_accuracies = {}
test_accuracies = {}


for neighbor in neighbors:
    # 2. Crie um modelo KNN para cada valor de k
    knn = KNeighborsClassifier(n_neighbors=neighbor)

    # 3. Treine o modelo
    knn.fit(X_train, y_train)

    # 4. Calcule a acurácia no conjunto de treino e teste
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)


# 5. Exiba os resultados de acurácia
print("\nQuestão 7.")
print("Acurácia no treino:", train_accuracies, "\n")
print("Acurácia no teste:", test_accuracies)


# 6. Plote o gráfico comparando as acurácias
plt.title("KNN: Variação do número de vizinhos (Academia)")

plt.plot(neighbors, list(train_accuracies.values()), label="Acurácia Treino")
plt.plot(neighbors, list(test_accuracies.values()), label="Acurácia Teste")

plt.legend()
plt.xlabel("Número de Vizinhos (k)")
plt.ylabel("Acurácia")

plt.show()
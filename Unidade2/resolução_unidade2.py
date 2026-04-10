from sklearn.preprocessing import StandardScaler
from dataset_unidade2 import estudantes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

#===============================================================================================================================================")
print('\n====================== 1_standardization. ======================')

# Separe as variáveis (X) e o alvo (y)
X = estudantes.drop(columns=['resultado'])
y = estudantes['resultado']
# X contém as características (idade, horas_estudo, etc.)
# y contém o que queremos prever (resultado: Aprovado/Reprovado)


# 1. Divida o dataset em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)


knn = KNeighborsClassifier(n_neighbors=3)
# Criamos o modelo KNN com k=3 (ele vai olhar os 3 vizinhos mais próximos)


# 2. Mostre os valores faltantes na coluna resultado
print("\nQuestão 2.")
print(estudantes['resultado'].isnull().sum())
# isnull() verifica quais valores são nulos
# sum() conta quantos valores nulos existem


# 3. Aplique a função fit do knn
knn.fit(X_train, y_train)
# fit() treina o modelo
# Ele aprende padrões nos dados de treino (X_train e y_train)
# No KNN, ele basicamente "memoriza" os dados para comparar depois


# 4. Mostre o acerto do algoritmo
print("\nQuestão 4.")
print(knn.score(X_test, y_test))
# score() calcula a acurácia do modelo
# Ou seja: quantas previsões ele acertou no conjunto de teste
# O valor vai de 0 a 1 (ex: 0.8 = 80% de acerto)


#===============================================================================================================================================")
print('\n====================== 2_log_normalization ======================')

pd.set_option('display.max_columns', None)
# Permite mostrar todas as colunas do dataset ao imprimir


# 1. Print as características estatísticas do dataset
print("\nQuestão 1.")
print(estudantes.describe())
# describe() mostra estatísticas das colunas numéricas, como:
# - média (mean)
# - desvio padrão (std)
# - mínimo (min)
# - máximo (max)
# - quartis (25%, 50%, 75%)


# 2. Aplique a normalização logarítmica na coluna nota_prova
estudantes['nota_prova_log'] = np.log(estudantes['nota_prova'])
# np.log() aplica o logaritmo natural nos valores
# Isso ajuda a "diminuir" diferenças muito grandes entre valores
# Criamos uma nova coluna para guardar os valores transformados


# 3. Print a variância da coluna nota_prova
print("\nQuestão 3.")
print(np.var(estudantes['nota_prova']))
# np.var() calcula a variância
# A variância mede o quanto os valores estão espalhados
# Valores maiores = dados mais dispersos


# 4. Print a variância da coluna normalizada
print("\nQuestão 4.")
print(np.var(estudantes['nota_prova_log']))
# Aqui calculamos a variância depois do log
# Normalmente, o log reduz a variância (dados ficam mais "comportados")

#===============================================================================================================================================")
print('\n====================== 3_Scaling_data ======================')

# 1. Inicialize o scaler
scaler = StandardScaler()
# StandardScaler padroniza os dados:
# transforma os valores para média = 0 e desvio padrão = 1


# 2. Separe as variáveis (X) e o alvo (y)
X = estudantes.drop(columns=['resultado'])
# X contém apenas os dados numéricos (entrada)


# 3. Normalize o dataset com scaler
X_norm = scaler.fit_transform(X)
# fit_transform() faz duas coisas:
# - aprende a média e desvio padrão (fit)
# - aplica a transformação (transform)
# O resultado é um array normalizado


# 4. Obtenha as labels da coluna resultado
y = estudantes['resultado'].values
# y são as classes que queremos prever (Aprovado/Reprovado)


# 5. Print a variância de X
print("\nQuestão 5.")
print('Variância\n', X.var())
# var() calcula a variância de cada coluna
# Aqui vemos o quanto os dados estão espalhados antes da normalização


# 6. Print a variância do dataset X_norm
print("\nQuestão 6.")
print('Variância do dataset normalizado\n', X_norm.var())
# Após o StandardScaler, a variância tende a ficar próxima de 1
# Isso padroniza todas as variáveis na mesma escala


# 7. Divida o dataset em treino e teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, stratify=y, random_state=42)
# Divide os dados em treino e teste
# stratify=y mantém a proporção de classes (Aprovado/Reprovado)


# 8. Inicialize o algoritmo KNN
knn = KNeighborsClassifier(n_neighbors=5)
# Criamos o KNN com k=5 (ele olha os 5 vizinhos mais próximos)


# 9. Aplique a função fit do KNN
knn.fit(X_train, y_train)
# Treina o modelo com os dados de treino


# 10. Verifique o acerto do classificador
print("\nQuestão 10.")
print('score', knn.score(X_test, y_test))
# score() retorna a acurácia
# Ex: 0.8 = 80% de acerto nas previsões
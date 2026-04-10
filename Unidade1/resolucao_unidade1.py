from dataset_unidade1 import alunos

#===============================================================================================================================================")
print('\n====================== 1_pre_processing ======================')

# 1. Mostre o tamanho do dataset alunos
print('\nQuestão 1.')
print(alunos.shape) # .shape retorna a quantidade de linhas e colunas do dataset.


# 2. Mostre as informações do dataset alunos
print('\nQuestão 2.')
alunos.info() # .info() mostra um resumo das colunas, tipos de dados e valores não nulos.


# 3. Mostre quantos valores faltam na coluna cidade
print('\nQuestão 3.')
print(alunos["cidade"].isnull().sum()) # .isnull().sum() conta quantos valores estão faltando (NaN) na coluna.


# 4. Remova as colunas altura e peso do dataset alunos
alunos_columns = alunos.drop(columns=["altura", "peso"]) # .drop(columns=[]) remove colunas específicas do DataFrame.


# 5. Remova as linhas com valores nulos na coluna nota
alunos_subset = alunos_columns.dropna(subset=["nota"])


# 6. Mostre o tamanho do novo dataset alunos_subset
print('\nQuestão 6.')
print(alunos_subset.shape) # .shape mostra a quantidade de linhas e colunas do novo DataFrame.


# ===============================================================================================================================================")
print('\n====================== 2_data_types ======================')

# 1. Mostre os primeiros elementos da coluna
print('\nQuestão 1.')
print(alunos["nota"].head()) # .head() mostra os 5 primeiros valores da coluna.


# 2. Mostre as características da coluna nota
print('\nQuestão 2.')
print(alunos["nota"].describe()) # .describe() mostra estatísticas básicas
print(alunos["nota"].dtype) # .dtype mostra o tipo de dado da coluna.


# 3. Converta a coluna nota para o tipo float
alunos["nota"] = alunos["nota"].astype("float") # .astype() converte o tipo de dado da coluna.


# 4. Mostre as características da coluna nota novamente
print('\nQuestão 4.')
print(alunos["nota"].describe()) # .describe() mostra estatísticas básicas
print(alunos["nota"].dtype) # .dtype mostra o tipo de dado da coluna.


# ===============================================================================================================================================")
print('\n====================== 3_training_and_test_sets ======================')

# 1. Exclua as colunas altura e peso do dataset alunos
alunos_new = alunos.drop(columns=["altura", "peso"]) # .drop(columns=[]) remove colunas específicas do DataFrame.


# 2. Exclua as linhas com valores nulos da coluna cidade
alunos_new = alunos_new.dropna(subset=["cidade"]) # .dropna(subset=[]) remove linhas onde há valores nulos na coluna especificada.


# 3. Mostre o balanceamento das classes na coluna cidade
print('\nQuestão 3.')
print(alunos_new["cidade"].value_counts()) # .value_counts() mostra a quantidade de ocorrências de cada valor na coluna.


# 4. Crie um DataFrame com todas as colunas, exceto cidade
X = alunos_new.drop("cidade", axis=1) # .drop(..., axis=1) remove a coluna especificada do DataFrame.


# 5. Crie um DataFrame de labels com a coluna cidade
y = alunos_new[["cidade"]] # seleciona apenas a coluna que será usada como variável alvo (label).


# 6. Importe a função train_test_split
from sklearn.model_selection import train_test_split # importa a função usada para dividir os dados em treino e teste.


# 7. Separe os dados em treino e teste usando amostragem estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, stratify=y, random_state=42)
 # train_test_split divide os dados mantendo a proporção das classes com stratify.


# 8. Mostre novamente o balanceamento das classes
print('\nQuestão 8.')
print(y_train["cidade"].value_counts()) # mostra a distribuição das classes após a divisão dos dados.
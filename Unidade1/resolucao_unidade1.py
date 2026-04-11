from dataset_unidade1 import alunos

#===============================================================================================================================================
print('\n====================== 1_pre_processing ======================')

# 1. Mostre o tamanho do dataset alunos
print('\nQuestão 1.')
print(alunos.shape)
# .shape retorna uma tupla com (linhas, colunas)


# 2. Mostre as informações do dataset alunos
print('\nQuestão 2.')
alunos.info()
# .info() mostra:
# - nome das colunas
# - tipo de dado de cada coluna
# - quantidade de valores não nulos


# 3. Mostre quantos valores faltam na coluna aprovado
print('\nQuestão 3.')
print(alunos["aprovado"].isnull().sum())
# isnull() identifica valores nulos (NaN)
# sum() conta quantos valores nulos existem na coluna


# 4. Remova as colunas altura e peso do dataset alunos
print('\nQuestão 4.')
alunos_new = alunos.drop(columns=["altura", "peso"])
# .drop(columns=[]) remove colunas específicas do DataFrame
# Aqui estamos criando um novo dataset sem altura e peso


# 5. Remova as linhas com valores nulos na coluna nota
print('\nQuestão 5.')
alunos_new = alunos_new.dropna(subset=["nota"])
# .dropna(subset=[]) remove linhas onde há valores nulos na coluna especificada
# Aqui removemos alunos que não possuem nota


# 6. Mostre o tamanho do novo dataset
print('\nQuestão 6.')
print(alunos_new.shape)
# Mostra o novo tamanho após remover linhas com valores nulos


#===============================================================================================================================================
print('\n====================== 2_data_types ======================')

# 1. Mostre os primeiros elementos da coluna nota
print('\nQuestão 1.')
print(alunos["nota"].head())
# .head() mostra os primeiros valores da coluna (por padrão, 5)


# 2. Mostre as características da coluna nota
print('\nQuestão 2.')
print(alunos_new["nota"].describe())
print(alunos_new["nota"].dtype)
# .describe() mostra estatísticas básicas (média, min, max, etc.)
# .dtype mostra o tipo de dado da coluna


# 3. Converta a coluna nota para o tipo float
alunos_new["nota"] = alunos_new["nota"].astype("float")
# .astype() converte o tipo de dado
# Aqui transformamos a nota de texto para número (float)


# 4. Mostre as características da coluna nota novamente
print('\nQuestão 4.')
print(alunos_new["nota"].describe())
print(alunos_new["nota"].dtype)
# Agora verificamos se a conversão foi feita corretamente


#===============================================================================================================================================
print('\n====================== 3_training_and_test_sets ======================')

# 1. Exclua as linhas com valores nulos da coluna aprovado
alunos_new = alunos_new.dropna(subset=["aprovado"])
# Remove linhas onde a variável alvo (aprovado) está nula


# 2. Mostre o balanceamento das classes na coluna aprovado
print('\nQuestão 2.')
print(alunos_new["aprovado"].value_counts())
# .value_counts() mostra quantas vezes cada categoria aparece


# 3. Crie um DataFrame com todas as colunas, exceto aprovado
X = alunos_new.drop("aprovado", axis=1)
# X contém as variáveis de entrada (features)


# 4. Crie um DataFrame de labels com a coluna aprovado
y = alunos_new["aprovado"]
# y contém a variável alvo (o que queremos prever)


# 5. Importe a função train_test_split
from sklearn.model_selection import train_test_split
# Função usada para dividir os dados em treino e teste


# 6. Separe os dados em treino e teste usando amostragem estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, stratify=y, random_state=42)


# 8. Mostre novamente o balanceamento das classes
print('\nQuestão 7.')
print(y_train.value_counts())
# Verifica se a divisão manteve o equilíbrio das classes
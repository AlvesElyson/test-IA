from dataset_unidade1 import alunos

#===============================================================================================================================================
print('\n====================== 1_pre_processing ======================')

# 1. Mostre o tamanho do dataset alunos
print('\nQuestão 1.')
print(alunos.shape)
# .shape retorna uma tupla com (linhas, colunas)
# Serve para entender o tamanho do dataset


# 2. Mostre as informações do dataset alunos
print('\nQuestão 2.')
alunos.info()
# .info() mostra:
# - nome das colunas
# - tipo de dado de cada coluna
# - quantidade de valores não nulos


# 3. Mostre quantos valores faltam na coluna cidade
print('\nQuestão 3.')
print(alunos["cidade"].isnull().sum())
# isnull() identifica valores nulos (NaN)
# sum() conta quantos valores nulos existem na coluna


# 4. Remova as colunas altura e peso do dataset alunos
alunos_columns = alunos.drop(columns=["altura", "peso"])
# .drop(columns=[]) remove colunas específicas do DataFrame
# Aqui estamos criando um novo dataset sem altura e peso


# 5. Remova as linhas com valores nulos na coluna nota
alunos_subset = alunos_columns.dropna(subset=["nota"])
# .dropna(subset=[]) remove linhas onde há valores nulos na coluna especificada
# Aqui removemos alunos que não possuem nota


# 6. Mostre o tamanho do novo dataset alunos_subset
print('\nQuestão 6.')
print(alunos_subset.shape)
# Mostra o novo tamanho após remover linhas com valores nulos


#===============================================================================================================================================
print('\n====================== 2_data_types ======================')

# 1. Mostre os primeiros elementos da coluna
print('\nQuestão 1.')
print(alunos["nota"].head())
# .head() mostra os primeiros valores da coluna (por padrão, 5)
# Útil para visualizar rapidamente os dados


# 2. Mostre as características da coluna nota
print('\nQuestão 2.')
print(alunos["nota"].describe())
print(alunos["nota"].dtype)
# .describe() mostra estatísticas básicas (média, min, max, etc.)
# .dtype mostra o tipo de dado da coluna


# 3. Converta a coluna nota para o tipo float
alunos["nota"] = alunos["nota"].astype("float")
# .astype() converte o tipo de dado
# Aqui transformamos a nota de texto para número (float)


# 4. Mostre as características da coluna nota novamente
print('\nQuestão 4.')
print(alunos["nota"].describe())
print(alunos["nota"].dtype)
# Agora verificamos se a conversão foi feita corretamente


#===============================================================================================================================================
print('\n====================== 3_training_and_test_sets ======================')

# 1. Exclua as colunas altura e peso do dataset alunos
alunos_new = alunos.drop(columns=["altura", "peso"])
# Removemos colunas que não serão usadas no modelo


# 2. Exclua as linhas com valores nulos da coluna cidade
alunos_new = alunos_new.dropna(subset=["cidade"])
# Remove registros sem informação na variável alvo


# 3. Mostre o balanceamento das classes na coluna cidade
print('\nQuestão 3.')
print(alunos_new["cidade"].value_counts())
# .value_counts() mostra quantas vezes cada categoria aparece
# Ajuda a ver se os dados estão balanceados


# 4. Crie um DataFrame com todas as colunas, exceto cidade
X = alunos_new.drop("cidade", axis=1)
# X contém as variáveis de entrada (features)


# 5. Crie um DataFrame de labels com a coluna cidade
y = alunos_new[["cidade"]]
# y contém a variável alvo (o que queremos prever)


# 6. Importe a função train_test_split
from sklearn.model_selection import train_test_split
# Função usada para dividir os dados em treino e teste


# 7. Separe os dados em treino e teste usando amostragem estratificada
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
# Divide os dados em:
# - treino (para aprender)
# - teste (para avaliar)
# stratify=y mantém a proporção das classes
# random_state garante reprodutibilidade


# 8. Mostre novamente o balanceamento das classes
print('\nQuestão 8.')
print(y_train["cidade"].value_counts())
# Verifica se a divisão manteve o equilíbrio das classes
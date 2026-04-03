from dataset import alunos

# 1. Mostre o tamanho do dataset alunos usando .shape
print('\nQuestão 1.')
print(alunos.shape)
# .shape retorna a quantidade de linhas e colunas do dataset.

# 2. Mostre as informações do dataset alunos usando .info()
print('\nQuestão 2.')
alunos.info()
# .info() mostra um resumo das colunas, tipos de dados e valores não nulos.

# 3. Mostre quantos valores faltam na coluna cidade usando .isnull().sum()
print('\nQuestão 3.')
print(alunos["cidade"].isnull().sum())
# .isnull().sum() conta quantos valores estão faltando (NaN) na coluna.

# 4. Remova as colunas altura e peso do dataset alunos usando .drop(columns=[])
# Coloque-as em uma variável chamada "alunos_columns"
alunos_columns = alunos.drop(columns=["altura", "peso"])
# .drop(columns=[]) remove colunas específicas do DataFrame.

# 5. Remova as linhas com valores nulos na coluna nota .dropna(subset=[])
# Coloque-as em uma variável chamada "alunos_subset"
alunos_subset = alunos_columns.dropna(subset=["nota"])
# .dropna(subset=[]) remove linhas onde há valores nulos na coluna especificada.

# 6. Mostre o tamanho do novo dataset alunos_subset usando .shape
print('\nQuestão 4.')
print(alunos_subset.shape)
# .shape mostra a quantidade de linhas e colunas do novo DataFrame.
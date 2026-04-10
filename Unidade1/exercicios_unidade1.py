from dataset_unidade1 import alunos

# ===============================================================================================================================================")
print('\n====================== 1_pre_processing ======================')

# 1. Mostre o tamanho do dataset alunos
print('\nQuestão 1.')


# 2. Mostre as informações do dataset alunos
print('\nQuestão 2.')


# 3. Mostre quantos valores faltam na coluna cidade
print('\nQuestão 3.')


# 4. Remova as colunas altura e peso do dataset alunos


# 5. Remova as linhas com valores nulos na coluna nota


# 6. Mostre o tamanho do novo dataset alunos_subset
print('\nQuestão 6.')



# ===============================================================================================================================================")
print('\n====================== 2_data_types ======================')

# 1. Mostre os primeiros elementos da coluna nota
print('\nQuestão 1.')


# 2. Mostre as características da coluna nota usando
print('\nQuestão 2.')


# 3. Converta a coluna nota para o tipo float usando


# 4. Mostre as características da coluna nota novamente usando
print('\nQuestão 4.')



# ===============================================================================================================================================")
print('\n====================== 3_training_and_test_sets ======================')

# 1. Exclua as colunas altura e peso do dataset alunos


# 2. Exclua as linhas com valores nulos da coluna nota


# 3. Mostre o balanceamento das classes na coluna cidade
print('\nQuestão 3.')


# 4. Crie um DataFrame com todas as colunas, exceto cidade


# 5. Crie um DataFrame de labels com a coluna cidade


# 6. Importe a função train_test_split
from sklearn.model_selection import train_test_split
# importa a função usada para dividir os dados em treino e teste.


# 7. Separe os dados em treino e teste usando amostragem estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, stratify=y, random_state=42)
# train_test_split divide os dados mantendo a proporção das classes com stratify.


# 8. Mostre novamente o balanceamento das classes
print('\nQuestão 8.')
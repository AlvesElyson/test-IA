from dataset import alunos

print("\n===============================================================================================================================================")

print('\n1_pre_processing')

# 1. Mostre o tamanho do dataset alunos usando .shape
print('\nQuestão 1.')

# 2. Mostre as informações do dataset alunos usando .info()
print('\nQuestão 2.')

# 3. Mostre quantos valores faltam na coluna cidade usando .isnull().sum()
print('\nQuestão 3.')

# 4. Remova as colunas altura e peso do dataset alunos usando .drop(columns=[])

# 5. Remova as linhas com valores nulos na coluna nota .dropna(subset=[])

# 6. Mostre o tamanho do novo dataset alunos_subset usando .shape
print('\nQuestão 6.')


print("\n===============================================================================================================================================")

print('\n2_data_types')

# 1. Mostre os primeiros elementos da coluna nota usando .head()
print('\nQuestão 1.')

# 2. Mostre as características da coluna nota usando .describe() e .dtype
print('\nQuestão 2.')

# 3. Converta a coluna nota para o tipo float usando .astype()

# 4. Mostre as características da coluna nota novamente usando .describe() e .dtype
print('\nQuestão 4.')


print("\n===============================================================================================================================================")

print('\n3_training_and_test_sets')

# 1. Exclua as colunas altura e peso do dataset alunos usando .drop(columns=[])

# 2. Exclua as linhas com valores nulos da coluna nota usando .dropna(subset=[])

# 3. Mostre o balanceamento das classes na coluna cidade usando .value_counts()
print('\nQuestão 3.')

# 4. Crie um DataFrame com todas as colunas, exceto cidade usando .drop(..., axis=1)

# 5. Crie um DataFrame de labels com a coluna cidade

# 6. Importe a função train_test_split
from sklearn.model_selection import train_test_split
# importa a função usada para dividir os dados em treino e teste.

# 7. Separe os dados em treino e teste usando amostragem estratificada
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
# train_test_split divide os dados mantendo a proporção das classes com stratify.

# 8. Mostre novamente o balanceamento das classes usando .value_counts()
print('\nQuestão 8.')
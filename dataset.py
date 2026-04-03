import pandas as pd

dataset = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
    "idade": [20, 22, None, 21, 23],
    "cidade": ["Fortaleza", "São Paulo", None, "Rio", "Salvador"],
    "nota": ["8.5", "7.0", "9.0", None, "6.5"],
    "altura": [1.60, 1.75, 1.80, 1.65, 1.70],
    "peso": [55, 70, 80, 60, 75]
}

alunos = pd.DataFrame(dataset)

print(alunos)
import pandas as pd

dataset = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
             "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"],

    "idade": [20, 22, None, 21, 23,
              24, 22, 20, 21, 23],

    "cidade": ["Fortaleza", "São Paulo", "Rio", "Rio", "Salvador",
               "Fortaleza", "São Paulo", "Rio", "Salvador", "Fortaleza"],

    "nota": ["8.5", "7.0", "9.0", None, "6.5",
             "8.0", "7.5", "9.5", "6.0", "8.2"],

    "altura": [1.60, 1.75, 1.80, 1.65, 1.70,
               1.68, 1.77, 1.62, 1.73, 1.66],

    "peso": [55, 70, 80, 60, 75,
             65, 72, 58, 68, 62]
}
alunos = pd.DataFrame(dataset)

print(alunos)
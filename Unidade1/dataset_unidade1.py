import pandas as pd

dataset = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
             "Fernanda", "Gustavo", "Helena", "Igor", "Juliana",
             "Kleber", "Larissa", "Marcos", "Natália", "Otávio",
             "Paula", "Rafael", "Sabrina", "Tiago", "Vanessa"],

    "idade": [20, 22, None, 21, 23,
              24, None, 20, 21, 23,
              25, 22, None, 21, 24,
              23, 22, None, 20, 21],

    "horas_estudo": [10, 6, 12, None, 5,
                     9, 7, 11, 3, 8,
                     6, None, 10, 4, 7,
                     9, 5, None, 12, 6],

    "faltas": [2, 5, 1, 8, None,
               3, 4, 2, 9, 3,
               6, 7, None, 8, 2,
               3, None, 6, 1, 4],

    "nota": ["8.5", "7.0", "9.0", None, "6.5",
             "8.0", "7.5", "9.5", "6.0", "8.2",
             None, "7.8", "8.7", "5.5", "6.9",
             "9.1", "6.2", None, "9.8", "7.1"],

    "altura": [1.60, 1.75, 1.80, 1.65, 1.70,
               1.68, 1.77, 1.62, None, 1.66,
               1.72, 1.64, 1.78, None, 1.69,
               1.67, 1.74, 1.63, 1.81, None],

    "peso": [55, 70, 80, 60, 75,
             65, None, 58, 68, 62,
             77, 59, None, 54, 73,
             66, 71, None, 82, 60],

    "aprovado": ["sim", "sim", "sim", "não", "não",
                 "sim", "sim", "sim", "não", "sim",
                 "não", "sim", "sim", "não", "não",
                 "sim", "não", "não", "sim", "sim"]
}

alunos = pd.DataFrame(dataset)

print(alunos)
import pandas as pd

dataset = {
    "idade": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
              18, 19, 20, 21, 22, 23, 24, 25, 26, 27],

    "horas_estudo": [2, 3, 4, 5, 6, 7, 8, 2, 3, 4,
                     5, 6, 7, 8, 2, 3, 4, 5, 6, 7],

    "faltas": [10, 8, 5, 3, 2, 1, 0, 12, 9, 6,
               4, 2, 1, 0, 11, 7, 5, 3, 2, 1],

    "nota_prova": [5.0, 6.0, 6.5, 7.0, 7.5, 8.0, 9.0, 5.5, 6.2, 6.8,
                   7.2, 7.8, 8.5, 9.5, 5.8, 6.4, 7.1, 7.6, 8.2, 9.0],

    "nota_trabalho": [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.5, 6.2, 6.8, 7.2,
                      7.6, 8.2, 9.0, 9.8, 6.5, 7.0, 7.8, 8.3, 8.9, 9.2],
}

df = pd.DataFrame(dataset)

df["resultado"] = [
    "Reprovado", "Reprovado", "Reprovado", "Aprovado", "Aprovado",
    "Aprovado", "Aprovado", "Reprovado", "Reprovado", "Reprovado",
    "Aprovado", "Aprovado", "Aprovado", "Aprovado", "Reprovado",
    "Reprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado"
]

estudantes = df

print(estudantes)
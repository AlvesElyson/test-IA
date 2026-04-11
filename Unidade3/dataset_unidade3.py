import pandas as pd

dataset = {
    "tempo_mensalidade_meses": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],

    "frequencia_semana": [
        6, 6, 5, 5, 4, 4, 3, 3, 2, 2,
        1, 1, 2, 2, 3, 3, 4, 4, 5, 5
    ],

    "horas_treino_semana": [
        10, 10, 9, 9, 8, 8, 7, 7, 6, 6,
        5, 5, 6, 6, 7, 7, 8, 8, 9, 9
    ],

    "indice_satisfacao": [
        10, 10, 9, 9, 8, 8, 7, 7, 6, 6,
        5, 5, 4, 4, 3, 3, 2, 2, 1, 1
    ],

    "dias_faltados_mes": [
        0, 0, 1, 1, 2, 2, 3, 3, 5, 5,
        6, 6, 7, 7, 8, 8, 9, 9, 10, 10
    ],

    "cancelou": [
        0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}

df_academia = pd.DataFrame(dataset)

print(df_academia)
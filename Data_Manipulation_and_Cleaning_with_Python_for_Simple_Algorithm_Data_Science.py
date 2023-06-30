# Importando o Pandas
import pandas as pd

# Estruturando o dicionário
dados = {
    "Nome": [
        "João",
        "Maria",
        "José",
        "Ana",
        "Maria"
    ],

    "Idade": [
        '25',
        21,
        30,
        27,
        21
    ],

    "Sexo": [
        "Masc",
        "Fem",
        None,
        "Fem",
        "Fem"
    ],
    
    "Altura": [
        1.75,
        1.90,
        1.80,
        16.0,
        1.90
    ],
    
    "Peso": [
        75,
        67,
        90,
        60,
        67
    ]
}

# Atribuindo o dataframe do dicionário para a variável df
df = pd.DataFrame(dados)


# Atribuindo os valores ausentes à variável valores_ausentes
valores_ausentes = df.isnull()

# Localizando o valor nulo na linha 2 e coluna 2 e atribuindo o valor
df.iloc[2, 2] = "Masc"

# Remove duplicatas e, um dataframe
df = df.drop_duplicates()

# Transformando string em inteiro
df["Idade"] = df["Idade"].astype(int)

# Tratando outliers de 16.0m para 1.60m
df.iloc[3, 3] = 1.60

# Exibindo o dataframe
print(f"\n{df}\n")


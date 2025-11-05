import pandas as pd

# Caminho do arquivo .pkl
caminho = "dataset_masks_modified.pkl"

# Carregar o dataset
df = pd.read_pickle(caminho)

# Mostrar as primeiras linhas e todas as colunas
pd.set_option('display.max_columns', None)
print(df.head())

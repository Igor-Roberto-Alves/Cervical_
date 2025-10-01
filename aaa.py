import os
import pandas as pd

# dataframe vazio para armazenar
Cells_Data = pd.DataFrame(columns=["class", "filepath"])

# percorre todas as pastas
for root, dirs, files in os.walk("archive"):
    # verifica se estamos dentro de uma pasta chamada 'cropped'
    if os.path.basename(root) == "CROPPED":
        # a classe é o nome da pasta anterior
        class_name = os.path.basename(os.path.dirname(root))
        
        for file in files:
            if file.endswith(".bmp"):
                file_path = os.path.join(root, file)
                # adiciona no DataFrame
                Cells_Data = pd.concat([Cells_Data, pd.DataFrame({
                    "class": [class_name],
                    "filepath": [file_path]
                })], ignore_index=True)

print(Cells_Data.head())
print("Total de imagens .bmp:", len(Cells_Data))
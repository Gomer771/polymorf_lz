import pandas as pd

data = {}

df = pd.DataFrame(data)

# Удаление дубликатов в столбце "Имя"
df_unique = df.drop_duplicates(subset=['Терминал оплаты'])

print(df_unique)

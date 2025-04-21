
import pandas as pd
class Terminal:

    def __init__(self, df_path):
        
        self.df = pd.read_csv(df_path) #чтение данных из файла csv.
        print(df_path.loc[1:12, ['Терминал оплаты']])

        



import pandas as pd

class Terminal:
    #читаем цсв файл
    def __init__(self, input_file):
        self.data = pd.read_csv(input_file)
        
#разделяем данные по банкам
    def split_by_bank(self):
        
        banks = ["Белинвестбанк", "БелАгропромбанк", "Беларусбанк", "МаксБанк", "Приорбанк"]

        #извлекаем название банка, убирая код после дефиса
        self.data["Банк"] = self.data["Терминал оплаты"].apply(lambda x: str(x).split("-")[0].strip())

        for i, bank in enumerate(banks, start=1):
            bank_data = self.data[self.data["Банк"] == bank]
            
            filename = f"{i}.csv"
            bank_data.to_csv(filename, index=False)
            print(f"Файл сохранён: {filename}")

    def __invert__(self):
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates()
        removed_count = initial_count - len(self.data)
        print(f"Дубликаты удалены. Удалено записей: {removed_count}")
        return removed_count

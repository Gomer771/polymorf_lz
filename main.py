from terminal import Terminal

if __name__ == "__main__":
    input_file = 'data.csv'
    processor = Terminal(input_file)

    processor.split_by_bank()  # Разделение датасета по банкам 
    removed = ~processor  # Удаление дубликатов и получение их количества

    print(f"удалённых дубликатов: {removed}")

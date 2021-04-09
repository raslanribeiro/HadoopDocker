def word_cont(data_path):
    with open(f"./mock_data/{data_path}", "rt") as file:
        data = file.read()
        words = data.split()
        qtd_words = len(words)
        print('Number of words in text file :', qtd_words)
        return qtd_words

word_cont("example1.txt")
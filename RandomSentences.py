import numpy as np
import pandas as pd


def create_random_word(length):
    word = ''
    while len(word) < length:
        letter = chr(np.random.randint(65, 122))
        if letter.isalpha():
            word += letter
    return word

def create_random_reference(list_of_sentence):
    new_list_of_sentence = list_of_sentence.copy()
    num_of_words = len(list_of_sentence)
    type_ = np.random.randint(1, 4) #[1], [1-10], [1, 4, 8, 10]
    reference = ''
    if type_ == 1:
        reference = '[' + str(np.random.randint(1, 1000)) + ']'
    if type_ == 2:
        number_1 = np.random.randint(1, 1000)
        number_2 = np.random.randint(number_1, 1000)
        reference = '[' + '-'.join([str(number_1), str(number_2)]) + ']'
    if type_ == 3:
        n = np.random.randint(2, 6)
        seq = sorted([np.random.randint(1, 1000) for _ in range(n)])
        seq = [str(i) for i in seq]
        reference = '[' + ', '.join(seq) + ']'

    new_list_of_sentence.insert(np.random.randint(1, num_of_words), reference) if num_of_words > 1 else new_list_of_sentence.insert(-1, reference)
    return new_list_of_sentence

def create_sentence():
    sentence_length = np.random.randint(1, 30)
    sentence = []
    for _ in range(sentence_length):
        word_length = np.random.randint(1, 10)
        sentence.append(create_random_word(word_length))

    sentence_with_reference = create_random_reference(sentence)
    return ' '.join(sentence_with_reference) + '.', ' '.join(sentence) + '.'

input_data = []
target_data = []

for i in range(10000):
    inp, tr = create_sentence()
    input_data.append(inp)
    target_data.append(tr)

df = pd.DataFrame({'Input': input_data, 'Target': target_data})
print(df)
df.to_csv(r'C:\Users\Igor\Downloads\WordsWithAndWithoutReference.csv', sep= ',', index = False, encoding='utf-8')
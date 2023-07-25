import pickle

def read_code_vocab_pkl(name):
    with open(fr'./../dataset/{name}/code.word2id', 'rb') as f:
        code_word2id = pickle.load(f)

    with open(fr'./../dataset/{name}/code.id2word', 'rb') as f:
        code_id2word = pickle.load(f)

    return code_word2id, code_id2word

def read_comment_vocab_pkl(name):
    with open(fr'./../dataset/{name}/comment.word2id', 'rb') as f:
        comment_word2id = pickle.load(f)

    with open(fr'./../dataset/{name}/comment.id2word', 'rb') as f:
        comment_id2word = pickle.load(f)

    return comment_word2id, comment_id2word

if __name__ == '__main__':
    name = 'PCSD'  
    code_word2id, code_id2word = read_code_vocab_pkl(name)
    comment_word2id, comment_id2word = read_comment_vocab_pkl(name)

    with open(fr'./../EDA/{name}/code_word2id.txt', 'w', encoding='utf-8') as f:
        for word, idx in code_word2id.items():
            f.write(f"{word}\t{idx}\n")

    with open(fr'./../EDA/{name}/code_id2word.txt', 'w', encoding='utf-8') as f:
        for idx, word in code_id2word.items():
            f.write(f"{idx}\t{word}\n")

    with open(fr'./../EDA/{name}/comment_word2id.txt', 'w', encoding='utf-8') as f:
        for word, idx in comment_word2id.items():
            f.write(f"{word}\t{idx}\n")

    with open(fr'./../EDA/{name}/comment_id2word.txt', 'w', encoding='utf-8') as f:
        for idx, word in comment_id2word.items():
            f.write(f"{idx}\t{word}\n")


    # Now you have the dictionaries loaded in code_word2id and code_id2word.
    # You can use them as follows:

    # Accessing word-to-id mapping
    # word = "def"
    # word_id = code_word2id.get(word, code_word2id["<UNK>"])  # Replace "<UNK>" with the default value for unknown words
    # print(f"The ID of '{word}' is: {word_id}")

    # # Accessing id-to-word mapping
    # idx = word_id
    # word_from_id = code_id2word.get(idx, "<UNK>")  # Replace "<UNK>" with the default value for unknown indices
    # print(f"The word with ID {idx} is: '{word_from_id}'")

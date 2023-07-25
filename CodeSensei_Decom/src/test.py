# text = "   Hello World friends "

# print(text.split(' '))
# for t in text.split(' ')[:300]:
#     print(t)

from collections import Counter

# Sample code token dictionary
code_token_dict = {
    "for": 10,
    "i": 5,
    "in": 8,
    "range": 3,
    "(": 12,
    ")": 12,
    ":": 6,
    "print": 4,
    "hello": 2,
    "world": 1
}

# Set the desired code vocabulary size (excluding special tokens)
code_vocab_size = 100

# Add special tokens to the code token dictionary
code_token_dict.update({"<PAD>": 0, "<BOS>": 0, "<EOS>": 0, "<UNK>": 0})

# Calculate the code vocabulary using the provided line
code_vocab = [tu[0] for tu in Counter(code_token_dict).most_common(code_vocab_size)]

# Print the resulting code vocabulary
print("Code Vocabulary:", code_vocab)

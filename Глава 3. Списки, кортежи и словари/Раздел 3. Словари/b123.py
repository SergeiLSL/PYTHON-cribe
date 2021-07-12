import json

data = json.load(open("data.json"))


def retrive_definition(word):
    return data[word]


word_user = input("Enter a word: ")

print(retrive_definition(word_user))
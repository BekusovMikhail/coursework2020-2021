import nltk
import pickle
import re


def tokenize(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    text = [word.lower() for word in words if re.findall(r'\b[A-Za-z]+\b', word) and word.isalpha()]
    return text


def form_genprobs(probs, genprobs):
    for i in range(len(probs)):
        if probs[i][0] in genprobs:
            if probs[i][1] in genprobs[probs[i][0]]:
                genprobs[probs[i][0]][probs[i][1]] += 1
            else:
                genprobs[probs[i][0]][probs[i][1]] = 1
        else:
            genprobs[probs[i][0]] = {probs[i][1]: 1}
    return genprobs


def parstext_on_1_word(path, genprobs={}):
    file = open(path)
    text = file.read()
    tokens = tokenize(text)

    probs = [[tokens[i], tokens[i + 1]] for i in range(len(tokens) - 1)]

    return form_genprobs(probs, genprobs)


def parstext_on_2_word(path, genprobs={}):
    file = open(path)
    text = file.read()
    tokens = tokenize(text)

    probs = [[(tokens[i], tokens[i + 1]), tokens[i + 2]] for i in range(len(tokens) - 2)]

    return form_genprobs(probs, genprobs)


def parstext_on_3_word(path, genprobs={}):
    file = open(path)
    text = file.read()
    tokens = tokenize(text)

    probs = [[(tokens[i], tokens[i + 1], tokens[i + 2]), tokens[i + 3]] for i in range(len(tokens) - 3)]

    # probs.sort(key=lambda x: x[0][0])
    # print(probs)

    return form_genprobs(probs, genprobs)


def parstext_on_4_word(path, genprobs={}):
    file = open(path)
    text = file.read()
    tokens = tokenize(text)

    probs = [[(tokens[i], tokens[i + 1], tokens[i + 2], tokens[i + 3]), tokens[i + 4]] for i in range(len(tokens) - 4)]

    # probs.sort(key=lambda x: x[0][0])
    # print(probs)

    return form_genprobs(probs, genprobs)


def PrintInOutput(file, probs):
    fileo = open(file, "wb")
    pickle.dump(probs, fileo)

import pickle
import random
import re

import workwithfiles


def parsprobs(path):
    file = open(path, "rb")
    try:
        probs = pickle.load(file)
    except:
        return {}
    return probs


def AddWordsToData(function=workwithfiles.parstext_on_1_word, file_pickle_from_and_to="", path_to_file_words_from=""):
    probs = parsprobs(file_pickle_from_and_to)
    tmpprobs = function(path_to_file_words_from, probs)
    workwithfiles.PrintInOutput(file_pickle_from_and_to, tmpprobs)


def create_probs_output():
    file = open("probsoutput_1word", "w")
    file = open("probsoutput_2word", "w")
    file = open("probsoutput_3word", "w")
    file_names = ["Anna Karenina.txt",
                  "20000 Leagues Under the Sea.txt",
                  "The Emperor.txt",
                  "The Idiot.txt",
                  "The Mysterious Island.txt",
                  "The War of the Worlds.txt",
                  "TheBrothersKaramazov.txt",
                  "WarandPeaceWoNl.txt"]
    for i in file_names:
        AddWordsToData(workwithfiles.parstext_on_1_word, "probsoutput_1word", i)
        AddWordsToData(workwithfiles.parstext_on_2_word, "probsoutput_2word", i)
        AddWordsToData(workwithfiles.parstext_on_3_word, "probsoutput_3word", i)


# create_probs_output()
genprobs = {}


def GenerateString(first_string, second_string="", third_string="", window=1, number_of_words=10):
    if window == 1:
        probs = parsprobs("probsoutput_1word")
        genprobs = probs.copy()
        HMM = [first_string]
        for i in range(number_of_words):
            flag = 0
            while flag == 0:
                try:
                    # tmp = sorted(list(probs[HMM[i]].items()), key=lambda x: x[1], reverse=True)[0][0]
                    tmp = sorted(list(probs[HMM[i]].items()), key=lambda x: x[1], reverse=True)[random.randint(0, 9)][0]
                    flag = 1
                except:
                    flag = 0
            HMM += [tmp]
            del probs[HMM[i]][tmp]
        HMM = " ".join(HMM)
        print(HMM)
    elif window == 2:
        probs = parsprobs("probsoutput_2word")
        genprobs = probs.copy()
        HMM = [first_string, second_string]
        for i in range(1, number_of_words):
            flag = 0
            # tmp = sorted(list(probs[(HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[0][0]
            while flag == 0:
                try:
                    # tmp = sorted(list(probs[(HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[0][0]
                    tmp = sorted(list(probs[(HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[
                        random.randint(0, 10)][0]
                    flag = 1
                except:
                    flag = 0

            HMM += [tmp]
            del probs[(HMM[i - 1], HMM[i])][tmp]
        HMM = " ".join(HMM)
        print(HMM)
    elif window == 3:
        probs = parsprobs("probsoutput_3word")
        genprobs = probs.copy()
        HMM = [first_string, second_string, third_string]
        for i in range(2, number_of_words):
            flag = 0
            while flag == 0:
                try:
                    # tmp = sorted(list(probs[(HMM[i - 2], HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[0][0]
                    tmp = \
                        sorted(list(probs[(HMM[i - 2], HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[
                            random.randint(0, 5)][0]
                    flag = 1
                except:
                    flag = 0
            HMM += [tmp]
            # del probs[(HMM[i - 2], HMM[i - 1], HMM[i])][tmp]
        HMM = " ".join(HMM)
        print(HMM)


GenerateString("i", window=1)
GenerateString("i", second_string="have", window=2)
GenerateString("i", second_string="want", third_string="to", window=3, number_of_words=15)

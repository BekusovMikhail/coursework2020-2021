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
    open("probsoutput_1word", "w")
    open("probsoutput_2word", "w")
    open("probsoutput_3word", "w")
    open("probsoutput_4word", "w")
    file_names = ["20000 Leagues Under the Sea.txt",
                  "Anna Karenina.txt",
                  "The Count of Monte Cristo.txt",
                  "The Emperor.txt",
                  "The Idiot.txt",
                  "The Master and Margarita.txt",
                  "The Mysterious Island.txt",
                  "The Three Musketeers.txt",
                  "The War of the Worlds.txt",
                  "TheBrothersKaramazov.txt",
                  "WarandPeaceWoNl.txt"]
    for i in file_names:
        AddWordsToData(workwithfiles.parstext_on_1_word, "probsoutput_1word", i)
        AddWordsToData(workwithfiles.parstext_on_2_word, "probsoutput_2word", i)
        AddWordsToData(workwithfiles.parstext_on_3_word, "probsoutput_3word", i)
        AddWordsToData(workwithfiles.parstext_on_4_word, "probsoutput_4word", i)
        print(i)


# create_probs_output()
genprobs = {}


def GenerateString(first_string, second_string="", third_string="", fourth_string="", window=1, number_of_words=10,
                   combinate=False, chance1=0.7, chance2=0.15, chance3=0.45):
    if not combinate:
        if window == 1:
            probs = parsprobs("probsoutput_1word")

            HMM = [first_string]
            for i in range(number_of_words):
                flag = 0
                while flag == 0:
                    try:
                        # tmp = sorted(list(probs[HMM[i]].items()), key=lambda x: x[1], reverse=True)[0][0]
                        tmp = \
                            sorted(list(probs[HMM[i]].items()), key=lambda x: x[1], reverse=True)[random.randint(0, 9)][
                                0]
                        flag = 1
                    except:
                        flag = 0
                HMM += [tmp]
                del probs[HMM[i]][tmp]
            HMM = " ".join(HMM)
            return HMM
        elif window == 2:
            probs = parsprobs("probsoutput_2word")

            if not second_string:
                second_string = GenerateString(first_string, window=1, number_of_words=1).split()[-1]
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
            return HMM
        elif window == 3:
            probs = parsprobs("probsoutput_3word")

            if not second_string:
                second_string = GenerateString(first_string, window=1, number_of_words=1).split()[-1]
            if not third_string:
                third_string = GenerateString(first_string, second_string, window=2, number_of_words=2).split()[-1]
            HMM = [first_string, second_string, third_string]
            for i in range(2, number_of_words):
                flag = 0
                while flag == 0:
                    try:
                        # tmp = sorted(list(probs[(HMM[i - 2], HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[0][0]
                        tmp = \
                            sorted(list(probs[(HMM[i - 2], HMM[i - 1], HMM[i])].items()), key=lambda x: x[1],
                                   reverse=True)[
                                random.randint(0, 5)][0]
                        flag = 1
                    except:
                        flag = 0
                HMM += [tmp]
                del probs[(HMM[i - 2], HMM[i - 1], HMM[i])][tmp]
            HMM = " ".join(HMM)
            return HMM
        elif window == 4:
            probs = parsprobs("probsoutput_4word")
            if not second_string:
                second_string = GenerateString(first_string, window=1, number_of_words=1).split()[-1]
            if not third_string:
                third_string = GenerateString(first_string, second_string, window=2, number_of_words=2).split()[-1]
            if not fourth_string:
                fourth_string = GenerateString(first_string, second_string, third_string, window=3,
                                               number_of_words=3).split()[-1]
            HMM = [first_string, second_string, third_string, fourth_string]
            for i in range(3, number_of_words):
                flag = 0
                while flag == 0:
                    try:
                        # tmp = sorted(list(probs[(HMM[i - 2], HMM[i - 1], HMM[i])].items()), key=lambda x: x[1], reverse=True)[0][0]
                        tmp = \
                            sorted(list(probs[(HMM[i - 3], HMM[i - 2], HMM[i - 1], HMM[i])].items()),
                                   key=lambda x: x[1], reverse=True)[random.randint(0, 5)][0]
                        flag = 1
                    except:
                        flag = 0
                HMM += [tmp]
                del probs[(HMM[i - 3], HMM[i - 2], HMM[i - 1], HMM[i])][tmp]
            HMM = " ".join(HMM)
            return HMM

    else:
        if not second_string:
            second_string = GenerateString(first_string, window=1, number_of_words=1).split()[-1]
        if not third_string:
            third_string = GenerateString(first_string, second_string, window=2, number_of_words=2).split()[-1]
        if not fourth_string:
            fourth_string = GenerateString(first_string, second_string, third_string, window=3,
                                           number_of_words=3).split()[-1]
        HMM = [first_string, second_string, third_string, fourth_string]
        for i in range(3, number_of_words):
            chance = random.random()
            if chance <= chance1:
                HMM.append(GenerateString(first_string=HMM[-1], window=1, number_of_words=1).split()[-1])
            elif chance <= chance1 + chance2:
                HMM.append(
                    GenerateString(first_string=HMM[-2], second_string=HMM[-1],
                                   window=2, number_of_words=2).split()[-1])
            elif chance <= chance1 + chance2 + chance3:
                HMM.append(
                    GenerateString(first_string=HMM[-3], second_string=HMM[-2], third_string=HMM[-1], window=3,
                                   number_of_words=3).split()[-1])
            else:
                HMM.append(
                    GenerateString(first_string=HMM[-4], second_string=HMM[-3], third_string=HMM[-2],
                                   fourth_string=HMM[-1], window=3, number_of_words=3).split()[-1])
        HMM = " ".join(HMM)
        return HMM


# print(GenerateString("i", window=1, number_of_words=15))
# print(GenerateString("i", second_string="have", window=2, number_of_words=2))
# print(GenerateString("i", second_string="want", third_string="to", window=3, number_of_words=3))
print(GenerateString("i", window=4, number_of_words=10))
# print(GenerateString("i", number_of_words=15, combinate=True))

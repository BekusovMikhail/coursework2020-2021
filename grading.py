import kenlm
import generator


# import workwithfiles


def print_score(string, file_for_model='text_score_3.binary'):
    model = kenlm.Model(file_for_model)
    z = model.score(string, eos=True, bos=True)
    print(string, z, 10 ** z, sep='\n')


def print_scores_from_all_models(string):
    print("2-gram model")
    print_score(string, file_for_model='text_score_2.binary')
    print("3-gram model")
    print_score(string, file_for_model='text_score_3.binary')
    print("4-gram model")
    print_score(string, file_for_model='text_score_4.binary')


tmp = "xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx"
print_scores_from_all_models(tmp)
tmp = "The wife had discovered that the husband was carrying on"
print_scores_from_all_models(tmp)
print("--------------------------------------------------------------------", end='\n\n')

for i in ["do", "fly", "make", "speak", "call", "open", "start", "work", "use"]:
    print("window_1")
    tmp = generator.GenerateString(i, window=1, number_of_words=10)
    print_scores_from_all_models(tmp)
    print('\n')
    print("window_2")
    tmp = generator.GenerateString(i, window=2, number_of_words=10)
    print_scores_from_all_models(tmp)
    print('\n')
    print("window_3")
    tmp = generator.GenerateString(i, window=3, number_of_words=10)
    print_scores_from_all_models(tmp)
    print('\n')
    print("window_4")
    tmp = generator.GenerateString(i, window=4, number_of_words=10)
    print_scores_from_all_models(tmp)
    print('\n')
    print("combinate")
    tmp = generator.GenerateString(i, combinate=True, number_of_words=10)
    print_scores_from_all_models(tmp)
    print("\n")
    print("--------------------------------------------------------------------", end='\n\n\n')

# tmpfile = open("full_text_tokenized.txt", "w")
# tokenized_full_text = workwithfiles.tokenize(open("full_text.txt", "r").read())
# print()
# tmpfile.write(" ".join(tokenized_full_text))

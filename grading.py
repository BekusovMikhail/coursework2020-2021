import kenlm
import generator


# import workwithfiles


def print_score(string):
    model = kenlm.Model('full_text_for_score.binary')
    z = model.score(string, eos=True, bos=True)
    print(string, z, 10 ** z, sep='\n')


tmp = "xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx"
print_score(tmp)
print("--------------------------------------------------------------------")

for i in ["hi", "i", "you", "hello", "game"]:
    tmp = generator.GenerateString(i, window=1, number_of_words=10)
    print_score(tmp)
    tmp = generator.GenerateString(i, window=2, number_of_words=10)
    print_score(tmp)
    tmp = generator.GenerateString(i, window=3, number_of_words=10)
    print_score(tmp)
    tmp = generator.GenerateString(i, window=4, number_of_words=10)
    print_score(tmp)
    tmp = generator.GenerateString(i, combinate=True, number_of_words=10)
    print_score(tmp)
    print("--------------------------------------------------------------------")

# tmpfile = open("full_text_tokenized.txt", "w")
# tokenized_full_text = workwithfiles.tokenize(open("full_text.txt", "r").read())
# print()
# tmpfile.write(" ".join(tokenized_full_text))

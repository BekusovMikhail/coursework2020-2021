import kenlm
import generator

# import workwithfiles

model = kenlm.Model('full_text.binary')

tmp = "xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx"
print(tmp)
print(model.score(tmp, eos=True, bos=True))
print("--------------------------------------------------------------------")

for i in ["hi", "i", "you", "hello", "game"]:
    tmp1 = generator.GenerateString(i, window=1, number_of_words=10)
    print(tmp1)
    print(model.score(tmp1, eos=True, bos=True))
    tmp2 = generator.GenerateString(i, window=2, number_of_words=10)
    print(tmp2)
    print(model.score(tmp2, eos=True, bos=True))
    tmp3 = generator.GenerateString(i, window=3, number_of_words=10)
    print(tmp3)
    print(model.score(tmp3, eos=True, bos=True))
    tmp4 = generator.GenerateString(i, window=4, number_of_words=10)
    print(tmp4)
    print(model.score(tmp4, eos=True, bos=True))
    tmp5 = generator.GenerateString(i, combinate=True, number_of_words=10)
    print(tmp5)
    print(model.score(tmp5, eos=True, bos=True))
    print("--------------------------------------------------------------------")

# tmpfile = open("full_text_tokenized.txt", "w")
# tokenized_full_text = workwithfiles.tokenize(open("full_text.txt", "r").read())
# print()
# tmpfile.write(" ".join(tokenized_full_text))

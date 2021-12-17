# 実験的にnltkを用いて品詞分解したものを表示

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

f = open('test.txt', 'r')
data = f.read()
print(data)
s = data
# s = "I saw a girl with a telescope"
morph = nltk.word_tokenize(s)
# print(morph)
print('------------------------------------------------------------')
print("start")
pos = nltk.pos_tag(morph)
for e in pos:
    print(e[0]+":"+e[1])
# print(pos)
print("end")
print('--------------------------------------------------------------')

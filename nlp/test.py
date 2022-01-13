# 実験的にnltkを用いて品詞分解したものを表示

import nltk
from abstractionFilter import absctractionFilter
from grammer_network import check
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

f = open('test.txt', 'r')
data = f.read()
print(data)
s = data
morph = nltk.word_tokenize(s)
print('------------------------------------------------------------')
# print("start")
pos = nltk.pos_tag(morph)
abstracted = absctractionFilter(pos)
result = check(0, abstracted)
print('--------------------------------------------------------------')
print('=====>'+result)

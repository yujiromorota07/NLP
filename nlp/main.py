from xmlrpc.client import boolean
from grammer_network import check
from dictionary import dic
from treeview import treeview

f = open('test.txt', 'r')
# list = f.read().split(" ")
words = []
for word in f.read().split(" "):
    if word in dic:
        words.append([word, dic[word]])
words.insert(0, ['', 'START'])
words.append(['.', 'END'])
result = check(0, words)
treeview(result[0], words)
print(result[1])

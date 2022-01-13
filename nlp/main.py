from grammer_network import check
from dictionary import dic
from treeview import treeview
f = open('test.txt', 'r')
data = f.read()
list = data.split(' ')
list2 = []
for e in list:
    if e in dic:
        list2.append([e, dic[e]])
list2.insert(0, ['', 'START'])
list2.append(['.', 'END'])
# print(list2)
result = check(0, list2)
treeview(result[0], list2)
print(result[1])
# print("result :"+result)

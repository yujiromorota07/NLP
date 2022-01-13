def treeview(n, words):
    for s in range(n):
        for index in range(s):
            print(words[index][0], end=" ")
            print("("+words[index][1]+")", end=" ")

        print("\n")

# ネットワーク文法をチェックする処理を追加


def check(index: int, words: list):

    if index == (len(words)-1):
        # print(words[index][1])
        # return "This is sentence!"
        return [index+2, "this is a sentence!"]
    else:
        current = words[index][1]
        forward = words[index+1][1]
        if check_connection(current, forward):
            # print(words[index][0])
            # # print("|")
            # print(words[index][1])
            # print("\n")
            return check(index+1, words)
        else:
            # return "This is not sentence!"
            return [index+1, "this is not a sentence!"]


def check_connection(current, foward):

    if current == "START":
        if foward != "DET" and foward != "NOUN":
            return False

    if current == "DET":
        if foward != "ADJ" and foward != "NOUN":
            return False

    if current == "NOUN":
        if foward != "DET" and foward != "PREP" and foward != "VERB" and foward != "ADV" and foward != "END":
            return False

    if current == "PREP":
        if foward != "DET" and foward != "NOUN" and foward != "ADJ":
            return False

    if current == "ADV":
        if foward != "NOUN" and foward != "PREP":
            return False

    if current == "VERB":
        if foward != "ADV" and foward != "DET" and foward == "END":
            return False

    if current == "ADJ":
        if foward != "NOUN":
            return False

    return True
    # if current=="END":

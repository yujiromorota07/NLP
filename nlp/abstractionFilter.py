def absctractionFilter(words:list):
    l=len(words)
    abstracted_list=[]
    for index in range(l):
        word_class=words[index][1]
        word=words[index][0]
        convert(word,word_class,abstracted_list)
    abstracted_list.insert(0,['','START'])
    abstracted_list.append(['.',"END"])
    return abstracted_list

def convert(word,word_class,list):
    #形容詞
    if word_class=="JJ" or word_class=="JJR" or word_class=="JJS":
            list.append([word,"ADJ"])
    #名詞
    if word_class=="NN" or word_class=="NNS" or word_class=="NNP" or word_class=="NNPS" or word_class=="PRP":
        list.append([word,"NOUN"])
    #副詞
    if word_class=="RB" or word_class=="RBR" or word_class=="RBS":
        list.append([word,"ADV"])
    #前置詞
    if word_class=="TO":
        list.append([word,"PREP"])
    #動詞
    if word_class=="VB" or word_class=="VBD" or word_class=="VBG" or word_class=="VBN" or word_class=="VBP" or word_class=="VBZ":
        list.append([word,"VERB"])
    #冠詞
    if word_class=="DT":
        list.append([word,"DET"])
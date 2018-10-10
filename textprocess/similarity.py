import difflib
def sequence_match():
    res= difflib.SequenceMatcher(a='haha is a haha es is a ', b='haha is a haha kafka is a').quick_ratio()
    print(res)

documents=[
    '[[teacher.tis1.teacher/YudbzduURsGhxHMRzyfNcA][[teacher.tis1.teacher][1]] DocumentMissingException[[teacher][344]: document missing]]'

]
stoplist=set('for a of the and to in'.split())
texts=[[word for word in document.lower().split() if word not in stoplist] for document in documents]
print(texts)

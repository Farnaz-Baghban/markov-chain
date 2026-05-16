import random
text = """
I love python.
I love coding.
python is awesome.
we Learn python.
she teaches English.
furthermore the langiages are fine.
this is a book.
that was an accident.
sometimes shorter path is better.
for this context concentration is better.
he pays in cash.
tomorrow you will be fine.
today you fail.
yesterday was horrible.
you will reach your goal.
you must change your mind.
you must be wary of people.
someone will help you.
"""


words= text.split()
model={}
# crating a model of key: value
for i in range(len(words)-1):

    words[i] = words[i+1]
# ----------------------------------------
# ----------------------------------------
#     word = words[i]
#     next_word = words[i+1]
# 
# model[word] = [] ->if not already existing
#    model[word].append(next_word)

for i in model:
    current = i
    next_words=random.choice(model[i])
current=random.choice(words)
sentence=[]

for i in model:
    current = i
    next_words=random.choice(model[i])  
sentence.append(current)
sentence.append(next_words)  
    # ----------------------------------
# ----------------------------------------
# choose one word to start with (randomly)
# put that word in sentence
# choose the next word from model
# update the current
# do it again
# 
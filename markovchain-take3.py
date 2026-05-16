# we are goin to care about relation ships and order instead of randomaization
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
you must be wary of bad people.
someone will help you.
"""
# text parser
words = []
sentences=text.split(".")
for i in sentences:
    words.append(i.split())

print(words)
current = random.choice(words)
next_words=[]
model={}


print("----------",current)
for i in words:
    for j in range(len(i)-1):
        word = i[j]
        if word not in model:
            model[word] = []
        
        model[word].append(i[j+1])

print("\n------------------------------\n")
print(model)

for i in words:
    for j in i:
        if j in current and j !=" ":
            next_words.append(j)

print("\n--------------------------\n")
print(next_words)    
    
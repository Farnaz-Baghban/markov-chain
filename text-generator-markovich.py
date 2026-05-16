# Markov Chain
# next words depend on the current word
import random
text = """
I love python
I love coding
python is awesome
we Learn python
she teaches English
"""
words = text.split(" ")
for i in words:
    # if "\n" in i:
    i2=i.replace("\n","")
    words.remove(i)
    words.append(i2)

model = {}
for i in range(len(words) -1):
    word = words[i]
    nextword = words[i + 1]
    
    
    # add the new chosen words to the dictionary called "model"
    # if not already added
    if word not in model:
        model[word] = []
    model[word].append(nextword)

    
    
print(model)

current = "I"
result = [current]
# generate a text:
for _ in range(300):
    nextwords = model.get(current)
    
    if not nextwords:
        break
        
    current= random.choice(nextwords)
    result.append(current)

print(" ".join(result))
    
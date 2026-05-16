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
"""
# text parser
words = []
sentences=text.split(".")
for i in sentences:
    words.append(i.split())
for i in words:
    if "\n" in i:
        i = i.remove("\n")
print(words)


current = random.choice(words)
next_words=[]
model={}
print("----------",current)
for i in words:
    for j in i:
        if j in current and j !=" ":
            next_words.append(j)

print("\n--------------------------\n")
# randomsentence=next_words.join()
print(next_words)    
    
# ---------------------------------------------------
# semi-random association تولید می‌کند
# این اتفاق در بعضی art generatorهای قدیمی هم می‌افتاد.
# چرا هر بار خروجی فرق می‌کند؟
# random.choice(words) به خاطر این خط:

# Random word association
# Keyword clustering
# Probabilistic word filtering


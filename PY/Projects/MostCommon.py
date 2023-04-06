from collections import Counter

with open('py.txt', 'r') as f:
    text = f.read()

    c = Counter(text)
    print(c.most_common())



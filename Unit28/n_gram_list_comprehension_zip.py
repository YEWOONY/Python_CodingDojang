text = 'hello'
print(list(zip([text[i:] for i in range(3)])))  # [('hello'), ('ello'), ('llo')]
print(list(zip(*[text[i:] for i in range(3)])))  # [('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

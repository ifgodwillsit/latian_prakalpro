# In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

# >>> d = Dictionary()

# >>> d.newentry('Apple', 'A fruit that grows on trees')

# >>> print(d.look('Apple'))
# A fruit that grows on trees

# >>> print(d.look('Banana'))
# Can't find entry for Banana
# Good luck and happy coding!

class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        return self.entries.get(word, f"Can't find entry for {word}")
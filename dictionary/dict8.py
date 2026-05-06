# Design a data structure that supports the following two operations:

# addWord / add_word which adds a word,
# search which searches a literal word or a regular expression string containing lowercase letters "a-z" or "." where "." can represent any letter. Return true if the search term fully matches any word previously added; otherwise, return false.
# You may assume that all given words contain only lowercase letters.

# Examples
# wd = WordDictionary()

# wd.add_word("bad")
# wd.add_word("dad")
# wd.add_word("mad")

# wd.search("pad") == False
# wd.search("bad") == True
# wd.search(".ad") == True
# wd.search("b..") == True
# Note: the data structure will be initialized multiple times during the tests!

import re
class WordDictionary:
    def __init__(self):
        self.data=[]
  
    def add_word(self,x):
        self.data.append(x)
  
    def search(self,x):
        for word in self.data:
            if re.match(x+"\Z",word): return True
        return False
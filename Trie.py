   
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_trie = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nav = self.main_trie
        #print(f"Inserting {word}")
        for c in word:
            if c in nav:
                nav = nav[c]
            else:
                nav[c] = dict()
                nav = nav[c]
        # is it word (?)
        nav[True] = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nav = self.main_trie
        for c in word:
            if c in nav:
                nav = nav[c]
                continue
            return False
        return True in nav
        
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nav = self.main_trie
        for c in prefix:
            if c in nav:
                nav = nav[c]
                continue
            return False
        return True
        
        


# Trie object should be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word) # search for word in trie
# param_3 = obj.startsWith(prefix) # return true if word exists in Trie

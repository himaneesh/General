# -*- coding: utf-8 -*-
"""
Created on Tue May 22 00:01:54 2018

@author: sherPCP
"""
## TRIE Revisited

class TrieNode:
    def __init__(self):
        self.children=[None]*26
        
        self.isLastLetter=False
    
    
class Trie:

    def __init__(self):
        self.root= self.getNode()
    
    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
    
    def _getIndex(self,ch):
        return ord(ch)-ord('a')
        
    def insert(self,key):
        rt=self.root
        length=len(key)
        for level in range(length):
            index=self._getIndex(key[level])
            if not rt.children[index]:
                rt.children[index]= self.getNode()
            rt=rt.children[index]
                
            
            rt.isLastLetter=True

    def search(self, key):
        rt=self.root
        length=len(key)
        for level in range(length):
            index=self._getIndex(key[level])
            if not rt.children[index]:
                return False   
            rt=rt.children[index]
            
           
        return True


def main():
    
    keys = ["the","a","there","anaswe","any","by","their",'here']
    op = ["Not present in trie",
              "Present in tire"]
    
    t=Trie()
    print("printing")
    print(t.root)
    print("done")
    for key in keys:
        t.insert(key)
    print("done")
    print("{} ---- {}".format("the",op[t.search("th")]))
   # print("{} ---- {}".format("these",op[t.search("an")]))
    #print("{} ---- {}".format("their",op[t.search("their")]))
    #print("{} ---- {}".format("thaw",op[t.search("thaw")]))





if __name__=='__main__':
    main()

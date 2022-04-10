class Solution:
    def recursion(self, s, index, wordDict):
        #if the index in already in memo 
        if index in self.memo:
            return self.memo[index] 

        #Base Case: if we have exhausted the whole string that means we found a match
        if index>=len(s):
            return True


        ret = False
        for word in wordDict:
            word_length = len(word)
            #if word length is greater than the remaining word we can use in the string
            #then skip the word
            if len(word)>len(s[index:]):
                continue
            #Recusive Case: if the word is a match
            #set the new index to be (index + length of the word) 
            if s[index:index+word_length]==word:
                #"or" is used because we need only one case to successfully pass
                ret = ret or self.recursion(s, index+word_length, wordDict)

        self.memo[index] = ret
        return ret




    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        return self.recursion(s, 0, wordDict)

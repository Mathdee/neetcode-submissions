class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # initialize an empty string to put the encoded result
        for s in strs:
            res += str(len(s)) + "#" + s # "Hello" becomes "5#Hello"
        return res
    def decode(self, s: str) -> List[str]:

        res = [] #holds recovered strings
        i = 0 # tracks the start of current "Length#String" block

        while i < len(s): # Continue until the entire string is encoded
            j = i # starts at 'i' to find the '#' delimiter.

            while s[j] != '#': #Continue until j find '#' to identify number
                j += 1
            
            # slice between 'i' and 'j' and we will find the digit
            #Convert digit to int
            # Example: if s[i:j] is "12", then the next string is 12 characters long
            length = int(s[i:j]) 

            # The actual string data starts immediately after the '#' (at j + 1)
            # It ends exactly 'length' characters later
            start = j+1
            end = start + length

            # Extract that specific slice and add it to our result list
            res.append(s[start:end])

            # Move i pointer to very end of string, puts i at the start of the next length prefix for the next loop.
            i = end

        #return res: list of decoded strings
        return res

class Solution:
    def romanToInt(self, s: str) -> int:
    
        romanNums = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        
        sums = 0;
        
        for i in range(0, len(s)) :
            if ( i+1 < len(s) and romanNums[s[i]] < romanNums[s[i+1]]):
                sums -= romanNums[s[i]]
            else:
                sums += romanNums[s[i]]
        
        
        return sums
            
        
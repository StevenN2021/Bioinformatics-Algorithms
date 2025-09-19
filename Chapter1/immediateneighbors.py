'''
Input: A string Pattern and an integer d.
Output: The collection of strings Neighbors(Pattern, d).
'''

def neighbors(s: str, d: int) -> list[str]:
  """Generate neighbors of a string within a given Hamming distance."""
  res = set()
  res.add(s)

  d = {
    "A" : ["T","C","G"],
    "T" : ["A","C","G"],
    "C" : ["T","A","G"],
    "G" : ["T","C","A"]
  }
  for i in range(len(s)):
    symbol = s[i]
    curr = list(s) 
    for x in d[symbol]: 
      
    
    
  
  
  

# Crypotography
def Cryptography(text,S):
   a=''.join(map(chr,range(97,123))).upper()
   b=[]
   c=[]
   for i in a:
  	 b.append(i)   
   for j in range(0,len(text)):
      if text[j] != " ":
         c.append(b[(int(((a.index(text[j])+S)%26)))])
      else:
         c.append(" ")
   return ''.join(c)  
print(Cryptography("SPY CODER",5))

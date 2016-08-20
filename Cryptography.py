Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Cryptography(text,S):
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

... 
unlock this code
...

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
letterGoodness=[0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
Letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Dict=dict(zip(Letter,letterGoodness))
text=input()
zunumber=[]

for S in range(0,26):
   zu=Cryptography(text,S)
   x=0
   for i in zu:
      if i!=' ':
         x+=Dict.get(i)
   zunumber.append(x)
s=zunumber.index(max(zunumber))
print(Cryptography(text,s))

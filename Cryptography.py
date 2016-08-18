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

import read
import collections



def count():
   s = ""
   for i in df['headline']:
      s+=str(i)
      s+=" "
   s = s.lower()
   s = s.split(sep=None, maxsplit=-1)
#  print(type(s))
#  print(s)
    
   cnt = collections.Counter()
   for word in s:
        cnt[word] += 1
    
   #print(cnt)

   return cnt
    
if __name__ == "__main__":
   cnt = count()
   print(cnt.most_common(100))

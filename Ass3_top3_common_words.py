#Python Program to find top 3 most common words occurring in a list 

l = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 
            'the', 'eyes',  "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]

l1 = []#list containing unique words from l
l2=[]#list containing frequencies of words in l
k=[]#copy of list l2
  
for i in l:              
  if i not in l1: 
      l1.append(i)  
              
for i in range(0, len(l1)): 
    l2.append(l.count(l1[i]))
    
k=list(l2)   
l2.sort(reverse=True)#sorting of list in descending order

for i in range(0,3):
    p=k.index(l2[i])
    print("Top",(i+1)," common word:",l1[p],l2[i]) 
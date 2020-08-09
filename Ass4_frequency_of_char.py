#Python Program to implement frequency_of_chars

new_string = list('asdsadDASDFASCSAASAS')
l1 = []#list containing unique chars from l
l2=[]#list containing frequencies of chars in l
  
for i in new_string:              
  if i not in l1: 
      l1.append(i) 
              
for i in range(0, len(l1)): 
    l2.append(new_string.count(l1[i]))
    print('Frequency of',l1[i],'is',l2[i])
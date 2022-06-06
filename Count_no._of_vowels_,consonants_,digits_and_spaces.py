s=input()
c,v,d,l=0,0,0,0
for i in s:  
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
        v+=1 
    elif i.isalpha():  
        c+=1
    elif i.isdigit():
        d+=1
    else:
        l+=1
print('Vowels: ' "%d" %v)
print('Consonants: ' "%d" %c)
print("Digits: " "%d" %d)
print('White spaces: ' "%d" %l)
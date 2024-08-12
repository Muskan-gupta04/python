str= input('Enter the string: ')
n=len(str)
cnt=0
for i in range(int((n)/2)):
    if(str[i]==str[n-i-1]):
        cnt+=1
        continue
    else:
        print('Given string is not a palindrome')
        
if(cnt==int(n/2)): print('Given string is a palindrome')
        
        
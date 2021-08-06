import sys
def if_palindrome(s):
    if len(s)==1:
        return True
    s1=s[::-1]
    return s1==s
s=input()
l=len(s)
for i in range(1,l-1):
    s1=s[:i]
    if if_palindrome(s1):
        for j in range(1,l-i):
            s2=s[i:i+j]
            s3=s[i+j:]
            if if_palindrome(s2) and if_palindrome(s3):
                print(s1)
                print(s2)
                print(s3)
                sys.exit()
print("Impossible")
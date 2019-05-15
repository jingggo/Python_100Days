##### 字符串
```
def main():
    str1 = 'hello world!'
    print(len(str1))                    #12
    print(str1.capitalize())            #Hello world!
    print(str1.upper())                 #HELLO WORLD!

    print(str1.find('or'))              #7
    print(str1.find('shit'))            #-1

    print(str1.startswith('He'))        #False
    print(str1.startswith('he'))        #True

    print(str1.endswith('!'))           #True

    print(str1.center(50,'*'))          #*******************hello world!*******************

    print(str1.rjust(50, ' '))          #                                      hello world!

    #slice
    str2 = 'abc123456'                  
    print(str2[2])                      #c
    print(str2[2:])                     #c123456
    print(str2[2:5])                    #c12
    #step is 2
    print(str2[2::2])                   #c246
    print(str2[::2])                    #ac246
    #reversed
    print(str2[::-1])                   #654321cba
    
    print(str2[-3:-1])                  #45

    print(str2.isdigit())               #False

    print(str2.isalpha())               #False

    print(str2.isalnum())               #True

    str3='  jjjynag@123.com'
    print(str3)                         #  jjjynag@123.com
    print(str3.strip())                 #jjjynag@123.com

if __name__=='__main__':
    main()
    
    
Output:  
12
Hello world!
HELLO WORLD!
7
-1
False
True
True
*******************hello world!*******************
                                      hello world!
c
c123456
c12
c246
ac246
654321cba
45
False
False
True
  jjjynag@123.com
jjjynag@123.com
```

def palindrome(num: str):
    revnum = num[::-1]

    if not revnum == num:
        num = int(revnum) + int(num)
        palindrome(str(num))
    else:
        print(num) 

if __name__ == '__main__':
    num = input('Please input your number.\n')
    palindrome(num)
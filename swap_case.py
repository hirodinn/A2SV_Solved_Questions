def swap_case(s):
    string = ""
    for ch in s:
        if(ch.isupper()) :
            string+=ch.lower()
        else:
            string+=ch.upper()
    
    return string
    # we can also use the built in method for swapping
    # return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

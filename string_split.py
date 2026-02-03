def split_and_join(line):
    
    joined = ""
    for i in line: 
        if i == " ":
            joined+="-"
        else :
            joined += i
    
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

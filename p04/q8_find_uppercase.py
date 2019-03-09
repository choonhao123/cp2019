def find_num_uppercase(str):
    if len(str)==0:
        return 0
    elif str[0].isupper():
        return 1 + find_num_uppercase(str[1:])
    else:
        return 0 + find_num_uppercase(str[1:])
    
find_num_uppercase('Good MorninG!')

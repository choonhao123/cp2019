def count_letter(str,ch):
    if len(str)==0:
        return 0
    elif str[0]==ch:
        return 1 + count_letter(str[1:],ch)
    else:
        return 0 + count_letter(str[1:],ch)
    
count_letter('Welcome','e')

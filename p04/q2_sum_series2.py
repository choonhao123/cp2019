def sum_series2(i):
    if i == 0:
        return 0
    else:
        return i/(2*i+1) + sum_series2(i-1)
    
sum_series2(3)

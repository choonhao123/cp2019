def sum_series1(i):
    if i == 0:
        return 0
    else:
        return 1/i + sum_series1(i-1)
       

sum_series1(12)

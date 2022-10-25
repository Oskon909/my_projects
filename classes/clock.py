hour =2
minute=12
between=30
def clock(hour,min):
    res=12-hour
    res=res*30
    min_gr=360/60
    res_min=min_gr*min
    summ=res+res_min
    print(summ)

clock(12,30)

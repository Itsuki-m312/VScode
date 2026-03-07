values =[123,145,103,90,110] 


def total_and_avarage(values):
    total = 0
    for value in values:
        total = total + value
    num = len(values)
    avarage = total / num
    return(total,avarage,num)

total,avarage,num = total_and_avarage(values)

print(num,"個の合計",total,"平均",avarage,)
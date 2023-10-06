num = int(input())

res = []
if 100000 > num > 1:
    for i in range(2,num+1):
        if num%i==0:
            res.append(i)
    if len(res) ==1:
        print(f'{num} является простым числом')
    else:
        print(f'{num} является составным числом')
else:
    print('Число должно быть больше 1 и меньше 100000')
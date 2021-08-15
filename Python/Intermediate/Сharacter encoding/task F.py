'''
Общий вид канонического разложения натурального число nn имеет вид
n = p_1^{k_1}*p_2^{k_2} ... p_q^{k_q}

где p_i- делители числа n, p_1 < p_2 < ... < p_qp , а k_i- их кратность.
Формат входных данных
Натуральное число nn, n < 10^{15}n<10 
Формат выходных данных
Каноническое разложение числа n в виде строки p_1:k_1,p_2:k_2, ...p 
'''

def number_factors(n):
    time_list = []
    div = 2
    while n!=1:
        while n%div==0:
            time_list.append(div)     
            n/=div
        div+=1
    time_set = set(time_list)
    count=0
    for i in time_set:
        print(i,end=':')
        if count!=(len(time_set)-1):
            print(time_list.count(i),end=',')
        else:
            print(time_list.count(i),end='')
        count+=1


def main():
    n=int(input())
    if n==1:
        print("1:1",end='')
    else:
        number_factors(n)

main()
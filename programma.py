import decimal
import time
from decimal import Decimal, getcontext



def getMin(Nums):
    MinNum = float(Nums[0])
    for Num in Nums:
        if float(Num) < MinNum:
            MinNum = float(Num)
    return MinNum


def getMax(Nums):
    MaxNum = float(Nums[0])
    for Num in Nums:
        if float(Num) > MaxNum:
            MaxNum = float(Num)
    return MaxNum


def getSum(Nums):
    Sum = 0
    for Num in Nums:
        Sum += float(Num)
    return Sum


def getMulAll(Nums):  # если умножение чисел float будет слишком большим то prod = inf
    Nums_prod = Nums
    prod = 1.0
    limit = 10.0 ** 308
    for i in range(len(Nums_prod)):
        if prod < limit:
            prod *= float(Nums_prod[i])
        else:
            break
    return prod

def vspiskeestnol(Nums):
    if getMulAll(Nums) == 0.0:
        return True
    else:
        return False


def main1():
    start = time.time()
    print('Test reading')
    Nums = open('numbers1.txt', 'r').readlines()
    for Num in Nums:
        print(Num.replace("\n", ''))
    print('Мин = ' + str(getMin(Nums)))
    print('Макс = ' + str(getMax(Nums)))
    print('Сумма = ' + str(getSum(Nums)))
    print('Общее умножение = ' + str(getMulAll(Nums)))
    print('Reading time:', time.time() - start, 'seconds.') \


def main2():
    start = time.time()
    print('Test reading')
    Nums = open('numbers2.txt', 'r').readlines()
    for Num in Nums:
        print(Num.replace("\n", ''))
    print('Мин = ' + str(getMin(Nums)))
    print('Макс = ' + str(getMax(Nums)))
    print('Сумма = ' + str(getSum(Nums)))
    print('Общее умножение = ' + str(getMulAll(Nums)))
    print('Reading time:', time.time() - start, 'seconds.')


def main3():
    start = time.time()
    print('Test reading')
    Nums = open('numbers3.txt', 'r').readlines()
    for Num in Nums:
        print(Num.replace("\n", ''))
    print('Мин = ' + str(getMin(Nums)))
    print('Макс = ' + str(getMax(Nums)))
    print('Сумма = ' + str(getSum(Nums)))
    print('Общее умножение = ' + str(getMulAll(Nums)))
    print('Reading time:', time.time() - start, 'seconds.')



main1()
print('-------------------------------------')
main2()
print('-------------------------------------')
main3()







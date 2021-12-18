# Домашнее задание 3
## В данном домашнем задании нудно было написать код программы, а также проверяющие тесты для нее.
*Код программы:*

```python 
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
```

*Тесты*:
```python 
from programma import getMin, getMax, getSum, getMulAll, vspiskeestnol
import pytest




def test_getMax():
    assert getMax([1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert getMax([-12120, -4523529, 453552, 5343443.23, 0]) == 5343443.23
    assert getMax([-12, -152, 112, 8439, 100000000000000000000, -122.7]) == 100000000000000000000


def test_getMin():
    assert getMin([1, 2, 3, 2, 4, 5, 6, 7]) == 1
    assert getMin([-1022220, -342134451434649, 1324234114132422, 624131313.23, 0]) == -342134451434649
    assert getMin([-4, 6, 1000003400, -1342200.1]) == -1342200.1


def test_getMulAll():
    assert getMulAll([-1, 3132310, 2020, 11]) == -69599928200
    assert getMulAll([121, -11242, 5.14, 7.111]) == -49719041.65227999526768255414310725621686963809172201963518642104950667759410976032086182385683059692
    assert getMulAll([212122, 576, 69127, -4513234, 1.21]) == -4.612422985992084e+19


def test_getSum():
    assert getSum([1, 2, 3, 4, 5]) == 15
    assert getSum([0.1212, 541.424, 12122.3356]) == 12663.8808
    assert getSum([112145, 1345.01232, 13328953, 2743.25713]) == 13445186.269450001

def test_vspiskeestnol():
    assert vspiskeestnol([1, 2, 3, 4, 5, 0]) == True
    assert vspiskeestnol([0.1212, 541.424, 12122.3356]) == False
    ```

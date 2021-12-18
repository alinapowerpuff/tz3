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





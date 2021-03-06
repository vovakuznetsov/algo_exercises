"""https://codeforces.com/contest/1353/problem/C"""
"""Сложность: 1000"""

"""Вам задана доска размера n×n, где n нечетно (не кратно 2). Изначально в каждой клетке доски расположена одна фигура.
За один ход вы можете выбрать ровно одну фигуру, расположенную в какой-либо клетке и передвинуть ее в одну из клеток, 
имеющую общую сторону или угол с текущей клеткой, то есть из клетки (i,j) вы можете передвинуть фигуру в клетку:
(i−1,j−1);
(i−1,j);
(i−1,j+1);
(i,j−1);
(i,j+1);
(i+1,j−1);
(i+1,j);
(i+1,j+1);
Конечно же, вы не можете двигать фигуры в клетки за пределами доски. Допустимо, что после хода в одной клетке будет находиться несколько фигур.

Ваша задача — найти минимальное количество ходов, необходимое, чтобы собрать все фигуры в одной клетке 
(т.е. в n2−1 клетках должно быть расположено 0 фигур и в одной клетке должны быть расположены n2 фигур).
"""

# Решение
"""Будем рассматривать доску как набор "квадратов" от центральной клетки к краям
n - сторона квадрата
cells - количество клеток, составляющих рамку
path - длина пути до центральной клетки
n   cells   path    sum
1   1       0       0
3   8       1       8
5   16      2       32
7   24      3       72
и т.д."""


import itertools


levels = [8*n*n for n in range(250000)] 
res = list(itertools.accumulate(levels))
inp = int(input())
for _ in range(inp):
    n = int(input())
    print(res[n // 2])
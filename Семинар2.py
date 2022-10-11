
# Задача 1. Напишите программу, которая принимает на
# вход число N и выдает список факториалов для чисел от 1
# до N.
import math
def Task1():
    print("Введите N")
    N = int(input())
    list = [math.factorial(i) for i in range(1,N+1)]
    print(list)

# Задача 2. Выведите таблицу истинности для выражения
# ¬(X ∧ Y) ∨ Z.
def Task2():
     print ("X  |  Y  |  Z  |   ¬(X ∧ Y) ∨ Z ")
     for x in range(0,2):
        for y in range(0,2):
            for z in range(0, 2):
                print (x, " | ", y, " | ", z, " | ", int(not(x and y) or z))
                
# Задача 3. Даны две строки. Посчитайте сколько раз
# каждый символ первой строки встречается во второй
def Task3():
    print ("Ведите первую строку ")
    str1 = input()
    print ("Ведите вторую строку ")
    str2 = input()
    for i in range(len(str1)):
        print(f'{str1[i]} - {str2.count(str1[i])} ')

# Задача 4. Задайте список из N элементов, заполненных
# числами из промежутка [-N, N]. Сдвиньте все элементы
# списка на 2 позиции вправо.
def Task4():
    print("Введите N")
    N = int(input())
    print("Введите смещение ")
    count = int(input())
    list = [i for i in range(-N,N+1)]
    print(list)
    new_list = []
    new_list[0:count] = list[len(list)-count:len(list)]
    new_list[count:len(list)-1] = list[0:len(list)-count]
    print(new_list)

Task1()
Task2()
Task3()
Task4()
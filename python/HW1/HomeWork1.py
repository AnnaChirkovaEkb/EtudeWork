# print ("a")
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# print ("Input number of  day in week");
# a=int (input());
# if 6>a>0:
#     print ("workday")
# elif a>=8 or a<=0:
#     print ("Error")
# else:
#     print ("weekend")

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("????????????????")

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print ("Input coorditate if point X")
x=float (input())
print ("Input coorditate if point Y")
y=float (input())

print ("The point is in quarter number")
if x>0 and y>0:
    print ("1")
elif x<0 and y>0:
    print ("2")
elif x<0 and y<0:
    print ("3")    
else:
    print ("4")


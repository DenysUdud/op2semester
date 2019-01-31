def input_func():
    lst = []
    a = input("Please input the lenght of a, b, c and a")
    b = input()
    c = input()
    accuracy = input()
    for i in range(0, c):
        lst.append(i)
    x = search(a,b,c,accuracy, 0, c, lst)
    print(x)


def search(a, b, c, acuuracy, lo, hi, lst):
    i = (lo + hi) / 2
    x = lst[i]
    if square_func_check(a, c, x) == True:
        return x
    else:
        square_func_check(a, c, x)



def square_func_check(a, c, x):
    height = (a**2 - (c/2)**2)**(0.5)
    new_height = height - x
    square_cub = x**2
    square_cub_triangle = square_triangle(height, c) - (square_triangle(new_height, x) - square_right_angled((c-x)/2, x))
    if square_cub.round == square_triangle:
        return True
    elif square_cub.round() < square_cub_triangle:
        return



def square_right_angled(kat_1, kat_2):
    return 0.5*(kat_1 * kat_2)

def square_triangle(height, side):
    return 0.5*(height*side)
# this program is from lab 1 second semester about triangle and square
def input_output_function():
    '''
    None -> None
    This function reads and checks input, then it starts main function and return result to the stdout
    '''
    # method is variable wihch means a method of input and output (file or stdin and stdout).
    method = input("What source you want use for input and output (std or file): ")
    if method == "std":
        a = False
        while a == False:
            triangle_sides = input("Please enter lengths of sides (use spaces between): ")
            lengths_lst = triangle_sides.split()
            a = input_check(lengths_lst, method)
        # sides lst is list with lengths of sides in form a,b,c
        sides_lst = input_check_isoceles(lengths_lst)
        if sides_lst:
            a = sides_lst[0]
            b = sides_lst[1]
            c = sides_lst[2]
            accuracy = input("Please input accuracy: ")
            print(search_square_func(a, b, c, accuracy, 0, a))
    elif method == "file":
        # name is file name
        name = input("Please enter name of file: ")
        file_lst = file_reader(name)
        lengths_lst = []
        for e in file_lst:
            if len(e) == 0:
                file_lst.remove(e)
            else:
                lengths_lst.append(e.split())
        if input_check(lengths_lst, method) != True:
            print("In your are incorect lengths")
            return
        accuracy = lengths_lst[3]
        sides_lst = input_check_isoceles(lengths_lst)
        if sides_lst:
            a = sides_lst[0]
            b = sides_lst[1]
            c = sides_lst[2]
            print(search_square_func(a, b, c, accuracy, 0, a))
        else:
            print("In your are incorect lengths")
            return


def file_reader(file_name):
    '''
    (string) -> list

    This function reads file and returns list, where arguments are rows

    '''
    with open(file_name, "r", encoding='UTF-8', errors="ignore") as file:
        return file.readlines()


def input_check(lst, method):
    '''
    lst -> bool
    Checks wether all elements are int and wether there are 3 elem

    >>> input_check_input([1,2,3])
    True
    >>> input_check_input([])
    False
    '''
    if (len(lst) == 4 and method == "file") or (len(lst) == 3 and method == "std"):
        for e in lst:
            try:
                e = float(e)
            except:
                return
    else:
        return
    return True


def input_check_isoceles(lengths_lst):
    '''
    lst ->
    This function checks wether from input lengths we can make
    isosceles triangle and returns lst with a, b, c - where a,b,c
    are sides of triangle.

    >>> input_check_isoceles([1,2,2])
    [1,2,2]
    '''

    if float(lengths_lst[0]) == float(lengths_lst[1]) and float(lengths_lst[0]) != float(lengths_lst[2]):
        a = float(lengths_lst[2])
        b = float(lengths_lst[0])
        c = b
    elif float(lengths_lst[0]) == float(lengths_lst[2]) and float(lengths_lst[0]) != float(lengths_lst[1]):
        a = float(lengths_lst[1])
        b = float(lengths_lst[0])
        c = b
    elif float(lengths_lst[1]) == float(lengths_lst[2]) and float(lengths_lst[1]) != float(lengths_lst[0]):
        a = float(lengths_lst[0])
        b = float(lengths_lst[1])
        c = b
    else:
        return
    if a < b + c:
        return [a, b, c, ]
    else:
        return


def search_square_func(a, b, c, accuracy, lo, hi):
    accuracy = str(accuracy).count("0")
    x = round((lo + hi)/2, accuracy)
    height = (c**2 - (a/2)**2)**(0.5)
    # height teorem of pephagore ( c, a/2, h ; b = c, a - the longest)
    new_height = height - x
    if round(x ** 2, accuracy) != round(0.5 * (height * a) - ((0.5 * new_height * x) + (x * (a - x/2))),accuracy):
        # x ** 2 - area of squre, 0.5 * (height * a) - area of triangle, (0.5 * new_height * x) - area of upper
        # tringle, (x * (a - x)) - area of small triangles
        return x
    elif round(x ** 2, accuracy) > round(0.5 * (height * a) - ((0.5 * new_height * x) + (x * (a - x/2))),accuracy):
        search_square_func(a, b, c, accuracy, lo, x)
    elif round(x ** 2, accuracy) < round(0.5 * (height * a) - ((0.5 * new_height * x) + (x * (a - x/2))),accuracy):
        search_square_func(a, b, c, accuracy, x, hi)
    elif lo > hi:
        return

input_output_function()













def sum_fractions(f1, f2):
    
    num = find_lcm(f1[1], f2[1])
    denominator = num
    numerator = (f1[0] * num // f1[1]) + (f2[0] * num// f2[1])
    return (numerator,denominator)



def subtract_fractions(f1, f2):
    
    num = find_lcm(f1[1], f2[1])
    denominator = num
    numerator = (f1[0] * num // f1[1]) - (f2[0] * num // f2[1])
    return (numerator,denominator)



def multiply_fractions(f1, f2):
    numerator = f1[0] * f2[0]
    denominator = f1[1] * f2[1]
    return (numerator, denominator)


def divide_fractions(f1, f2):
    numerator = f1[0] * f2[1]
    denominator = f1[1] * f2[0]
    return (numerator,denominator)



def find_lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm
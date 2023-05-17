def multiplication(multiplicator):
    def multiply(number):
        return number * multiplicator
    return multiply

double = multiplication(2)
triply = multiplication(3)
quadruple = multiplication(4)


print(double(4))
print(triply(4))
print(quadruple(4))
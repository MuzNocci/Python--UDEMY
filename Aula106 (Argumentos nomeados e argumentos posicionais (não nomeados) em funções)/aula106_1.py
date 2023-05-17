def soma(x, y, z): #definção de função
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

#soma é o nome da função

soma(5, 4, 2) #argumento posicional

soma(4, y=5, z=2) #argumento posicional e keyword (após o primeiro argumento ou parametro keyword, os demais também deverão ser keyword)

soma(y=5, z=2, x=4) #argumento keyword
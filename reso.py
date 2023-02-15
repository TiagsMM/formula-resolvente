import math

def formula_resolvente(a,b,c):

    insqrt = b*b - 4*a*c

    if insqrt < 0 :
        return None

    xpos= (- b + math.sqrt(insqrt)) / (2 * a)

    if insqrt == 0:
        return (xpos, )

    xneg= (- b - math.sqrt(insqrt)) / (2 * a)

    return (xpos,xneg)

print("ax^2 + bx + c = 0")

print("ᐶ a: ")
x = int(input())

print("ᐶ b: ")
y = int(input())

print("ᐶ c: ")
z = int(input())

resultado = formula_resolvente(x,y,z)

if resultado == None:
    print("Não Existem Raízes Possíveis")
elif len(resultado) == 1:
    print("x = " + str(resultado[0]))
else:
    print("x = " + str(resultado[0]) + ", x = " + str(resultado[1]))
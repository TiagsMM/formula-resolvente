import math

def formula_resolvente(a,b,c):

    insqrt = b^2 - 4*a*c

    if (insqrt) < 0 :
        return None

    xpos= (- b + math.sqrt(insqrt)) / (2 * a)

    xneg= (- b - math.sqrt(insqrt)) / (2 * a)

    return (xpos,xneg)

print("ᐶ a: ")
x = int(input())

print("ᐶ b: ")
y = int(input())

print("ᐶ c: ")
z = int(input())

resultado = formula_resolvente(x,y,z)

if resultado == None:
    print("Não Existem Raízes Possíveis")
else:
    print(formula_resolvente(x,y,z))


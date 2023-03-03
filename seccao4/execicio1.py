def mult(*args):
    total = 1
    for numero in args:
        total *= numero
        
    return total
    
print(mult(2,3))



def par_impar(num):
    if num % 2 == 0:
        return f"{num} é par"
    else:
        return f"{num} é ímpar"
    

print(par_impar(3))
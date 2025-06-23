import emoji
a = float(input('reta 1: '))
b = float(input('reta 2: '))
c = float(input('reta 3: '))

if a - b < c < a + b and c - b < a < c + b and c - a < b < c + a:
    print('Sim, essas retas permitem a formação de um triângulo!!! 🔼')
else:
    print('Ah...não pe possível formar um triângulo com essas retas...❌')

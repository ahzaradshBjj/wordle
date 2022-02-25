import os
os.system("")

print("hola" + '\48m')
print('\033[1;34;48m' + "hola" + '\033[1;37;0m')

# amarillo
print("\x1b[0;37;43m"+ "hola" + "\x1b[0m")
#verde
print('\33[42m'+'gaaa'+'\x1b[0m')
#gris
print('\33[105m'+'gaaa'+'\x1b[0m')

def texto(color, palabra):
    if color == 'verde':
        return (f"\x1b[0;37;43m{palabra}\x1b[0m")

a = texto("verde", "chupala")
print(a)
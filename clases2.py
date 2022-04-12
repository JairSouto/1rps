from enum import auto


class Auto ():
    def __init__(self,marca='',modelo=0):
        self.marca = input('ingrese la marca que posee: ')
        self.modelo = int(input('ingrese el año del modelo que posee:'))
    def mostrar(self):
        print('La marca que selecciono es :', self.marca)
        print('El modelo elegido es ', self.modelo)
class Coche1(Auto):
    def __init__(self):
        super().__init__()
        self.precio = float(input('ingrese el valor del coche '))
    def mostrar(self):
        super().mostrar()
        print('Precio: ', self.precio)
    def gamas(self):
        if self.precio >= 60000 :
            print('Su auto' ,self.marca , 'es de gama alta') 
        elif self.precio >= 30000 and self.precio < 60000:
               print('Su auto', self.marca , 'es de gama media/alta')
        else:
            print('Su auto ', self.marca , 'es de gama baja')
Cliente = Coche1()
Cliente.mostrar()
Cliente.gamas()
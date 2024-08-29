'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class CuentaBancaria:
    def__init__(self, numeroCta, nombreCliente, saldoCta = 0.0, fechaapertura, ultimoRetiro = None, ultimaConsignacion = None):
        self.__numeroCta = numeroCta 
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaapertura  = datatime.now
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion
    
    #Metodo para acceder y modificar los atributos encapsulados 
    def get_numeroCta(self):
        return self.__numeroCta
        
    def get_nombreCliente(self):
        return self.__nombreCliente
        

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
        self.__fechaApertura  = fechaApertura 
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion
    
    #Metodo para obtener y establecer (getters y setters)
    def get_numeroCta(self):
        return self.__numeroCta
        
    def get_nombreCliente(self):
        return self.__nombreCliente
    
    def get_saldoCta(self):
        return self.__saldoCta 
        
    def get_fechaApertura(self):
        return self.__fechaApertura
        
    def get_UltimoRetiro(self): 
        return self.__ultimoRetiro
        
    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion
        
    # Setters
    def set_ultimoretiro(self, fecha):
        self.__ultimoRetiro = fecha

    def set_ultimaConsignacion(self, fecha):
        self.__ultimaConsignacion = fecha

    # Métodos para consignat, retirar y transferir
    def consignar (self, cantidad, fecha):
        if cantidad > 0:
            self.__saldoCta += cantidad 
            self.set_ ultimoRetiro (fecha) 
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldoCta}")
        else:
            print("fondos insuficientes o cantidad invalida.")

      def retirar(self, cantidad, fecha):
        if 0 < cantidad <= self.__saldoCta:
            self.__saldoCta -= cantidad 
            self.set_ultimoRetiro(fecha)
            print(f"Transferecia exitosa. Nuevo saldo: {self.__saldoCta}")
        else:
            print("Fondos insufiente o cantidad invalida.")
        
    def transferir(self, cuentaDestino, cantidad, fecha):
        if 0 < cantidad <= self.__saldoCta:
            self.__saldoCta -= cantidad 
            cuentaDestino.consignar(cantidad, fecha)
            self.set_ultimoRetiro(fecha)
            print(f"Transferecia exitosa. Nuevo saldo: {self.__saldoCta}")
        else:
            print("Fondos insufiente o cantidad invalida.")
        
# Menu de opciones
def mostrar_menu():
    print("\n--- Menu de opciones ---")
    print("1. Apertura de cuenta")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Transferir")
    print("5.  salir")
def main (:
     cuentas = {}
    
    while True:
        mostrar_menu()
        opcion = input ("Seleccione una opcion: ")

        if opcion == "1":
            numeroCta = input("Numero de cuenta: ")
            nombreCliente = input("Nombre del cliente : ")
            fechaApertura = input("Fecha de apertura (DD/MM/AAAA): ")
            nueva_cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura)
            cuentas[numeroCta] = nueva_cuenta
            print("Cuenta creada exitosamente.")

        elif opcion == "2":
            numeroCta = input ("Numero de cuentas: ")
            if numeroCta in cuentas:
                Cantidad = float (input("Cantidad a retirar: ")
                fecha = input("Fecha de retiro (DD/MM/AAAA): ")
                
            
    

          

        

        


'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, fechaAperturapertura, saldoCta = 0.0, ultimoRetiro = None, ultimaConsignacion = None):
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
            self.set_ultimoConsignacion(fecha) 
            print(f"consignacion exitoso. Nuevo saldo: {self.__saldoCta}")
        else:
            print("fondos insuficientes o cantidad invalida.")

    def retirar(self, cantidad, fecha):
        if 0 < cantidad <= self.__saldoCta:
            self.__saldoCta -= cantidad
            self.set_ultimoRetiro(fecha)
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldoCta}")
        else:
            print("Fondos insuficientes o cantidad inválida.")
        
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
def main ():
     cuentas = {}
    
     while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeroCta = input("Número de cuenta: ")
            nombreCliente = input("Nombre del cliente: ")
            fechaApertura = input("Fecha de apertura (DD/MM/AAAA): ")
            nueva_cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura)
            cuentas[numeroCta] = nueva_cuenta
            print("Cuenta creada exitosamente.")

        elif opcion == "2":
            numeroCta = input("Número de cuenta: ")
            if numeroCta in cuentas:
                cantidad = float(input("Cantidad a consignar: "))
                fecha = input("Fecha de consignación (DD/MM/AAAA): ")
                cuentas[numeroCta].consignar(cantidad, fecha)
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == "3":
            numeroCta = input("Número de cuenta: ")
            if numeroCta in cuentas:
                cantidad = float(input("Cantidad a retirar: "))
                fecha = input("Fecha de retiro (DD/MM/AAAA): ")
                cuentas[numeroCta].retirar(cantidad, fecha)
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == "4":
            numeroCtaOrigen = input("Número de cuenta origen: ")
            numeroCtaDestino = input("Número de cuenta destino: ")
            if numeroCtaOrigen in cuentas and numeroCtaDestino in cuentas:
                cantidad = float(input("Cantidad a transferir: "))
                fecha = input("Fecha de transferencia (DD/MM/AAAA): ")
                cuentas[numeroCtaOrigen].transferir(cuentas[numeroCtaDestino], cantidad, fecha)
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

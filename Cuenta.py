import random 
class Cuenta:
    def __init__(self,titular,edad,saldo=0):
        self.__numeroCuenta = self.generaNumeroCuenta()
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo

    def generaNumeroCuenta(self):
        longitud = 10
        NumeroCuenta = "C"
        for i in range(0,longitud):
            NumeroCuenta +=  str(random.randint(0,9))
            
        return NumeroCuenta    
            
    #GETTERS    
    def getNumeroCuenta(self):
        return self.__numeroCuenta
    
    def getTitular(self):
        return self.__titular    

    def getEdad(self):
        return self.__edad    
    
    def getSaldo(self):
        return self.__saldo    
    
    #SETTERS
    def setNumeroCuenta(self,numeroCuenta):
        self.__numeroCuenta = numeroCuenta
        
    def setTitular(self,Titular):
        self.__titular = Titular  
    
    def setEdad(self,edad):
        self.__edad = edad      
        
    def setSaldo(self,Saldo):
        self.__saldo = Saldo    
        
        
    def retiraEfectivo(self,Monto):
        self.__saldo =- Monto
        
    def agregaEfectivo(self,Monto):
        self.__saldo =+ Monto    
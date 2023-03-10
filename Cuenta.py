class Cuenta:
    def __init__(self,numeroCuenta,titular,edad,saldo=0):
        self.__numeroCuenta = numeroCuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo
    #GETTERS    
    def getNumeroCuenta(self):
        return self.__numeroCuenta
    
    def getTitular(self):
        return self.__titular    

    def getEdad(self):
        return self.__titular    
    
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
from tkinter import Tk,Frame,Label,Entry,Button,Grid
from Cuenta import *
from Prompt import *
from DepositaACuenta import *

def salir():
    ventana.quit()

def guardarDinero():
    miPrompt = Prompt(ventana)
    miPrompt.mostrarPrompt("Guardar dinero","Ingresa la cantidad a guardar","Depositar")
    dineroahorrar = miPrompt.getText()
    miPrompt.cierraPrompt()
    miCuenta.agregaEfectivo(float(dineroahorrar))
    actualizaDatos()

def retirarDinero():    
    miPrompt = Prompt(ventana)
    miPrompt.mostrarPrompt("Retirar dinero","Ingresa la cantidad a retirar","Retirar")
    dineroretirar = miPrompt.getText()
    miPrompt.cierraPrompt()
    miCuenta.retiraEfectivo(float(dineroretirar))
    actualizaDatos()

def actualizaDatos():
    LblSaldoTotal.config(text=miCuenta.getSaldo())

def depositoACuenta():
    depositar = DepositoACuenta(ventana,"Numero cuenta:","Monto a depositar:")  
    depositar.mostrarPrompt("Deposito")
    CuentaADepositar = depositar.getNumeroCuenta()  
    MontoDepo = depositar.getMontoDepositar()
    depositar.cierraPrompt()
    miCuenta.retiraEfectivo(float(MontoDepo))
    actualizaDatos()
    #print("Numero cuenta:",CuentaADepositar,"\nMonto:",MontoDepo)
    
miCuenta = Cuenta("Diego MP",20,235)
ventana = Tk()
ventana.title("Bienvenido")
ventana.resizable(False,False)
ventana.geometry("320x280")


#Aqui se pondra la info de la cuenta (numero cuenta,titular, saldo)
FrameInfoCuenta = Frame(ventana,bg="#0074D9")
FrameInfoCuenta.pack(expand=True,fill="both")
#Aqui van los botones con las opciones disponibles
FrameBtnOperations = Frame(ventana,bg="#2E86C1")
FrameBtnOperations.pack(expand=True,fill="both")

LblCuenta = Label(FrameInfoCuenta,text="Numero cuenta:")
LblNumCuenta = Label(FrameInfoCuenta,text="[numero]")
LblCuenta.grid(row=0,column=0)
LblNumCuenta.grid(row=0,column=1)

LblTitu = Label(FrameInfoCuenta,text="Titular:")
LblNameTitu = Label(FrameInfoCuenta,text="[nombre]")
LblTitu.grid(row=1,column=0)
LblNameTitu.grid(row=1,column=1)

LblEdad = Label(FrameInfoCuenta,text="Edad:")
LblNumEdad = Label(FrameInfoCuenta,text="[edad]")
LblEdad.grid(row=2,column=0)
LblNumEdad.grid(row=2,column=1)

LblSaldo = Label(FrameInfoCuenta,text="Saldo:")
LblSaldoTotal = Label(FrameInfoCuenta,text="[money]")
LblSaldo.grid(row=3,column=0)
LblSaldoTotal.grid(row=3,column=1)

#Botones con las opciones
btnIngresarEfectivo = Button(FrameBtnOperations,text="Ahorrar",command=guardarDinero)
btnRetirarEfectivo = Button(FrameBtnOperations,text="Retirar",command=retirarDinero)
btnDepositoACuenta = Button(FrameBtnOperations,text="Depositar a otra cuenta",command=depositoACuenta)
btnSalir = Button(FrameBtnOperations,text="Salir",command=salir)

btnIngresarEfectivo.grid(row=0,column=0)
btnRetirarEfectivo.grid(row=0,column=1)
btnDepositoACuenta.grid(row=0,column=2)
btnSalir.grid(row=2,column=1)

LblNumCuenta.config(text=miCuenta.getNumeroCuenta())
LblNameTitu.config(text=miCuenta.getTitular())
LblNumEdad.configure(text=miCuenta.getEdad())
LblSaldoTotal.config(text=miCuenta.getSaldo())

#mostramos la venta
ventana.mainloop()
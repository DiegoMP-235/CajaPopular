from tkinter import Tk,Frame,Label,Entry,Button,Grid,messagebox
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
    messagebox.showinfo("Todo salio bien","Operacion exitosa!")
    actualizaDatos()

def retirarDinero():    
    miPrompt = Prompt(ventana)
    miPrompt.mostrarPrompt("Retirar dinero","Ingresa la cantidad a retirar","Retirar")
    dineroretirar = miPrompt.getText()
    miPrompt.cierraPrompt()
    miCuenta.retiraEfectivo(float(dineroretirar))
    messagebox.showinfo("Todo salio bien","Operacion exitosa!")
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
    messagebox.showinfo("Todo salio bien","Operacion exitosa!")
    actualizaDatos()
    #print("Numero cuenta:",CuentaADepositar,"\nMonto:",MontoDepo)

#Colores
Color1 = "#9A9A9A"
Color2 = "#FFA07A"
PaddingX=5
PaddingY=5
    
miCuenta = Cuenta("Diego MP",20,235)
ventana = Tk()
ventana.title("Bienvenido")
ventana.resizable(False,False)
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"320x280+{(ancho_pantalla//2)-150}+{(alto_pantalla//2)-200}")
#ventana.geometry("320x280+500+100")

#Aqui se pondra la info de la cuenta (numero cuenta,titular, saldo)
ContainLabels = Frame(ventana,bg=Color1)
ContainLabels.pack(expand=True,fill="both")

LabelTittle = Label(ContainLabels,text="Mi cuenta",font=("Arial", 15, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle.pack()

FrameInfoCuenta = Frame(ContainLabels,bg=Color1)
FrameInfoCuenta.pack(padx=PaddingX,pady=PaddingY)


#Aqui van los botones con las opciones disponibles
FrameBTNSection = Frame(ventana,bg=Color2)
FrameBTNSection.pack(expand=True,fill="both")

FrameBtnOperations = Frame(FrameBTNSection,bg=Color2)
FrameBtnOperations.pack()

LblCuenta = Label(FrameInfoCuenta,text="Numero cuenta:")
LblNumCuenta = Label(FrameInfoCuenta,text="[numero]")
LblCuenta.grid(row=0,column=0,padx=PaddingX,pady=PaddingY)
LblNumCuenta.grid(row=0,column=1,padx=PaddingX,pady=PaddingY)

LblTitu = Label(FrameInfoCuenta,text="Titular:")
LblNameTitu = Label(FrameInfoCuenta,text="[nombre]")
LblTitu.grid(row=1,column=0,padx=PaddingX,pady=PaddingY)
LblNameTitu.grid(row=1,column=1,padx=PaddingX,pady=PaddingY)

LblEdad = Label(FrameInfoCuenta,text="Edad:")
LblNumEdad = Label(FrameInfoCuenta,text="[edad]")
LblEdad.grid(row=2,column=0,padx=PaddingX,pady=PaddingY)
LblNumEdad.grid(row=2,column=1,padx=PaddingX,pady=PaddingY)

LblSaldo = Label(FrameInfoCuenta,text="Saldo:")
LblSaldoTotal = Label(FrameInfoCuenta,text="[money]")
LblSaldo.grid(row=3,column=0,padx=PaddingX,pady=PaddingY)
LblSaldoTotal.grid(row=3,column=1,padx=PaddingX,pady=PaddingY)

#Botones con las opciones
btnIngresarEfectivo = Button(FrameBtnOperations,text="Ahorrar",command=guardarDinero)
btnRetirarEfectivo = Button(FrameBtnOperations,text="Retirar",command=retirarDinero)
btnDepositoACuenta = Button(FrameBtnOperations,text="Depositar a otra cuenta",command=depositoACuenta)
btnSalir = Button(FrameBtnOperations,text="Salir",command=salir)

btnIngresarEfectivo.grid(row=0,column=0,padx=PaddingX,pady=PaddingY)
btnRetirarEfectivo.grid(row=0,column=1,padx=PaddingX,pady=PaddingY)
btnDepositoACuenta.grid(row=0,column=2,padx=PaddingX,pady=PaddingY)
btnSalir.grid(row=3,column=0,columnspan=3,sticky="NSEW",padx=PaddingX,pady=PaddingY)

LblNumCuenta.config(text=miCuenta.getNumeroCuenta())
LblNameTitu.config(text=miCuenta.getTitular())
LblNumEdad.configure(text=miCuenta.getEdad())
LblSaldoTotal.config(text=miCuenta.getSaldo())

#mostramos la venta
ventana.mainloop()
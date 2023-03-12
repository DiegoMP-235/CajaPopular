from tkinter import Tk,Label,Entry,Button,Toplevel
class Prompt:
    
    def __init__(self,master):
        self.__nodoPadre = master
        self.__ventana = self.__creaVentana(master)
        self.__labelTitle = self.__creaLabel()
        self.__caja_texto = self.__creaCajaTexto()
        self.__btnGuardar = self.__creaBotonGuardar()
        self.__value = ""
        
    def __creaVentana(self,NodoPadre):#Instancia la ventana
        #ventana = Tk()
        ventana = Toplevel(NodoPadre)
        ventana.title("Entrada")
        ventana.geometry("220x85")
        ventana.resizable(False,False)
        return ventana
    
    def __creaLabel(self):
        etiqueta=Label(self.__ventana,text="Introduzca su texto:")
        etiqueta.pack()  
        return etiqueta
        
    def __creaCajaTexto(self):#Instancia la caja de texto del prompt
        caja_texto = Entry(self.__ventana)
        caja_texto.pack(expand=True) 
        return caja_texto
    
    def __guardar_texto(self): #Guarda el texto ingresado
        texto = self.__caja_texto.get()
        self.__value = texto
        self.__nodoPadre.focus_set()
        self.__ventana.quit() 

        
    def cierraPrompt(self):
        self.__ventana.destroy()
        
    def getText(self):#Retorna el texto guardado
        return self.__value
        
    def __creaBotonGuardar(self):#Instancia el boton para guardar el texto
        boton_guardar = Button(self.__ventana,text="Guardar",command=self.__guardar_texto)    
        boton_guardar.pack()     
        return boton_guardar
        
    #El 1er arg. corresponde a el titulo
    #El 2do arg. corresponde a el texto/indicacion
    #El 3er arg. corresponde a el texto del boton
    def mostrarPrompt(self, *args):
        if (len(args)==0): #Se muestra el prompt con los valores por defecto
            self.__ventana.mainloop()
        elif(len(args) == 1 ): #El primer argumento corresponde a el titulo del prompt   
            self.__ventana.title(args[0])
            self.__ventana.mainloop()      
        elif(len(args) == 2):#El segiundo argumento corresponde a el texto  
            self.__ventana.title(args[0])
            self.__labelTitle.config(text=args[1])
            self.__ventana.mainloop() 
        elif(len(args) == 3):   #El tercer argumento corresponde a el texto del boton 
            self.__ventana.title(args[0])
            self.__labelTitle.config(text=args[1])
            self.__btnGuardar.config(text=args[2])
            self.__ventana.mainloop() 
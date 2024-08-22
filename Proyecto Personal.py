#PROYECTO PERSONAL 1

from tkinter import *
from tkinter import messagebox
import sqlite3

#------------------------------FUNCIONES Y VARIABLES DEL PROGRAMA--------------------------------------------------------------------------



#------------------------------FUNCIONES Y VARIABLES DEL PROGRAMA--------------------------------------------------------------------------

#--------------------------------------------------------INTERFAZ--------------------------------------------------------------------------

#TIPO DE LETRA Y COLORES

BLANCO='#FFFFFF'
NEGRO='#000000'
AZUL='#2980B9'
ROJO='#E74C3C'
VERDE='#2ECC71'

fontCentury=('Century Gothic', '12')
fontArial=('Arial','10')
fontBookman=('Bookman Old Style','14')

#TIPO DE LETRA Y COLORES

def ventanaP():
    global ventana1
    ventana1=Tk()
    ventana1.config(bg=NEGRO, bd=7)
    ventana1.iconbitmap('icono.ico')
    ventana1.title('BASE DE DATOS')
    ventana1.resizable(0,0)
    
    def habilitarMasLicensia():
        messagebox.showinfo('BASE DE DATOS', message='PROGRAMA CREADO POR JESUS QUINTANA -JESUSQ-')
        
    def habilitarArhivoSalir():
        ventana1.destroy()
        
    def habilitarArhivoNuevo():
        try:
            baseDeDatos=sqlite3.connect('Base de Datos')
            cursorBDD=baseDeDatos.cursor()   
            cursorBDD.execute('CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CEDULA VARCHAR(10) UNIQUE, TELEFONO VARCHAR(12), CORREO VARCHAR(50), PESO VARCHAR(5), TALLA VARCHAR(4))')
    
            baseDeDatos.commit()
            baseDeDatos.close()
        except:
            messagebox.showinfo('Base de Datos', 'La base de datos ya existe')
    
    menuVentana1=Menu(ventana1)
    ventana1.config(menu=menuVentana1)
    
    archivoMenu=Menu(menuVentana1, tearoff=0)
    menuVentana1.add_cascade(label='Archivo', menu=archivoMenu)
    archivoMenu.add_command(label='Nuevo', command=habilitarArhivoNuevo)
    '''archivoMenu.add_command(label='Guardar')'''
    archivoMenu.add_separator()
    archivoMenu.add_command(label='Salir', command=habilitarArhivoSalir)
    
    '''edicionMenu=Menu(menuVentana1, tearoff=0)
    menuVentana1.add_cascade(label='Edición', menu=edicionMenu)
    edicionMenu.add_command(label='Crear')
    edicionMenu.add_command(label='Ver')
    edicionMenu.add_command(label='Actualizar')
    edicionMenu.add_command(label='Borrar')'''
    
    masMenu=Menu(menuVentana1, tearoff=0)
    menuVentana1.add_cascade(label='Más', menu=masMenu)
    masMenu.add_command(label='Licensía', command=habilitarMasLicensia)
    
    frame1=Frame(ventana1)
    frame1.grid(column=0, row=0)
    frame1.config(width=300, height=300)
    
    titulo1Ventana1=Label(frame1, text='BASE DE DATOS', font=fontBookman)
    titulo1Ventana1.place(x=70, y=110)
    
    botonVentana1=Button(frame1, text='Crear', font=fontBookman,width=7, command=ventana2)
    botonVentana1.place(x=105, y=150)
    
    ventana1.mainloop()

#----------------------------------------------------------VENTANA 2-----------------------------------------------------------------------------------------
#----------------------------------------------------------VENTANA 2-----------------------------------------------------------------------------------------
    
def ventana2():
    ventana1.withdraw()
    
    #-------------------CREACION DE LA BASE DE DATOS-----------------------------------------------
    
    try:
    
        baseDeDatos=sqlite3.connect('Base de Datos')
        cursorBDD=baseDeDatos.cursor()   
        cursorBDD.execute('CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CEDULA VARCHAR(10) UNIQUE, TELEFONO VARCHAR(12), CORREO VARCHAR(50), PESO VARCHAR(5), TALLA VARCHAR(4))')
    
        baseDeDatos.commit()
        baseDeDatos.close()
        
    except:
        messagebox.showinfo('Base de Datos', 'La base de datos ya existe')
    
    #-------------------CREACION DE LA BASE DE DATOS-----------------------------------------------
    
    global ventana2
    
    #VARIBALES Y FUNCIONES SIN REGITRAR
    
    def longitudCedula(longitudCed):
        if len(longitudCed)<=10:
            return True
        elif longitudCed=='':
            return True
        else:
            return False
            
    def longitudTelefono(longitudTelefon):
        if len(longitudTelefon)<=12:
            return True
        elif longitudTelefon=='':
            return True
        else:
            return False
            
    def longitudPeso(longitudPe):
        if len(longitudPe)<=5:
            return True
        elif longitudPe=='':
            return True
        else:
            return False
            
    def longitudTalla(longitudTal):
        if len(longitudTal)<=4:
            return True
        elif longitudTal=='':
            return True
        else:
            return False
        
    def idDigitos(idDigito):
        if idDigito.isdigit():
            return True
        elif idDigito=='':
            return True
        else:
            return False
    
    #VARIBALES Y FUNCIONES SIN REGITRAR
    
    ventana2=Toplevel(ventana1)
    ventana2.config(bg=NEGRO, bd=7)
    ventana2.iconbitmap('icono.ico')
    ventana2.title('BASE DE DATOS')
    ventana2.resizable(0,0)
    
    #VARIABLES PARA REGITRAR // DENTRO DE LA INTERFAZ
    
    longitudCedul=ventana2.register(longitudCedula)
    longitudTelef=ventana2.register(longitudTelefono)
    longitudPes=ventana2.register(longitudPeso)
    longitudTall=ventana2.register(longitudTalla)
    idDigit=ventana2.register(idDigitos)
    
    IDtext=StringVar()
    nombreText=StringVar()
    apellidoText=StringVar()
    cedulaText=StringVar()
    telefonoText=StringVar()
    correoText=StringVar()
    pesoText=StringVar()
    tallaText=StringVar()
    
    def buscarBDDver():
        
        IDtexto=int(IDtext.get())
        
        IDentrada.delete(0, END)
        nombreEntrada.config(state='normal')
        nombreEntrada.delete(0, END)
        apellidoEntrada.config(state='normal')
        apellidoEntrada.delete(0, END)
        cedulaEntrada.config(state='normal')
        cedulaEntrada.delete(0, END)
        telefonoEntrada.config(state='normal')
        telefonoEntrada.delete(0, END)
        correoEntrada.config(state='normal')
        correoEntrada.delete(0, END)
        pesoEntrada.config(state='normal')
        pesoEntrada.delete(0, END)
        tallaEntrada.config(state='normal')
        tallaEntrada.delete(0, END)
        
        try:
            baseDeDatos=sqlite3.connect('Base de Datos')
            cursorBDD=baseDeDatos.cursor()
            cursorBDD.execute('SELECT * FROM PERSONAS')
        
            listaDatosVer=cursorBDD.fetchall()
            
            nombreEntrada.insert(END, (listaDatosVer[IDtexto-1])[1])
            nombreEntrada.config(state='disabled')
            apellidoEntrada.insert(END, (listaDatosVer[IDtexto-1])[2])
            apellidoEntrada.config(state='disabled')            
            cedulaEntrada.insert(END, (listaDatosVer[IDtexto-1])[3])
            cedulaEntrada.config(state='disabled')            
            telefonoEntrada.insert(END, (listaDatosVer[IDtexto-1])[4])
            telefonoEntrada.config(state='disabled')           
            correoEntrada.insert(END, (listaDatosVer[IDtexto-1])[5])
            correoEntrada.config(state='disabled')        
            pesoEntrada.insert(END, (listaDatosVer[IDtexto-1])[6])
            pesoEntrada.config(state='disabled')            
            tallaEntrada.insert(END, (listaDatosVer[IDtexto-1])[7])
            tallaEntrada.config(state='disabled')
        
        except:
            messagebox.showinfo('Base de Datos','Introduzca un ID')
            
    def buscarBDDborrar():
        print('BORRANDO..')
    
    def buscarBDDactualizar():
        print('ACTUALIZANDO...')
    
    def habilitarArhivoNuevo():
        try:
            baseDeDatos=sqlite3.connect('Base de Datos')
            cursorBDD=baseDeDatos.cursor()   
            cursorBDD.execute('CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CEDULA VARCHAR(10) UNIQUE, TELEFONO VARCHAR(12), CORREO VARCHAR(50), PESO VARCHAR(5), TALLA VARCHAR(4))')
    
            baseDeDatos.commit()
            baseDeDatos.close()
            
        except:
            messagebox.showinfo('Base de Datos', 'La base de datos ya existe')
    
    def borrarTodo():
        IDentrada.delete(0, END)
        nombreEntrada.delete(0, END)
        apellidoEntrada.delete(0, END)
        cedulaEntrada.delete(0, END)
        telefonoEntrada.delete(0, END)
        correoEntrada.delete(0, END)
        pesoEntrada.delete(0, END)
        tallaEntrada.delete(0, END)
        
    def habilitarEdicionVer():
        IDentrada.config(state='normal')
        nombreEntrada.config(state='disabled')
        apellidoEntrada.config(state='disabled')
        cedulaEntrada.config(state='disabled')
        telefonoEntrada.config(state='disabled')
        correoEntrada.config(state='disabled')
        pesoEntrada.config(state='disabled')
        tallaEntrada.config(state='disabled')
        botonBuscarActualizar.config(state='normal', command=buscarBDDver)
    
    def habilitarEdicionInsertar():
        IDentrada.config(state='disabled')
        nombreEntrada.config(state='normal')
        apellidoEntrada.config(state='normal')
        cedulaEntrada.config(state='normal')
        telefonoEntrada.config(state='normal')
        correoEntrada.config(state='normal')
        pesoEntrada.config(state='normal')
        tallaEntrada.config(state='normal')
        botonBuscarActualizar.config(state='disabled')
        
        IDentrada.delete(0, END)
        nombreEntrada.delete(0, END)
        apellidoEntrada.delete(0, END)
        cedulaEntrada.delete(0, END)
        telefonoEntrada.delete(0, END)
        correoEntrada.delete(0, END)
        pesoEntrada.delete(0, END)
        tallaEntrada.delete(0, END)
        
    def habilitarEdicionActualizar():
        IDentrada.config(state='normal')
        nombreEntrada.config(state='disabled')
        apellidoEntrada.config(state='disabled')
        cedulaEntrada.config(state='disabled')
        telefonoEntrada.config(state='disabled')
        correoEntrada.config(state='disabled')
        pesoEntrada.config(state='disabled')
        tallaEntrada.config(state='disabled')
        botonBuscarActualizar.config(state='normal', command=buscarBDDactualizar)
        
    def habilitarEdicionBorrar():
        IDentrada.config(state='normal')
        nombreEntrada.config(state='disabled')
        apellidoEntrada.config(state='disabled')
        cedulaEntrada.config(state='disabled')
        telefonoEntrada.config(state='disabled')
        correoEntrada.config(state='disabled')
        pesoEntrada.config(state='disabled')
        tallaEntrada.config(state='disabled')
        botonBuscarActualizar.config(state='normal', command=buscarBDDborrar)
        
    def habilitarMasLicensia():
        messagebox.showinfo('BASE DE DATOS', message='PROGRAMA CREADO POR JESUS QUINTANA -JESUSQ-')
        
    def habilitarArhivoSalir():
        ventana1.destroy()
    
    def habilitarBotonEnviar():
        nombreTexto=nombreText.get()
        apellidoTexto=apellidoText.get()
        cedulaTexto=cedulaText.get()
        telefonoTexto=telefonoText.get()
        correoTexto=correoText.get()
        pesoTexto=pesoText.get()
        tallaTexto=tallaText.get()
        
        if nombreTexto=='' or apellidoTexto=='' or cedulaTexto=='' or telefonoTexto=='' or correoTexto=='' or pesoTexto=='' or tallaTexto=='':
            messagebox.showinfo('BASE DE DATOS', message='Rellena todos los campos')
            
        else:
            
            baseDeDatos=sqlite3.connect('Base de Datos')
            cursorBDD=baseDeDatos.cursor() 
            
            cursorBDD.execute("INSERT INTO PERSONAS VALUES(NULL, '"+nombreTexto+ 
            "','"+ apellidoTexto + 
            "','"+ cedulaTexto + 
            "','"+ telefonoTexto + 
            "','"+ correoTexto + 
            "','"+ pesoTexto + 
            "','"+ tallaTexto + "')")
            
            nombreEntrada.delete(0, END)
            apellidoEntrada.delete(0, END)
            cedulaEntrada.delete(0, END)
            telefonoEntrada.delete(0, END)
            correoEntrada.delete(0, END)
            pesoEntrada.delete(0, END)
            tallaEntrada.delete(0, END)
            
            messagebox.showinfo('Base de Datos', 'Datos Insertado con éxito')
            
            
            baseDeDatos.commit()
            baseDeDatos.close()
            
   
    #VARIABLES PARA REGITRAR // DENTRO DE LA INTERFAZ--------------------------------------------------------------------------

    menuVentana2=Menu()
    ventana2.config(menu=menuVentana2)
    
    archivoMenuV2=Menu(menuVentana2, tearoff=0)
    menuVentana2.add_cascade(label='Arhivo', menu=archivoMenuV2)
    archivoMenuV2.add_command(label='Nuevo', command=habilitarArhivoNuevo)
    archivoMenuV2.add_separator()
    archivoMenuV2.add_command(label='Salir', command=habilitarArhivoSalir)
    
    edicionMenuV2=Menu(menuVentana2, tearoff=0)
    menuVentana2.add_cascade(label='Edición', menu=edicionMenuV2)
    edicionMenuV2.add_command(label='Insertar', command=habilitarEdicionInsertar)
    edicionMenuV2.add_command(label='Ver', command=habilitarEdicionVer)
    edicionMenuV2.add_command(label='Actualizar', command=habilitarEdicionActualizar)
    edicionMenuV2.add_command(label='Borrar', command=habilitarEdicionBorrar)
    
    masMenuV2=Menu(menuVentana2, tearoff=0)
    menuVentana2.add_cascade(label='Más', menu=masMenuV2)
    masMenuV2.add_command(label='Licensia', command=habilitarMasLicensia)
    
    frame2=Frame(ventana2, width=350, height=550)
    frame2.grid(column=0, row=0)
    frame2.grid_propagate(0)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)
    frame2.rowconfigure(2, weight=1)
    frame2.rowconfigure(3, weight=1)
    frame2.rowconfigure(4, weight=1)
    frame2.rowconfigure(5, weight=1)
    frame2.rowconfigure(6, weight=1)
    frame2.rowconfigure(7, weight=1)
    frame2.rowconfigure(8, weight=1)
    
    ID=Label(frame2, text='ID', font=fontBookman)
    ID.grid(column=0, row=0, padx=7, pady=15)
    IDentrada=Entry(frame2, state='disabled', justify='center', validate='key', validatecommand=(idDigit, '%P'), textvariable=IDtext)
    IDentrada.grid(column=1, row=0, padx=5, pady=15)
    
    nombre=Label(frame2, text='Nombres', font=fontBookman)
    nombre.grid(column=0, row=1, padx=7, pady=15)
    nombreEntrada=Entry(frame2, justify='center', textvariable=nombreText)
    nombreEntrada.grid(column=1, row=1, padx=10, pady=15)
    
    apellido=Label(frame2, text='Apellidos', font=fontBookman)
    apellido.grid(column=0, row=2, padx=7, pady=15)
    apellidoEntrada=Entry(frame2, justify='center', textvariable=apellidoText)
    apellidoEntrada.grid(column=1, row=2, padx=5, pady=15)
    
    cedula=Label(frame2, text='Cedula', font=fontBookman)
    cedula.grid(column=0, row=3, padx=7, pady=15)
    cedulaEntrada=Entry(frame2, validate='key', validatecommand=(longitudCedul, '%P'), justify='center', textvariable=cedulaText)
    cedulaEntrada.grid(column=1, row=3, padx=5, pady=15)
    
    telefono=Label(frame2, text='Telefono', font=fontBookman)
    telefono.grid(column=0, row=4, padx=7, pady=15)
    telefonoEntrada=Entry(frame2, validate='key', validatecommand=(longitudTelef, '%P'), justify='center', textvariable=telefonoText)
    telefonoEntrada.grid(column=1, row=4, padx=5, pady=15)
    
    correo=Label(frame2, text='Correo', font=fontBookman)
    correo.grid(column=0, row=5, padx=7, pady=15)
    correoEntrada=Entry(frame2, justify='center', textvariable=correoText)
    correoEntrada.grid(column=1, row=5, padx=5, pady=15)
    
    peso=Label(frame2, text='Peso', font=fontBookman)
    peso.grid(column=0, row=6, padx=7, pady=15)
    pesoEntrada=Entry(frame2, validate='key', validatecommand=(longitudPes, '%P'), justify='center', textvariable=pesoText)
    pesoEntrada.grid(column=1, row=6, padx=5, pady=15)
    
    talla=Label(frame2, text='Talla', font=fontBookman)
    talla.grid(column=0, row=7, padx=7, pady=15)
    tallaEntrada=Entry(frame2, validate='key', validatecommand=(longitudTall, '%P'), justify='center', textvariable=tallaText)
    tallaEntrada.grid(column=1, row=7, padx=5, pady=15)
    
    botonBorrar=Button(frame2, text='Borrar', font=fontBookman, command=borrarTodo)
    botonBorrar.grid(column=0, row=8, pady=15, sticky='E')
    
    botonEnviar=Button(frame2, text='Enviar', font=fontBookman, command=habilitarBotonEnviar)
    botonEnviar.grid(column=1, row=8, pady=15)
    
    botonBuscarActualizar=Button(frame2, text='Buscar', font=fontBookman, state='disabled')
    botonBuscarActualizar.grid(column=2, row=0, padx=7)
    
    ventana2.mainloop()
#--------------------------------------------------------INTERFAZ--------------------------------------------------------------------------

ventanaP()
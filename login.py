import tkinter
from tkinter import*
from tkinter import messagebox
def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("500x580")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("FI.ico")

    Label(pantalla1, text="Por favo ingrese su usuario y contraseña").pack()
    Label(pantalla, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify
pantalla=Tk()
pantalla.geometry("500x580")
pantalla.title("Binevenidos")
pantalla.iconbitmap("FI.ico")

image=PhotoImage(fil="TEC.gif")
image=image.subsample(2,4)
label=Label(image=image)
label.pack()

Label(text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("calibri",18)).pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()

Button(text="Iniciar sesion", height="3", width="50",command=inicio_sesion).pack()
Label(text="").pack()
Button(text="Registrarse", height="3", width="50").pack()
pantalla.mainloop()

nombreusuario_verefy=StringVar()
contrasenausuario_verify=StringVar()

global nombre_usuario_entry
global contrasena_usuario_entry

Label(pantalla1, text="Usuario").pack()
nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
nombre_usuario_entry.pack()
Label(pantalla1).pack()


Label(pantalla1, text="Contraseña").pack()
contrasenausuario_verify = Entry(pantalla1, textvariable=contrasenausuario_verify)
contrasenausuario_verify.pack()
Label(pantalla1).pack()

Button(pantalla1, text="Iniciar Sesion").pack()


menu_pantalla()

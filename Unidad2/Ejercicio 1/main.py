from email import email
from Manejadoremail import Manejadoremail

if __name__ == "__main__" :
    unmail = email()
    """nombre = input("ingrese su nombre: ")
    uncorreo = input("Igrese su correo: ")
    contra = input("ingrese su contraseña: ")
    unmail.crearcuenta(uncorreo,nombre,contra)
    print("Estimado {}, te enviaremos tus mensajes ala direccion de correo:{}" .format(nombre,uncorreo))
    contra2=input("Ingrese su contraseña actual: ")
    unmail.cambiarcontraseña(contra2)
    otrocorreo = input("Ingrese un correo: ")
    contra3 = input("ingrese su contraseña")
    otrocorreo = otrocorreo.split("@")
    idcuenta = otrocorreo[0]
    otrocorreo[1] = otrocorreo[1].split(".")
    dominio = otrocorreo[0]
    tipodominio = otrocorreo[1]
    nuevocorreo = email(idcuenta,dominio,tipodominio,contra3)"""
    unalista = Manejadoremail()
    unalista.cargaremial()


class email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio= ""
    __contraseña = ""
    def __init__(self, idcuenta="", dominio="", tipodominio="", contraseña=""):
        self.__tipoDominio = tipodominio
        self.__dominio = dominio
        self.__idcuenta = idcuenta
        self.__contraseña = contraseña

    def getDominio(self):
        return self.__dominio

    def crearcuenta(self,uncorreo,contra,nombre):
        uncorreo = uncorreo.split("@")
        self.__idcuenta = uncorreo[0]
        uncorreo[1] = uncorreo[1].split(".")
        self.__dominio = uncorreo[0]
        self.__tipoDominio = uncorreo[1]


    def cambiarcontraseña (self,contra2):
        if contra2 == self.__contraseña:
            self.__contraseña = input("Ingrese nueva contraseña")
            print("Contraseña cambianda exitosamente!!!")
        else: print("contraseña incorrecta")


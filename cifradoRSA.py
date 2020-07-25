from random import sample
class cifradoRSA():

    def __init__(self):
        self.__n=0
        self.__z=0
        self.__k=0
        self.__p=0
        self.__q=0

    def setN(self,n):
        self.__n=n
    def getN(self):
        return self.__n
    def setZ(self,z):
        self.__z=z
    def getZ(self):
        return self.__z
    def setK(self,k):
        self.__k=k
    def getK(self):
        return self.__k
    def setP(self,p):
        self.__p=p
    def getP(self):
        return self.__p
    def setQ(self,q):
        self.__q=q
    def getQ(self):
        return self.__q


    def generarNumerosPrimos(self,inicio,final):
        numeros_primos=[]
        for i in range(inicio,final+1):
            contador=0
            for j in range(1,i+1):
                #un numero primo solo debe ser divisible por si mismo o por 1 
                if i%j==0:
                    contador=contador+1
            
            if contador==2:
                numeros_primos.append(i)
            
        return numeros_primos

    def obtenerNumerosPrimos(self):
        #se obtienen 2 numeros primos entre 1 y 400
        numeros=self.generarNumerosPrimos(1,400)
        num_primos_seleccionados=sample(numeros,2)
        return num_primos_seleccionados

    def obtenerNumeroCoprimo(self,numero_primo):
        numeros_primos=self.generarNumerosPrimos(1,numero_primo)
        len_numeros_primos=len(numeros_primos)
        posibles_coprimos=[]

        for i in range(0,len_numeros_primos):
            if numeros_primos[i]%numero_primo!=0:
                posibles_coprimos.append(numeros_primos[i])
        
        num_coprimo=sample(posibles_coprimos,1)
        return num_coprimo[0]

    def funcionPhi(self,p,q):
        z=(p-1)*(q-1)
        return z

    def clavePublica(self):
        numeros_primos=self.obtenerNumerosPrimos()
        self.setP(numeros_primos[0])
        self.setQ(numeros_primos[1])
        n=self.getP()*self.getQ()
        self.setN(n)
        z=self.funcionPhi(self.getP(),self.getQ())
        self.setZ(z)
        self.setK(self.obtenerNumeroCoprimo(self.getZ()))
        clave_publica=[self.getN(),self.getK()]
        return clave_publica


    def clavePrivada(self):
        x=False
        j=1
        k=self.getK()
        z=self.getZ()
        print(z)
        while x!=True:
            aux=k*j
            if aux%z==1:
                x=True
            else:
                j=j+1
        clave_privada=[self.getN(),j]
        return clave_privada

    def convertirMsgEnAscii(self,msg):
        len_msg=len(msg)
        value_msg_ascii=[]
        for i in range(0,len_msg):
            aux=msg[i]
            value_msg_ascii.append(ord(aux))
        
        return value_msg_ascii

    def cifrarMensaje(self,msg,clave_publica):
        msg_ascii=self.convertirMsgEnAscii(msg)
        msg_cifrado=[]
        for i in range(0,len(msg_ascii)):
            letra_cifrada=self.cifrarLetra(msg_ascii[i],clave_publica)
            msg_cifrado.append(letra_cifrada)
        
        return msg_cifrado
    def cifrarLetra(self,letra_ascii,clave_publica):
        n=clave_publica[0]
        k=clave_publica[1]
        e=(letra_ascii**k)%n
        return e

    def descifrarMensaje(self,msg_cifrado,clave_privada):
        letra_descifrada=""
        msg_descifrado=[]

        for i in range(0, len(msg_cifrado)):
            letra_descifrada=self.descifrarLetra(msg_cifrado[i],clave_privada)
            msg_descifrado.append(letra_descifrada)
        return msg_descifrado

    def descifrarLetra(self,letra_cifrada,clave_privada):
        letra_descifrada=(letra_cifrada**clave_privada[1])%clave_privada[0]
        return letra_descifrada
    
    def asciiALetras(self,msgAscii):
        equivalencias={"32":" ","65":"A","66":"B","67":"C","68":"D","69":"E","70":"F","71":"G","72":"H","73":"I","74":"J",
        "75":"K","76":"L","77":"M","78":"N","79":"O","80":"P","81":"Q","82":"R","83":"S","84":"T","85":"U",
        "86":"V","87":"W","88":"X","89":"Y","90":"Z","97":"a","98":"b","99":"c","100":"d","101":"e","102":"f",
        "103":"g","104":"h","105":"i","106":"j","107":"k","108":"l","109":"m","110":"n","111":"o","112":"p",
        "113":"q","114":"r","115":"s","116":"t","117":"u","118":"v","119":"w","120":"x","121":"y","122":"z"}
        mensaje=[]
        for i in range(0,len(msgAscii)):
            mensaje.append(equivalencias[str(msgAscii[i])])
        
        mensaje="".join(mensaje)
        return mensaje

obj=cifradoRSA()
clave_publica=obj.clavePublica()
clave_privada=obj.clavePrivada()
print(f"Clave publica:{clave_publica} \nClave privada:{clave_privada}")
msg="lirio acuatico mas que una plaga"
print("Mensaje:",msg)
msg_ascii=obj.convertirMsgEnAscii(msg)
print("Mensaje en ascii:",msg_ascii)
msg_cifrado=obj.cifrarMensaje(msg,clave_publica)
print("Mensaje cifrado:",msg_cifrado)
msg_descifrado=obj.descifrarMensaje(msg_cifrado,clave_privada)
print("Mensaje descifrado(valor ascii):",msg_descifrado)
msg_descifrado_letras=obj.asciiALetras(msg_descifrado)
print("Mensaje descifrado(letras):",msg_descifrado_letras)


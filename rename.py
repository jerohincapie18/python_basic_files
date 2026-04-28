import os
import glob
# Script para cambiar la extension de archivos
# Puede ser usado mas que todo para archivos corruptos, que bajaron mal la extension
#aqui simplemente liste la ruta, pero nunca toque nada de estas variables
ruta = "C:\\Users\\jeroh\\Desktop\\librosCyber"
archivos = os.listdir(ruta)

#globglob sirve para devolver los que tengan una extension especifica
lista_pdf_ = glob.glob("C:\\Users\\jeroh\\Desktop\\librosCyber\\*.pdf_") #aqui edita la ruta
#print(lista_pdf_)
#print(lista_pdf_[0])
#l1 = lista_pdf_[0]
#print(l1.split(".")[0])
# Aqui los transformo, de .pdf_ a .pdf (se puede meter en un try except para los errores)
for nombre in lista_pdf_:
   libro = nombre.split(".")[0]
   print(libro)
   os.rename(nombre, f"{libro}.pdf")

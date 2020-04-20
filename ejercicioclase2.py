from random import randint, uniform,random
class Alumno:
  
    def __init__(self, nombre, idp, notas):
        self.nombre = nombre
        self.idp = idp
        self.notas = []

    def __str__(self):
        cadena=str(self.idp)+" ,"+self.nombre+" ,"+ str(self.notas)
        return cadena

    def establecer_nota(self):
        x=0
        while x<=8 :
            self.notas.append(int(random()*10+1))
            x+=1


    def notaMedia(self,notas):
        suma=0
        for i in notas:
            suma+=i
        media=suma/len(notas)
        print("Media: "+ str(media))

alumno_a=Alumno("Iago", 2, [] )
alumno_b=Alumno("Laura", 5, [] )
alumno_c=Alumno("Africa", 1, [] )
alumno_a.establecer_nota()
alumno_b.establecer_nota()
alumno_c.establecer_nota()
print(alumno_a)
alumno_a.notaMedia(alumno_a.notas)
print(alumno_b)
alumno_b.notaMedia(alumno_b.notas)
print(alumno_c)
alumno_c.notaMedia(alumno_c.notas)


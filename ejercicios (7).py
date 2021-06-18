#Jean Carlos Santacruz - 8962275
#Alejandro Castañeda - 89644217

#pregunta 1
"""
def areaTriangulo (base,altura):

    areaTriangulo= (base*altura)/2
    return areaTriangulo

a1= (areaTriangulo(50,30))
print ("el area del triangilo es: " + (str(a1)) + " cm")

#pregunta 2
def notaFinal (parcial1, parcial2, taller, proyecto):
    notaFinal=(((parcial1+parcial2)/2)*0.5)+((taller)*0.3)+((proyecto)*0.2)
    return notaFinal
n1=notaFinal(3.5,3,4,3)
print ("su nota final es:"+(str(n1)))

#pregunta 3
def celsiusAFahrenheit (C):
    F= (C*1.8)+32
    return F
c1=celsiusAFahrenheit(30)
print (c1)
"""
"""            
#pregunta 5
def cambioDeMoneda():
    pesos = int(input("digite cantidad de dinero en pesos colombianos "))
    moneda= input("¿a que moneda quiere convertir dolares,yenes o euros? ")
    if moneda=="dolares":
        moneda= (pesos/3576.00)
        moneda= moneda-moneda*0.02
        print (str(pesos)+" pesos colombianos es igual a "+str(moneda)+" dolares")
        return moneda
    
    if moneda=="yenes":
        moneda= pesos/32.81
        moneda= moneda-moneda*0.02
        print (str(pesos)+" pesos colombianos es igual a "+str(moneda)+" yenes")
        return moneda
    
    if moneda=="euros":
        moneda= pesos/4276.97
        moneda= moneda-moneda*0.02
        print (str(pesos)+" pesos colombianos es igual a "+str(moneda)+" euros")
        return moneda

cambioDeMoneda()
"""








print("Bienvenido al programa..")
persona={"Nombre":"","Apellido":"","Edad":0,"Peso":0,"Altura":0,"Direccion":"","Telefono":""}
def cat_imc():
    "Obtencion de categoria de IMC"
    while imc < 18.5:
        cat = "Bajo peso"
        return cat
    while 18.5 < imc < 24.9:
        cat = "Peso normal"
        return cat
    while 25.0 < imc < 29.9:
        cat = "Sobre Peso"
        return cat
    while 30.0 < imc < 34.9:
        cat = "Obesidad tipo I"
        return cat
    while 35.0 < imc < 39.9:
        cat = "Obesidad tipo II"
        return cat
    while imc > 40:
        cat = "Obesidad tipo III"
        return cat
def imprimir():
    print("Informacion personal Nombre y Apellido: " + persona["Nombre"].upper() + " " + persona["Apellido"].upper() + "\nCategoria de IMC: " + cat_imc().upper() + " / Peso " + persona["Peso"] + " Kg / Altura: "+ persona["Altura"] + " metros\nEdad: " + persona["Edad"] + " años" "\nDireccion en: " + persona["Direccion"].upper() + " / Telefono: " + persona["Telefono"] )
for p in persona:
    persona[p] = input(f"ingrese su {p} : ") 
imc=round(float(persona["Peso"])/(float(persona["Altura"])**2),2)
persona["IMC"]=imc

cat_imc()
imprimir()

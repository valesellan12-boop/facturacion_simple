# ---- Funciones ------
def valida_resp():
    resp=input("Desea ingresar otro cliente s/n:").lower()
    while(resp!="s" and resp!="n"):
        print("Ingreso erroneo...")
        resp=input("Desea ingresar otro cliente s/n:").lower()
    return resp


def valida_precio():
    while True:
        try:
            precio=float(input("Ingrese el precio:"))
            while(precio<3):
                print("Error")
                precio=float(input("Ingrese el precio:"))
        except ValueError:
            print("error en tipo de dato")
            continue
        break
    return precio


def valida_cant():
    while True:
        try:
            cant=int(input("Ingrese la cantidad de productos:"))
            while(cant<1):
                print("Error")
                cant=int(input("Ingrese la cantidad de productos:"))
        except ValueError:
            print("error en tipo de dato")
            continue
        break
    return cant


def valida_fpago():
    resp=input("Cual es su forma de pago e. efectivo  t. tarjeta").lower()
    while(resp!="e" and resp!="t"):
        print("Ingreso erroneo...")
        resp=input("Cual es su forma de pago e. efectivo  t. tarjeta").lower()
    return resp


#Funcion con parametros
def calcular_total(cant,precio):
    subt=cant*precio
    imp=calc_impuesto(subt)
    total=subt+imp
    return total,imp,subt


def calc_impuesto(subt):
    iva=subt*0.15
    return iva


def pago_tarjeta(subt):
    inc=subt*0.05
    return inc
#Programa principal
resp="s"
cont=0 #cant de clientes
suma_t=0 #suma de todo lo vendido
suma_imp=0 #suma todo los valor de impuesto=iva
while(resp=="s"):
    cont=cont+1 #cuenta la cant de clientes
    cant=valida_cant()
    precio=valida_precio()
    total,imp,subt=calcular_total(cant,precio)  #devuelve 3 valores
    op=valida_fpago()
    if op=="e":
        inc=0
        t=total
    else:
        inc=pago_tarjeta(subt)
        t=total+inc
    print(f"Subtotal...... ${subt:.2f}")
    print(f"IVA...... ${imp:.2f}")
    print(f"Incremento %...... ${inc:.2f}")
    print(f"Total a pagar...... ${t:.2f}")
    suma_t=suma_t+t
    suma_imp=suma_imp+imp
    resp=valida_resp()
#fin del ciclo
print(f"Total vendido {suma_t:.2f}")
print("Cantidad de clientes ", cont)
print(f"Total recibido por IVA  {suma_imp:.2f}")

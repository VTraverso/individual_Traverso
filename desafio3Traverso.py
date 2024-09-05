videojuegos =[[1, "MINECRAFT", "MICROSOFT", "SANDBOX"],
    [2, "OVERWATCH", "BLIZZARD", "FPS"], 
    [3, "MARIO PARTY", "NINTENDO", "ARCADE"], 
    [4, "CALL OF DUTY", "BLIZZARD", "FPS"],
    [5, "DEEP ROCK GALACTIC", "BSG", "FPS"],
    [6, "ANIMAL CROSSING", "ERIC BALONE", "RPG"]]

def organize(videojuegos_):
    vj_ord = [[Id, Nombre[:9], Editor[:8], Genero[:7]] for Id, Nombre, Editor, Genero in videojuegos_]
    for i in range (len(vj_ord)):
        vj_ord[i][1]= vj_ord[i][1].upper()
        vj_ord[i][2]= vj_ord[i][2].upper()
        vj_ord[i][3]= vj_ord[i][3].upper()

    vj_ord2=sorted(vj_ord, key=lambda x:(x[1],x[2],x[0]))
    return vj_ord2
organize(videojuegos)
def create(a):
    a.append([])
    for f in a[0]:
        a[len(a)-1].append(0)
    flag=0
    while flag==0:
        nombr= input("ingrese el nombre del Videojuego: ")
        if nombr.isalpha() == True:
            editr= input("ingrese el editor del Videojuego: ")
            if editr.isalpha() == True:
                genr= input("ingrese el genero del Videojuego: ")
                if genr.isalpha() == True:
                    flag=-1
       
    a[-len(a)][0] = a[0][0] + 1
    a[-len(a)][1] = nombr
    a[-len(a)][2] = editr
    a[-len(a)][3] = genr
    
    return a

def read(b):
    print(f"{'Id' :>6}{'Nombre' :^12}{'Editor' :^12}{'Género' :<6}")
    print("=" * 40)
    for Id, Nombre, Editor, Genero in b:
         print(f"{Id :>6}{Nombre :^12}{Editor :^12}{Genero :<6}")
def update(c):
    flag=0
    while flag==0:
        nro= int(input("¿Qué dato quiere actualizar?: 1-Id, 2-Nombre, 3-Editor, 4-Género"))
        
        flag=1
        if nro==1:
            pos=int(input("ingrese el id que desea cambiar: "))
            band=0
            a=-1
            while band==0 and a<len(c)-1:
                a+=1
                if c[a][0]==pos:
                    band=1
            if band==1:
                c[a][0]==int(input("ingrese el id por el que desea actualizarlo: "))
                return c
            else:
                print("error, el Id que ingresó no se encuentra.")
        else:
            pos=int(input("ingrese el id de la fila del videojuego que desea actualizar: "))
            band=0
            a=-1

            while band==0 and a< len(c)-1:
                a+=1
                if c[a][0]==pos:
                    band=1
            if band==0:
                print("no se encuentra el id ingresado.")
            else:
                des=int(input("¿qué desea cambiar?: 1-Nombre, 2-Editor, 3-Género"))
                if des==1:
                    c[a][1]=input("Ingrese el nombre nuevo: ")
                    return c
                elif des==2:
                    c[a][2]=input("Ingrese el editor nuevo: ")
                    return c
                elif des==3:
                    c[a][3]=input("Ingrese el género nuevo: ")
                    return c
                else:
                    print("dato incorrecto")
                    flag=0

def destroy(d):
    band=0
    a=-1

    while band==0 and a<len(d)-1:
        pos=(input("ingrese el Id que desea eliminar: "))
        a+=1
        if d[a][0]==pos and pos.isnumeric()== True:
            d.pop(a)
            return d
        else:
            print("no se encuentró el id ingresado")
            band=0
    #cuando ingreso un id, no lo encuentra.. por qué?


vj_organized = organize(videojuegos)
flag1=0
flag2=-1
while flag1==0:
    if flag2==0:
        vj_organized=organize(videojuegos)
        flag2=-1
    
    des=int(input("select an action: 1. CREATE, 2. READ, 3. UPDATE, 4. DESTROY 5. STOP"))
    
    if des==1:
        vj=create(vj_organized)
        flag2=0

    elif des==2:
        read(vj_organized)

    elif des==3:
        vj=update(vj_organized)
        flag2=0

    elif des==4:
        vj=destroy(vj_organized)
        flag2=0

    elif des==5:
        flag1=1




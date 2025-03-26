frutas = ["manzana","naranja","kiwi","frutillas","mango"]
frutas_fav = ["frutillas", "naranja", "kiwi"]
asd = input("Escribe una fruta")
if asd in frutas_fav:
    print("Wow!! La/s",asd,"esta/n dentro de tus frutas favoritas")
else:
    print("Esta fruta no esta en tus frutas favoritas.")
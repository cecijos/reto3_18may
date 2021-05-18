billete10=10
billete5=5
billete20=20

#menu = ["ensalada", "hamburguesa", "paella"]
#precio_menu=[10,15,20]

menu ={'ensalada':10,'hamburguesa':15,'paella':20}

#carta=[[menu],[precio_menu]]

cuenta=0
repetir=''

#for x in menu:
    #print(x, end = ' ')
#for x in precio_menu:
 #   print (x, end = ' ')

#for i in carta:
 #   for j in i:
  #      print(j,end="")
    #print()

print(menu)

if __name__ == "__main__":
    while True:
        item=input("Enter menu")
        if item in menu.keys():
            #cuenta=precio_menu
            print(menu[item])
            cuenta=menu[item]
        else:
            print("menu no encontrado")
        repetir = input("Desea comer mas enter y/n")

        if repetir=='y':
         print('y')
        else:
            break
        New_item = input("Enter nuevo menu")
        if New_item in menu.keys():
            print(menu[New_item])
            cuenta = menu[New_item]+cuenta
            print (f'EL total de la cuenta  es {cuenta}')


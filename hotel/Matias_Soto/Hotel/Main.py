from view.Personas_V import chef

def main():
    print("Aplicacion Inicial")

    chefcito = chef("remi", 1 , "Paris", ["Rata"])
    
    print(chefcito.ver_pedidos())

    print(chefcito.recibir_pedido(["Bebida","Completo", "Pie de limon"]))

    print(chefcito.ver_pedidos())

main()

from view.personas import chef

class __main__():
    print("Aplicacion iniciada")
    chefcito = chef("Remi", 1 , "Paris", ["Ratattouille"])

    print(chefcito.ver_pedidos())

    print(chefcito.recibir_pedido(["Bebida", "Completo", "Pie de limon"]))

    print(chefcito.ver_pedidos())

__main__()


from view.personas import chef

def __main__():
    print("Aplicacion iniciada")
    chefcito = chef("remi", 1, "Paris", ["Ratatouille"])

    print(chefcito.ver_pedidos())

    print(chefcito.recibir_pedidos(['Bebida', 'Completo', 'Pie de limon']))

    print(chefcito.ver_pedidos())

__main__()
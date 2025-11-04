from view.personas import Chef

def __main__():
    print("Aplicacion iniciada")
    chefcito = Chef('Remi', 1, 'Paris', ['Ratatoullie'])

    print(chefcito.ver_pedidos())

    print(chefcito.recibir_pedidos(['Bebida','Completo','Pie de limon']))

    print(chefcito.ver_pedidos())

__main__()

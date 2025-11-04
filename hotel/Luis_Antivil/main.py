from view.personas import chef

def __main__(): 
    print("Aplicacion iniciada")
    chefcito= chef('Remi', 1, 'Paris', ['Ratatoullie'])

    print(chefcito.ver_pedidos())

    print(chefcito.recibir_pedidos(['hola']))

    print(chefcito.ver_pedidos())

__main__()
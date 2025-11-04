from view.Personas import chef

def _main_():
    print("Aplicacion Inicial")

    chefcito = chef("remi", 1 , "Paris", ["Rata"])
    
    print(chefcito.ver_pedido())

    print(chefcito.recibir_pedido(["Bebida","Completo", "Pie de limon"]))

    print(chefcito.ver_pedido())

_main_()

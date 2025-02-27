while True:
    sair = input("Deseja sair [sim/nao]? ").lower().startswith('s') # startswith('letra') and endswith('letra')
    
    if sair:
        print("Sistema finalizado.")
        break
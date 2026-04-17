def cash_machine(number: int) -> dict:
    troco = {}

    notas = [100,50,20,10,5,2]
    for nota in notas:
        res = number // nota
        if res != 0:
            troco[str(nota)] = res
            number = number % nota
    
    return troco

saque = cash_machine(120)

for key, value in saque.items():
    print(f"R${key:<3} | {value} nota(s)")
    
din = float(input('\033[33mQuanto dinheiro você tem na carteira? \033[4;32mR$'))
dol = din / 5.30
print(f'\033[0;34mCom \033[4;32mR${din:.2f}\033[0;34m você pode comprar \033[4;32mUS${dol:.2f}\033[m')
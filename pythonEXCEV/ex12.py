preco = float(input('\033[33mQual o preço do produto? \033[4;32mR$'))
promo = preco * 0.05
desconto = preco - promo
print(f'\033[34mO produto que custava \033[4;32mR${preco:.2f}\033[0;34m, na promoção com desconto de \033[31m5%\033[34m, vai custar \033[0;32mR${desconto:.2f}\033[m')

print('\033[4;31m{:=^40}'.format('LOJAS TUTTI AMICI')
      )
preco = float(input('\033[0;33mDigite o preço das compras: \033[0;30m'))
forma = str(input('\033[0;33mComo vai ser a forma de pagamento? \033[0;30m'))
forma = forma.lower()
parcelas = 0
if forma == 'dinheiro' or forma == 'cheque':
    valor = preco - (preco * 0.10)
    print('\033[0;36mPagamento à vista possuí um desconto de 10%! O valor ficará: \033[4;32mR${} '.format(valor))
elif forma == 'débito':
    valor = preco - (preco * 0.05)
    print('\033[0;36mPagamento à vista no cartão possuí um desconto de 5%! O valor ficará:\033[4;32mR${}'.format(valor))
elif forma == 'crédito':
    parcelas = int(input('\033[0;33mQuantas vezes deseja parcelar? \033[0;30m'))
else:
    print('\033[0;31mOpção de pagamento inválida! Tente novamente!')
if parcelas == 2:
    print('\033[0;36mPagamento em duas vezes no cartão de crédito, o valor ficará normal! Valor:\033[4;32m 2x de R${}. Total: R${} '.format(preco/2,
                                                                                                                              preco))
elif parcelas >= 3:
    juros = preco * 0.20
    totparc = (preco + juros) / parcelas
    total = preco + (preco * 0.20)
    print('\033[0;36mPagamento em três ou mais vezes no cartão de crédito, terá 20% De juros! Valor:\033[4;32m {}x de R${:.2f} com 20% De juros. Total: R${:.2f}'.format(parcelas,
                                                                                                                                                                        totparc,
                                                                                                                                                                            total))
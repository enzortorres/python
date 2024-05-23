cor = {'vermelho':'\033[0;31m',
        'verde':'\033[0;32m',
            'amarelo':'\033[0;33m',
                'padrao':'\033[0;30m'}
casa = float(input('{}Qual o valor da casa? {}R$'.format(cor['amarelo'], cor['padrao'])))
salario = float(input('{}Qual o seu saláriO? {}'.format(cor['amarelo'], cor['padrao'])))
ano = int(input('{}Em quantos anos você deseja pagar a casa? {}'.format(cor['amarelo'], cor['padrao'])))
mes = ano * 12
mensalidade = casa / mes
if mensalidade > salario * 0.30:
    print('{}Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(cor['verde'], casa, ano, mensalidade))
    print('{}Infelizmente o emprestimo não poderá ser realizado!\033[m'.format(cor['vermelho']))
else:
    print('{}Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(cor['verde'], casa, ano, mensalidade))
    print('{}O emprestimo poderá ser realizado!\033[m'.format(cor['verde']))
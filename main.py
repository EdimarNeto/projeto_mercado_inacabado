from fluxo_de_caixa import flux_ca

def msg_ini():
    print('<' * 25, '>' * 25)
    print('                   Olá, bem vindo!')
    print('    Informe ou atualize seu Registro Financeiro')
    print('<' * 25, '>' * 25)


def menu():
    print('[1] Usuários')  # pode-se adicionar novos usuários ou clientes a partir daqui
    print('[2] Metodos de Pagamento')
    print('[3] Fluxo de Caixa / Notas Fiscais')
    print('[4] ')
    print('[5] ')


msg_ini()
menu()

opc = int(input('Sua Escolha: '))

if opc == 1:
    print('NÃO ESTÁ FEITO AINDA')

elif opc == 2:
    print('<' * 23, '>' * 23)
    print("Temos essas formas de pagamento:\n" + "1. Boleto\n" + "2. Crédito\n" + "3. Débito\n" + "4. Pix")

    x = input("Opção desejada: ")
    if not x is None or not x == '': x = int(x)
    if x == 1:
        print("--------Boleto--------")

    elif x == 2:
        print("--------Crédito--------")

    elif x == 3:
        print("--------Débito--------")

    elif x == 4:
        print("--------Pix--------")


    print('<' * 23, '>' * 23)

elif opc == 3:
    flux_ca()

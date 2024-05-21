def flux_ca():
    fluxo_caixa = []

    def menu():
        print('<' * 10, '>' * 10)
        print('    Fluxo de Caixa')
        print('<' * 10, '>' * 10)
        print('[1] - Adicionar Receitas')
        print('[2] - Adicionar Despesas')
        print('[0] - Finalizar')

    def cad(tipo):
        nome = str(input('Nome: ')).strip().upper()
        valor = float(input('Valor: '))
        if tipo == 2:
            valor = -valor
        fluxo_caixa.append({
            'nome': nome,
            'valor': valor
        })

    menu()

    while True:
        try:
            opc = int(input('Digite sua opção: '))
            if opc == 0:
                break
            else:
                if opc == 1:
                    cad(1)
                elif opc == 2:
                    cad(2)
        except ValueError:
            print('Opção Inválida.')

    # Nota Fiscal
    total = 0
    for fc in fluxo_caixa:
        print(f'Nome: {fc["nome"]:<3} --- Valor: R$ {fc["valor"]:.2f}')
        total = total + fc["valor"]

    print(f'Saldo atual: R$ {total}')

    print('Deseja imprimir comprovante?')
    print('[1] Sim')
    print('[2] não')

    # imp = int(input('>>> '))
    # if imp == 1:
    # código para impressão
    # inserir um módulo
    # else:
    # print('Fim do programa')

    # Adicionar uma opc para voltar a pagina anterior


if __name__ == '__main__':
    flux_ca()

# Existem diferentes tipos de notas fiscais, como a Nota Fiscal Eletrônica (NF-e),
# que registra a venda de produtos, e a Nota Fiscal de Serviço Eletrônica (NFS-e),
# que registra a prestação de serviços.
# Cada tipo de nota fiscal tem um formato e um processo de emissão diferentes,
# que podem variar de acordo com o município ou o estado.
# Para emitir uma nota fiscal, você precisa ter um certificado digital,
# que é um documento eletrônico que comprova a sua identidade e a autenticidade dos seus dados.
# Você também precisa se credenciar junto à Secretaria da Fazenda do seu estado ou do seu município,
# que é o órgão responsável por autorizar e fiscalizar a emissão de notas fiscais. Depois, você pode usar
# um site ou um programa que gera e envia o arquivo da nota fiscal para o Portal da Fazenda, que é o sistema
# que valida e armazena as notas fiscais.
# Para imprimir uma nota fiscal, você precisa ter uma impressora conectada ao seu computador
# e configurada corretamente. Depois, você pode usar um módulo do Python que permite enviar
# dados para a impressora, como o win32print, que funciona no Windows, ou o cups, que funciona no Linux.
# Você também pode usar um site ou um programa que converte o arquivo da nota fiscal em um formato que pode ser
# impresso, como o PDF ou o Danfe, que é o documento auxiliar da NF-e.
# Você pode encontrar mais informações sobre como emitir e imprimir notas fiscais nos seguintes links:
# Como emitir Nota Fiscal Eletrônica NF-e? Passo a Passo - ContabilizeiComo emitir nota fiscal eletrônica NFS-e
# passo a passo - ContabilizeiAIDF da Nota Fiscal: veja o passo a passo para emitir!Como baixar uma nota fiscal
# com Chave de Acesso – Tecnoblog

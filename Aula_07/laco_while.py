import datetime

# escolha = ''
# while escolha != 'n':
#     ano_de_nascimento = int(input('Digite o ano de nascimento do usuário e tecle enter: '))
#     ano_atual = datetime.date.today().year
#     idade = ano_atual - ano_de_nascimento
#     print(f"A idade do usuario é {idade}")
#     escolha = input('Deseja fazer uma nova verificação? S ou N').lower()
# print('\nFim do programa')


contadora = 0
while contadora <= 50:
    contadora += 1
    if contadora % 3 == 0:
        continue
    print(contadora)
print('\nFim do programa.')
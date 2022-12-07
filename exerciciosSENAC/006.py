dia, mes, ano = input("Digite uma data: ").split("/")
if mes == '01':
    print(dia, "de janeiro de", ano)
elif mes == '02':
    print(dia, "de fevereiro de", ano)
elif mes == '03':
    print(dia, "de março de", ano)
elif mes == '04':
    print(dia, "de abril de", ano)
elif mes == '05':
    print(dia, "de maio de", ano)
elif mes == '06':
    print(dia, "de junho de", ano)
elif mes == '07':
    print(dia, "de julho de", ano)
elif mes == '08':
    print(dia, "de agosto de", ano)
elif mes == '09':
    print(dia, "de setembro de", ano)
elif mes == '10':
    print(dia, "de outubro de", ano)
elif mes == '11':
    print(dia, "de novembro de", ano)
elif mes == '12':
    print(dia, "de dezembro de", ano)
else:
    print('Data invalida!')
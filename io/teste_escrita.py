arquivo = open('dados/contatos_escrita.csv',
               encoding='latin_1', mode='a+')

contatos = [
    '11,Carol,carol@carol.com.br\n',
    '12,Ana,ana@ana.com.br\n',
    '13,Tais,tais@tais.com.br\n',
    '14,Felipe,felipe@felipe.com.br\n'
]

for contato in contatos:  # Loop para escrever os novos contatos
    arquivo.write(contato)
    
arquivo.flush()   # Escreve
arquivo.seek(28)  # Ponteiro
arquivo.write('12,Ana,ana@ana.com.br\n'.upper())
arquivo.flush()
arquivo.seek(0)

for linha in arquivo:
    print(linha)
URL                 = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
INDICE_INTERROGACAO = URL.find('?')
URL_BASE            = URL[:INDICE_INTERROGACAO]
URL_PARAMETROS      = URL[INDICE_INTERROGACAO + 1:]
PARAMETRO_BUSCA     = 'quantidade'
INDICE_PARAMETRO    = URL_PARAMETROS.find(PARAMETRO_BUSCA)
INDICE_VALOR        = INDICE_PARAMETRO + len(PARAMETRO_BUSCA) + 1
INDICE_E_COMERCIAL  = URL_PARAMETROS.find('&', INDICE_VALOR)
if INDICE_E_COMERCIAL == -1:
    VALOR = URL_PARAMETROS[INDICE_VALOR:]
else:
    VALOR = URL_PARAMETROS[INDICE_VALOR:INDICE_E_COMERCIAL]

print(URL)
print(URL_BASE)
print(PARAMETRO_BUSCA)
print(VALOR)

import re


class ExtratorURL:

    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\nURL: " + self.get_url_base() +\
                          "\nParâmetros: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def converte(self, cotacao, moeda_origem, moeda_destino, quantidade):
        if moeda_origem == "dolar" and moeda_destino == "real":
            return f"Valor convertido: {quantidade * cotacao:.2f}"
        elif moeda_origem == "real" and moeda_destino == "dolar":
            return f"Valor convertido: {quantidade / cotacao:.2f}"
        elif moeda_origem == moeda_destino:
            return cotacao
        else:
            return "Erro, escolha uma opção válida"


url = "bytebank.com/cambio?quantidade=8&moedaOrigem=dolar&moedaDestino=real"
extrator_url    = ExtratorURL(url)
cotacao         = 5.50
moeda_origem    = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino   = extrator_url.get_valor_parametro('moedaDestino')
quantidade      = float(extrator_url.get_valor_parametro('quantidade'))

print(extrator_url.converte(cotacao, moeda_origem, moeda_destino, quantidade))

produtos = []


def get_produtos(): return produtos


def inserir_produto(produto): produtos.append(produto)


class Produto:
    def __init__(self, id, preco, data_validade, quantidade, importado):
        self.id = id if id in ('F01', 'F02', 'F03', 'V01', 'V02', 'V03') else 'indefinido'
        self.preco = preco
        self.data_validade = data_validade
        self.quantidade = quantidade
        self.importado = importado

    def __str__(self):
        importado_txt = "importado" if self.importado else ""
        formato = "{:<5} {:<6} {:<4} {:>4} {:>11}"
        produto_formatado = formato.format(f'{self.id}', self.preco, self.quantidade, str(self.data_validade),
                                           importado_txt)
        return produto_formatado

from src.entidades.produto import Produto, inserir_produto, get_produtos
from src.entidades.feira_agricultura_familiar import (
    FeiraAgriculturaFamiliar,
    inserir_feira_agricultura_familiar,
    get_feiras_agricultura_familiar
)
from src.util.gerais import imprimir_objetos
from src.util.data import Data


def cadastrar_feiras_agricultura_familiar():
    inserir_feira_agricultura_familiar(
        FeiraAgriculturaFamiliar(nome='Feira de Dourados', data_realizacao=Data(14, 3, 2025), cidade='Dourados', horario='18:30', uf='MS'))
    inserir_feira_agricultura_familiar(
        FeiraAgriculturaFamiliar(nome='Feira de Sinop', data_realizacao=Data(20, 8, 2026), cidade='Sinop', horario='8:30', uf='MT'))
    inserir_feira_agricultura_familiar(
        FeiraAgriculturaFamiliar(nome='Feira de Guarulhos', data_realizacao=Data(1, 9, 2027), cidade='Guarulhos', horario='20:00', uf='SP'))
    inserir_feira_agricultura_familiar(
        FeiraAgriculturaFamiliar(nome='Feira de BH', data_realizacao=Data(1, 9, 2027), cidade='Belo Horizonte', horario='20:00', uf='MG'))

def cadastrar_produtos():
    inserir_produto(Produto(id='F01', preco=7.25, data_validade=Data(9, 8, 2024), quantidade=10, importado=True))
    inserir_produto(Produto(id='F02', preco=1.99, data_validade=Data(7, 9,2026), quantidade=16, importado=False))
    inserir_produto(Produto(id='F03', preco=5.45, data_validade=Data(5, 6, 2026), quantidade=23, importado=False))
    inserir_produto(Produto(id='V01', preco=3.99, data_validade=Data(20, 8, 2026), quantidade=40, importado=True))
    inserir_produto(Produto(id='V02', preco=7.49, data_validade=Data(31, 10, 2026), quantidade=12, importado=False))
    inserir_produto(Produto(id='V03', preco=6.49, data_validade=Data(31, 10, 2026), quantidade=12, importado=False))


if __name__ == '__main__':
    print('\nExposição de Produtos de uma Banca em uma Feira de Agricultura Familiar')
    cadastrar_feiras_agricultura_familiar()
    imprimir_objetos(cabeçalho='Feira de Agricultura Familiar: nome, data de realização, cidade, uf, horario',
                     objetos=get_feiras_agricultura_familiar())

    cadastrar_produtos()
    imprimir_objetos(cabeçalho='Produtos : id, preço, quantidade, data de validade, importado',
                     objetos=get_produtos())


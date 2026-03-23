feiras_agricultura_familiar = []


def get_feiras_agricultura_familiar(): return feiras_agricultura_familiar


def inserir_feira_agricultura_familiar(feira_agricultura_familiar): feiras_agricultura_familiar.append(
    feira_agricultura_familiar)


class FeiraAgriculturaFamiliar:

    def __init__(self, nome, data_realizacao, cidade, horario, uf):
        self.nome = nome
        self.data_realizacao = data_realizacao
        self.cidade = cidade
        self.horario = horario
        self.uf = uf

    def __str__(self):
        formato = "{:<20} {:<12} {:<16} {:<5} {:>4}"
        feira_agricultura_familiar_formatada = formato.format(f'{self.nome}', str(self.data_realizacao), self.cidade, self.horario, f'{self.uf}')
        return feira_agricultura_familiar_formatada

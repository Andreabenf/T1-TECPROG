from typing import Union

from exceptions import (DescricaoEmBrancoException,
                        ValorDeducaoInvalidoException,
                        ValorRendimentoInvalidoException,
                        ValorPensaoAlimenticiaInvalidoException,
                        NomeEmBrancoException)


class SimuladorIRPF:
    total_rendimentos = 0.0
    total_deducoes = 0.0
    total_dependentes = 0
    rendimentos = []
    deducoes = []
    pensoes_alimenticias = []
    contribuicoes_previdenciarias = []
    dependentes = []
    valor_deducao = 189.59

    # Constantes de valores referentes as faixas
    faixa_1_min = 0.0
    faixa_2_min = 922.67
    faixa_3_min = 924.40
    faixa_4_min = 913.63
    faixa_3_max = 1903.98

    # Constantes de aliquotas referente as faixas
    aliquota_faixa_2 = 0.075
    aliquota_faixa_3 = 0.15
    aliquota_faixa_4 = 0.225
    aliquota_faixa_5 = 0.275

    def cadastrar(self, tipo: str, valor: float, descricao: Union[str, None] = None):
        if descricao and descricao.strip() == "":
            raise DescricaoEmBrancoException

        if valor <= 0:
            if tipo == 'rendimento':
                raise ValorRendimentoInvalidoException
            if tipo == 'deducao':
                raise ValorDeducaoInvalidoException

        if tipo == "rendimento":
            if descricao:
                rendimento = {"descricao": descricao, "valor": valor}
                self.rendimentos.append(rendimento)
            self.total_rendimentos += valor

        if tipo == "deducao":
            if descricao:
                deducao = {"descricao": descricao, "valor": valor}
                self.deducoes.append(deducao)
            self.total_deducoes += valor

    def cadastrar_rendimento(self, valor: float, descricao: Union[str, None] = None):
        self.cadastrar(tipo='rendimento', valor=valor, descricao=descricao)

    def cadastrar_deducao(self, valor: float, descricao: Union[str, None] = None):
        self.cadastrar(tipo='deducao', valor=valor, descricao=descricao)

    def cadastrar_contribuicao_oficial(self, descricao: str, valor: float):
        self.cadastrar_deducao(valor, descricao)

    def cadastrar_pensao_alimenticia(self, valor: float):
        if valor <= 0:
            raise ValorPensaoAlimenticiaInvalidoException

        self.pensoes_alimenticias.append(valor)
        self.cadastrar_deducao(valor=valor)

    def cadastrar_dependente(self, nome: str, data_nascimento: str):
        if nome.strip() == "":
            raise NomeEmBrancoException

        dependente = {"nome": nome, "data_nascimento": data_nascimento}
        self.total_dependentes += 1
        self.dependentes.append(dependente)
        self.cadastrar_deducao(valor=self.valor_deducao)

    def calcular_primeira_faixa(self) -> float:
        return self.faixa_1_min

    def calcular_segunda_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_segunda_faixa = base - self.faixa_3_max

        if base_segunda_faixa <= 0:
            return 0

        if base_segunda_faixa >= self.faixa_2_min:
            return self.aliquota_faixa_2 * self.faixa_2_min

        return base_segunda_faixa * self.aliquota_faixa_2

    def calcular_terceira_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_terceira_faixa = base - (self.faixa_3_max + self.faixa_2_min)

        if base_terceira_faixa <= 0:
            return 0

        if base_terceira_faixa >= self.faixa_3_min:
            return self.aliquota_faixa_3 * self.faixa_3_min

        return base_terceira_faixa * self.aliquota_faixa_3

    def calcular_quarta_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_quarta_faixa = base - \
            (self.faixa_3_max + self.faixa_2_min + self.faixa_3_min)

        if base_quarta_faixa <= 0:
            return 0

        if base_quarta_faixa >= self.faixa_4_min:
            return self.aliquota_faixa_4 * self.faixa_4_min

        return base_quarta_faixa * self.aliquota_faixa_4

    def calcular_quinta_faixa(self) -> float:
        return Calcula5aFaixa(self).computar()

    def calcular_total_imposto(self):
        total = self.calcular_primeira_faixa()
        total += self.calcular_segunda_faixa()
        total += self.calcular_terceira_faixa()
        total += self.calcular_quarta_faixa()
        total += self.calcular_quinta_faixa()

        return total

    def calcular_aliquota_efetiva(self) -> float:
        return round(100 * (self.calcular_total_imposto()/self.total_rendimentos), 2)


class Calcula5aFaixa:

    # Referencia para o objeto original
    fonte: SimuladorIRPF

    # Um atributo para cada variável temporária do método
    base: float
    base_quinta_faixa: float

    def __init__(self, fonte: SimuladorIRPF):
        self.fonte = fonte

    def computar(self):
        self.base = self.fonte.total_rendimentos - self.fonte.total_deducoes
        self.base_quinta_faixa = self.base - \
            (self.fonte.faixa_3_max + self.fonte.faixa_2_min +
             self.fonte.faixa_3_min + self.fonte.faixa_4_min)

        if self.base_quinta_faixa <= 0:
            return 0

        return self.base_quinta_faixa * self.fonte.aliquota_faixa_5

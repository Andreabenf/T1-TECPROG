import pytest
import simulador_IRPF

# Neste commit possímosO codigo implementado após a iterções.
# Após duplicarmos, iremos uttilizar da parametrização para testar com 3 casos de teste cada teste.


@pytest.mark.parametrize("dedu1,dedu2,dedu3,total", [(100, 200, 300, 600), (150, 220, 100, 470), (120, 340, 650, 1110)])
def test_total_decucoes(dedu1, dedu2, dedu3, total):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", dedu1)
    simuilacao.cadastrar_deducao("testeDeducao", dedu2)
    simuilacao.cadastrar_deducao("testeDeducao", dedu3)
    assert simuilacao.total_deducoes == total;

@pytest.mark.parametrize("dedu1,dedu2,rend1,rend2", [(100, 200, 300, 600), (150, 220, 100, 470), (120, 340, 650, 1110)])
def test_1_faixa(dedu1, dedu2, rend1, rend2):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", dedu1)
    simuilacao.cadastrar_deducao("testeDeducao", dedu2)
    simuilacao.cadastrar_rendimento("testeRendimento", rend1)
    simuilacao.cadastrar_rendimento("testeRendimento", rend2)
    assert simuilacao.calcular_primeira_faixa() == 0;

@pytest.mark.parametrize("rendimento, pensao, res", [(100000, 10000, 23.88),(85000, 2000, 25.83),(30000, 500, 24.14)])
def test_aliquota_efetiva(rendimento, pensao, res):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_rendimento("rendimento", rendimento)
    simuilacao.cadastrar_pensao_alimenticia( pensao)
    aliquota = simuilacao.calcular_aliquota_efetiva()
    assert aliquota == res
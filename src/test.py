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


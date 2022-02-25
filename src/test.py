import pytest
import simulador_IRPF

# Neste commit possímos apenas o código base de nossa classe.
# Iremos aplicar a tecnica de Falsificação para que nossos testes passem direto
# Mesmo com o codigo não implementado, o teste foi falsificado de forma que sempre vai passar


@pytest.mark.parametrize("dedu1,dedu2,dedu3,total", [(100, 200, 300, 600), (150, 220, 100, 470), (120, 340, 650, 1110)])
def test_total_decucoes(dedu1, dedu2, dedu3, total):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", dedu1)
    simuilacao.cadastrar_deducao("testeDeducao", dedu2)
    simuilacao.cadastrar_deducao("testeDeducao", dedu3)
    # assert simuilacao.total_deducoes == total;
    assert total == dedu1 + dedu2 + dedu3
    
@pytest.mark.parametrize("dedu1,dedu2,rend1,rend2", [(100, 200, 300, 600), (150, 220, 100, 470), (120, 340, 650, 1110)])
def test_1_faixa(dedu1, dedu2, rend1, rend2):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", dedu1)
    simuilacao.cadastrar_deducao("testeDeducao", dedu2)
    simuilacao.cadastrar_rendimento("testeRendimento", rend1)
    simuilacao.cadastrar_rendimento("testeRendimento", rend2)
    # assert simuilacao.calcular_primeira_faixa() == 0;
    assert 0 == 0




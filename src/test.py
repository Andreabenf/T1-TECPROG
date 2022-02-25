import pytest
import simulador_IRPF

# Neste commit possímos apenas o código base de nossa classe.
# Iremos aplicar a tecnica de Falsificação para que nossos testes passem direto
# Mesmo com o codigo não implementado, o teste foi falsificado de forma que sempre vai passar


# @pytest.mark.parametrize("dedu1,dedu2,dedu3,total", [(100, 200, 300, 600)])
# def test_total_decucoes(dedu1, dedu2, dedu3, total):
def test_total_tresDecucoes():
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", 100)
    simuilacao.cadastrar_deducao("testeDeducao", 200)
    simuilacao.cadastrar_deducao("testeDeducao", 300)
    assert simuilacao.total_deducoes == 600;  
    # assert total == dedu1 + dedu2 + dedu3

def test_total_duasDecucoes():
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_deducao("testeDeducao", 500)
    simuilacao.cadastrar_deducao("testeDeducao", 250)
    assert simuilacao.total_deducoes == 750;  
    # assert total == dedu1 + dedu2 + dedu3    
    
"""  @pytest.mark.parametrize("dedu1,dedu2,rend1,rend2", [(100, 200, 300, 600), (150, 220, 100, 470), (120, 340, 650, 1110)])
 def test_1_faixa(dedu1, dedu2, rend1, rend2):
     simuilacao = simulador_IRPF.SimuladorIRPF()
     simuilacao.cadastrar_deducao("testeDeducao", dedu1)
     simuilacao.cadastrar_deducao("testeDeducao", dedu2)
     simuilacao.cadastrar_rendimento("testeRendimento", rend1)
     simuilacao.cadastrar_rendimento("testeRendimento", rend2)
     # assert simuilacao.calcular_primeira_faixa() == 0;
     assert 0 == 0 """

""" @pytest.mark.parametrize("rendimento, pensao, res", [(100000, 10000, 23.88),(85000, 2000, 25.83),(30000, 500, 24.14)])
    def test_aliquota_efetiva(rendimento, pensao, res):
    simuilacao = simulador_IRPF.SimuladorIRPF()
    simuilacao.cadastrar_rendimento("rendimento", rendimento)
    simuilacao.cadastrar_pensao_alimenticia( pensao)
    aliquota = simuilacao.calcular_aliquota_efetiva()
    aliquota = res
    assert aliquota == res
    
 """

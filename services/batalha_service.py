# ==============================================================================
# ESPAÇO DO PARCEIRO - SISTEMA DE BATALHAS MONSTERDEX
# ==============================================================================
# Este arquivo será responsável por toda a lógica de simulação de combate
# por turnos entre criaturas da MonsterDex.
#
# Planejamento de Implementação Futura:
#
# 1. Lógica de Turnos:
#    - Turnos alternados de ataque e defesa baseados na agilidade/iniciativa 
#      ou nível das criaturas.
#    - Fluxo de batalha até que um dos monstros tenha seus pontos de vida 
#      (HP) zerados.
#
# 2. Modificador d20 (Rolagem de Dado):
#    - Uso de rolagem de um dado virtual de 20 lados (d20) para simular sorte/azar.
#    - Críticos: Se o resultado for 20 (sucesso crítico), o dano será multiplicado.
#    - Esquiva: Se o resultado for 1 (falha crítica), o ataque falha completamente.
#
# 3. Tabela de Vantagens Elementares:
#    - Implementação da lógica inspirada em Pedra-Papel-Tesoura:
#      * Fogo (Vantagem contra Planta, Desvantagem contra Água)
#      * Água (Vantagem contra Fogo, Desvantagem contra Planta)
#      * Planta (Vantagem contra Água, Desvantagem contra Fogo)
#    - Aplicação de multiplicadores de dano baseados no tipo do ataque vs. 
#      tipo do monstro defensor (ex: Dano * 2.0 para vantagem, Dano * 0.5 para desvantagem).
#
# 4. Histórico de Batalhas:
#    - Registro detalhado de cada rodada de combate.
#    - Salvamento do log de batalha no banco de dados (`historico_batalhas`) 
#      contendo o nome dos oponentes, o vencedor, número de turnos e data da batalha.
# ==============================================================================

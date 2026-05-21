# MonsterDex

O **MonsterDex** é um projeto de terminal em Python para cadastrar monstros de bolso e simular batalhas táticas elementares (Fogo, Água e Planta) seguindo a lógica do jogo Pedra, Papel e Tesoura.

---

## 📂 Organização das Pastas (MVC)

O código foi dividido em pacotes modulares para separar dados, visualização e lógica:

*   **`models/banco_dados.py`**: Guarda apenas as variáveis, listas de monstros e histórico de batalhas.
*   **`views/menu_view.py`**: Controla as mensagens do console, recebe os dados digitados e trata erros de entrada com try/except.
*   **`services/monster_service.py`**: Lógica para cadastrar monstros, validar elementos e listar as criaturas da Dex.
*   **`services/batalha_service.py`**: Regras matemáticas do combate, rolagens de dados d20 e cálculo das vantagens dos elementos.
*   **`main.py`**: Ponto de partida que roda o menu.

---

## ⚔️ Vantagens dos Elementos

O cálculo de dano segue as seguintes vantagens e desvantagens de elementos:

*   **Fogo** vence **Planta** (Dano x2.0) e perde para **Água** (Dano x0.5).
*   **Água** vence **Fogo** (Dano x2.0) e perde para **Planta** (Dano x0.5).
*   **Planta** vence **Água** (Dano x2.0) e perde para **Fogo** (Dano x0.5).
*   Elementos iguais ou neutros causam dano padrão (Dano x1.0).

---

## 📋 Lista de Requisitos da Professora

Mapeamento direto de onde cada recurso obrigatório do projeto está aplicado ou planejado:

*   **Tuplas**: Usada na constante `ELEMENTOS_VALIDOS` em `models/banco_dados.py` e para estruturar cada habilidade `(nome, dano)`.
*   **Sets (Conjuntos)**: Usado no filtro de elementos únicos em `services/monster_service.py` e na listagem de habilidades únicas planejada em `listar_todas_habilidades_unicas()`.
*   **Dicionários**: Cada monstro é salvo como um dicionário contendo seus atributos (nome, elemento, nivel, ataque, defesa e habilidades).
*   **Listas**: Listas globais `catalogo_criaturas`, `monstros_customizados` e `historico_batalhas` em `models/banco_dados.py`.
*   **Lambda**: Função de linha única `calcular_poder_bruto` no topo de `services/monster_service.py`.
*   **List Comprehension**: Usada para juntar os monstros em `services/monster_service.py` e planejada na busca por elemento em `buscar_monstros_por_elementos()`.
*   **Match Case**: Usado no tratamento das opções do menu principal em `views/menu_view.py` e no cálculo elemental de vantagens em `services/batalha_service.py`.
*   **If Ternário**: Usado para validar o nome do elemento de forma direta na função `elemento_eh_valido()` em `services/monster_service.py`.

# Guia de Tarefas do Parceiro (MonsterDex)

> **Importante:** Delete este arquivo quando terminar de programar tudo e for juntar os códigos na branch main.

## 🛠️ Comandos do Git para começar

Rode esses comandos no terminal dentro da pasta do projeto para criar sua branch:

```bash
git checkout main
git pull origin main
git checkout -b feature-arena-e-relatorios
```

---

## ⚔️ O que você precisa programar em `services/batalha_service.py`

Crie a função de batalha no final do arquivo (onde deixei marcado):
1. **HP temporário:** Os monstros no banco não têm HP fixo. Calcule um HP para o combate (ex: `defesa * nivel * 5`) e salve em variáveis temporárias para não alterar o catálogo original.
2. **Loop de combate:** Faça um loop `while hp_jogador > 0 and hp_bot > 0:` para controlar os turnos de ataque.
3. **Menu de ataques:** Mostre as 4 habilidades do monstro do jogador. Peça para escolher entre 1 e 4 e use `match case` para definir o ataque escolhido.
4. **Ataque do Bot:** Escolha um ataque do bot de forma aleatória com `random.choice(monstro_bot["habilidades"])`.
5. **Dano:** Aplique a minha função `calcular_dano_final` para calcular quanto de HP o alvo vai perder em cada turno.
6. **Histórico:** Quando a batalha acabar, adicione o resultado na lista `historico_batalhas` (que está no arquivo `models/banco_dados.py`).

---

## 🔍 O que você precisa programar em `services/monster_service.py`

Precisamos entregar alguns requisitos que a professora pediu:

1. **Buscar monstros por elemento:**
   * Crie a função `buscar_monstros_por_elementos(elemento)`.
   * Ela deve retornar uma lista filtrada contendo apenas os monstros do elemento digitado.
   * **Obrigatório:** Use **List Comprehension** para fazer essa busca de forma simples.

2. **Listar habilidades sem repetir (Uso de Sets):**
   * Crie a função `listar_todas_habilidades_unicas()`.
   * Use a estrutura abaixo para pegar as habilidades de todos os monstros da lista e jogar em um `set` para evitar nomes repetidos:

```python
def listar_todas_habilidades_unicas():
    todos = models.banco_dados.catalogo_criaturas + models.banco_dados.monstros_customizados
    nomes_habilidades = set()
    for m in todos:
        for hab in m["habilidades"]:
            nomes_habilidades.add(hab[0]) # hab[0] pega só o nome do ataque, ignorando o dano
    print("Habilidades:", nomes_habilidades)
```

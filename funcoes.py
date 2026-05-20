import banco_dados

calcular_poder_bruto = lambda ataque, nivel: ataque * nivel

def elemento_eh_valido(elemento):
    return True if elemento in banco_dados.ELEMENTOS_VALIDOS else False

def cadastrar_criatura(nome, elemento, nivel, ataque, defesa, habilidades):
    nova_criatura = {
        "nome": nome,
        "elemento": elemento,
        "nivel": nivel,
        "ataque": ataque,
        "defesa": defesa,
        "habilidades": habilidades
    }
    banco_dados.monstros_customizados.append(nova_criatura)

def listar_todos_monstros():
    todos = banco_dados.catalogo_criaturas + banco_dados.monstros_customizados
    
    if not todos:
        print("\n=== NENHUM MONSTRO CADASTRADO NO SISTEMA ===")
        return

    print("\n========================================================")
    print("               CATÁLOGO GERAL DE MONSTROS               ")
    print("========================================================")
    
    for i, monstro in enumerate(todos, start=1):
        poder = calcular_poder_bruto(monstro["ataque"], monstro["nivel"])
        
        print(f"\n[{i}] {monstro['nome'].upper()} ({monstro['elemento']})")
        print(f"    Nível: {monstro['nivel']} | Poder Bruto: {poder}")
        print(f"    Atributos: Ataque: {monstro['ataque']} | Defesa: {monstro['defesa']}")
        print("    Habilidades:")
        
        for j, habilidade in enumerate(monstro["habilidades"], start=1):
            nome_atk, dano_base = habilidade
            print(f"      - Atk {j}: {nome_atk} (Dano Base: {dano_base})")
            
    print("\n========================================================")

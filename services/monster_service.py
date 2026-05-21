import models.banco_dados

# Função lambda para calcular o poder bruto
calcular_poder_bruto = lambda atk, lvl: atk * lvl

def elemento_eh_valido(elemento_nome):
    """
    Verifica se o elemento fornecido é válido utilizando um operador if ternário.
    """
    return True if elemento_nome in models.banco_dados.ELEMENTOS_VALIDOS else False

def cadastrar_monstro(nome, elemento, nivel, ataque, defesa, habilidades):
    """
    Cadastra um novo monstro personalizado na lista correspondente no banco de dados.
    """
    novo_monstro = {
        "nome": nome,
        "elemento": elemento,
        "nivel": nivel,
        "ataque": ataque,
        "defesa": defesa,
        "habilidades": habilidades
    }
    models.banco_dados.monstros_customizados.append(novo_monstro)

def listar_todos_monstros():
    """
    Junta as duas listas do banco de dados (catálogo e customizados) usando List Comprehension
    e exibe as informações detalhadas e as 4 habilidades de cada criatura usando loops FOR.
    """
    # Junção das duas listas usando List Comprehension para demonstrar o requisito
    todos = [m for m in models.banco_dados.catalogo_criaturas] + [m for m in models.banco_dados.monstros_customizados]
    
    if not todos:
        print("\n=== Nenhum monstro cadastrado no sistema! ===")
        return

    # Uso de Set (Conjunto) e Set Comprehension para identificar os elementos únicos presentes no banco
    elementos_presentes = {monstro["elemento"] for monstro in todos}

    print("\n=============================================")
    print("           CATÁLOGO DE MONSTROS DÉX           ")
    print(f" Elementos registrados na Dex: {', '.join(elementos_presentes)}")
    print("=============================================")
    
    for i, monstro in enumerate(todos, 1):
        poder = calcular_poder_bruto(monstro["ataque"], monstro["nivel"])
        print(f"\n[{i}] {monstro['nome'].upper()} (Poder Bruto: {poder})")
        print(f"    - Elemento: {monstro['elemento']}")
        print(f"    - Nível:    {monstro['nivel']}")
        print(f"    - Ataque:   {monstro['ataque']}")
        print(f"    - Defesa:   {monstro['defesa']}")
        print("    - Habilidades (Ataques):")
        
        # Loop estruturado para exibir as 4 habilidades da criatura
        for hab_idx, habilidade in enumerate(monstro["habilidades"], 1):
            nome_ataque, dano_base = habilidade
            print(f"        {hab_idx}. {nome_ataque} (Dano Base: {dano_base})")
            
    print("\n=============================================")

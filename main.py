import funcoes

def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("             MONSTER-DEX - MENU PRINCIPAL             ")
        print("=" * 50)
        print("  1. Cadastrar Criatura Customizada")
        print("  2. Listar Todas as Criaturas")
        print("  3. Batalhar (Modo de Batalha)")
        print("  4. Ver Histórico de Batalhas")
        print("  0. Sair do Sistema")
        print("=" * 50)
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[Erro] Entrada inválida. Escolha uma opção numérica (0 a 4).")
            continue
            
        match opcao:
            case 1:
                print("\n" + "-" * 50)
                print("            CADASTRO DE NOVA CRIATURA             ")
                print("-" * 50)
                
                nome = input("Nome da criatura: ").strip()
                while not nome:
                    print("[Erro] O nome não pode ser vazio.")
                    nome = input("Nome da criatura: ").strip()
                
                # Validação de Elemento usando a função elemento_eh_valido
                while True:
                    elemento = input("Elemento (Fogo, Água, Planta): ").strip().capitalize()
                    if funcoes.elemento_eh_valido(elemento):
                        break
                    print("[Erro] Elemento inválido! Escolha entre Fogo, Água ou Planta.")
                
                # Leitura de Nível
                while True:
                    try:
                        nivel = int(input("Nível (1-100): "))
                        if 1 <= nivel <= 100:
                            break
                        print("[Erro] O nível deve ser entre 1 e 100.")
                    except ValueError:
                        print("[Erro] Por favor, insira um número inteiro.")
                        
                # Leitura de Ataque
                while True:
                    try:
                        ataque = int(input("Valor de Ataque (mínimo 0): "))
                        if ataque >= 0:
                            break
                        print("[Erro] O ataque deve ser maior ou igual a 0.")
                    except ValueError:
                        print("[Erro] Por favor, insira um número inteiro.")
                        
                # Leitura de Defesa
                while True:
                    try:
                        defesa = int(input("Valor de Defesa (mínimo 0): "))
                        if defesa >= 0:
                            break
                        print("[Erro] A defesa deve ser maior ou igual a 0.")
                    except ValueError:
                        print("[Erro] Por favor, insira um número inteiro.")
                        
                # Leitura das 4 Habilidades usando loop FOR
                habilidades = []
                print("\nCadastre as 4 habilidades da criatura:")
                for i in range(1, 5):
                    nome_atk = input(f"  Nome do Ataque {i}: ").strip()
                    while not nome_atk:
                        print("  [Erro] O nome do ataque não pode ser vazio.")
                        nome_atk = input(f"  Nome do Ataque {i}: ").strip()
                        
                    while True:
                        try:
                            dano_base = int(input(f"  Dano Base do Ataque {i} (mínimo 0): "))
                            if dano_base >= 0:
                                break
                            print("  [Erro] O dano base deve ser maior ou igual a 0.")
                        except ValueError:
                            print("  [Erro] Por favor, insira um número inteiro.")
                            
                    habilidades.append((nome_atk, dano_base))
                    
                funcoes.cadastrar_criatura(nome, elemento, nivel, ataque, defesa, habilidades)
                print(f"\n[Sucesso] Criatura '{nome}' cadastrada com sucesso!")
                
            case 2:
                funcoes.listar_todos_monstros()
                
            case 3:
                print("\n" + "#" * 50)
                print("   [BLOQUEADO] Funcionalidade de Batalha em Desenvolvimento!")
                print("   Este módulo será desenvolvido pelo parceiro de equipe.")
                print("   (Verifique a branch dedicada à batalha)")
                print("#" * 50)
                
            case 4:
                print("\n" + "#" * 50)
                print("   [BLOQUEADO] Histórico de Batalhas Indisponível.")
                print("   Aguardando a implementação da lógica de batalha.")
                print("#" * 50)
                
            case 0:
                print("\nObrigado por utilizar o Monster-Dex! Encerrando...")
                break
                
            case _:
                print("\n[Erro] Opção inválida. Escolha uma opção de 0 a 4.")

if __name__ == "__main__":
    menu_principal()

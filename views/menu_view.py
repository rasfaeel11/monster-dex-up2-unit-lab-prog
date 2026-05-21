import services.monster_service

def exibir_menu():
    """
    Exibe o menu interativo da MonsterDex no terminal utilizando um loop WHILE TRUE
    e trata as opções com a estrutura MATCH CASE (Python 3.10+).
    """
    while True:
        print("\n" + "=" * 45)
        print("          👾 BEM-VINDO À MONSTERDEX 👾         ")
        print("=" * 45)
        print(" [1] Cadastrar Criatura Customizada")
        print(" [2] Listar Todas as Criaturas")
        print(" [3] Simular Batalha (Modo Arena)")
        print(" [4] Exibir Histórico de Batalhas")
        print(" [0] Sair do Programa")
        print("=" * 45)
        
        opcao = input("Escolha uma opção: ").strip()
        
        match opcao:
            case '1':
                print("\n--- CADASTRO DE NOVA CRIATURA ---")
                try:
                    nome = input("Nome da criatura: ").strip()
                    if not nome:
                        print("[Erro] O nome da criatura não pode ser vazio.")
                        continue
                    
                    elemento = input("Elemento (Fogo/Água/Planta): ").strip().capitalize()
                    if not services.monster_service.elemento_eh_valido(elemento):
                        print(f"[Erro] Elemento inválido! Escolha entre: Fogo, Água ou Planta.")
                        continue
                    
                    nivel = int(input("Nível (inteiro): "))
                    ataque = int(input("Ataque (inteiro): "))
                    defesa = int(input("Defesa (inteiro): "))
                    
                    if nivel <= 0 or ataque < 0 or defesa < 0:
                        print("[Erro] Os valores numéricos devem ser positivos.")
                        continue
                    
                    habilidades = []
                    print("\n--- Cadastro das 4 Habilidades ---")
                    for i in range(1, 5):
                        nome_atk = input(f"Nome da habilidade {i}: ").strip()
                        if not nome_atk:
                            print("[Erro] O nome da habilidade não pode ser vazio.")
                            raise ValueError("Nome de habilidade vazio")
                        
                        dano_base = int(input(f"Dano base da habilidade {i} (inteiro): "))
                        if dano_base < 0:
                            print("[Erro] O dano base não pode ser negativo.")
                            raise ValueError("Dano negativo")
                            
                        habilidades.append((nome_atk, dano_base))
                    
                    # Chama o serviço para cadastrar no banco
                    services.monster_service.cadastrar_monstro(nome, elemento, nivel, ataque, defesa, habilidades)
                    print(f"\n🎉 Sucesso! {nome} foi registrado com sucesso na MonsterDex!")
                    
                except ValueError:
                    print("\n❌ Erro: Entrada inválida! Por favor, digite números inteiros válidos para nível, ataque, defesa e dano base.")
            
            case '2':
                # Chama a função de listar todas as criaturas do serviço
                services.monster_service.listar_todos_monstros()
                
            case '3':
                print("\n⚠️  [Aviso] O simulador de batalhas está sendo desenvolvido na branch paralela 'feature-batalha'.")
                
            case '4':
                print("\n⚠️  [Aviso] O histórico de batalhas está sendo desenvolvido na branch paralela 'feature-historico'.")
                
            case '0':
                print("\nEncerrando a MonsterDex... Obrigado por utilizar!")
                break
                
            case _:
                print("\n❌ Opção inválida! Escolha uma das opções apresentadas no menu.")

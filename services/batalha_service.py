import random

def rolar_d20():
    # Sorteia um numero de 1 a 20 e retorna o resultado e a classificacao
    resultado = random.randint(1, 20)
    if resultado == 1:
        return resultado, "Esquiva"
    elif resultado == 20:
        return resultado, "Critico"
    else:
        return resultado, "Normal"

def calcular_multiplicador_elemental(elemento_atk, elemento_def):
    # Retorna a vantagem do elemento atacante contra o defensor
    match (elemento_atk, elemento_def):
        case ("Fogo", "Planta") | ("Planta", "Água") | ("Água", "Fogo"):
            return 2.0
        case ("Planta", "Fogo") | ("Água", "Planta") | ("Fogo", "Água"):
            return 0.5
        case _:
            return 1.0

def calcular_dano_final(status_ataque, dano_base_golpe, status_defesa_alvo, elemento_atk, elemento_def):
    # Calcula o dano final do ataque aplicando a rolagem do d20 e o elemento
    dado, tipo_rolagem = rolar_d20()
    
    if tipo_rolagem == "Esquiva":
        print("Errou! O oponente esquivou do golpe.")
        return 0
        
    mult_critico = 2.0 if tipo_rolagem == "Critico" else 1.0
    mult_elemental = calcular_multiplicador_elemental(elemento_atk, elemento_def)
    
    # Formula de dano base: ataque do monstro + dano do golpe - defesa do alvo
    dano_base = (status_ataque + dano_base_golpe) - status_defesa_alvo
    
    dano_calculado = dano_base * mult_critico * mult_elemental
    dano_final = int(dano_calculado)
    
    # Trava de dano minimo = 10
    if dano_final < 10:
        dano_final = 10
        
    if tipo_rolagem == "Critico":
        print(f"Acerto Critico! (Rolou: {dado}) Dano dobrado!")
    else:
        print(f"Dado: {dado} ({tipo_rolagem})")
        
    return dano_final

# ==============================================================================
# PARCEIRO: Programe a partir daqui o loop de turnos da batalha (While)
# ==============================================================================

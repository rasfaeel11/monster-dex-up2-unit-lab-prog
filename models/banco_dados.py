# Tuple of valid elements
ELEMENTOS_VALIDOS = ("Fogo", "Água", "Planta")

# Catalog of 3 original monsters, one of each element, with 4 skills (tuple: (attack_name, base_damage))
catalogo_criaturas = [
    {
        "nome": "Pyrilizard",
        "elemento": "Fogo",
        "nivel": 5,
        "ataque": 18,
        "defesa": 12,
        "habilidades": [
            ("Brasa", 10),
            ("Mordida Flamejante", 25),
            ("Rugido de Fogo", 0),
            ("Explosão Solar", 50)
        ]
    },
    {
        "nome": "Hydraqua",
        "elemento": "Água",
        "nivel": 5,
        "ataque": 14,
        "defesa": 16,
        "habilidades": [
            ("Jato de Água", 12),
            ("Cauda Chicotada", 18),
            ("Névoa Protetora", 0),
            ("Tsunami", 45)
        ]
    },
    {
        "nome": "Florasaur",
        "elemento": "Planta",
        "nivel": 5,
        "ataque": 15,
        "defesa": 15,
        "habilidades": [
            ("Chicote de Vinha", 15),
            ("Semente Drenante", 10),
            ("Folha Navalha", 22),
            ("Raio Solar", 50)
        ]
    }
]

# Custom monsters created by the user
monstros_customizados = []

# Battle history logs
historico_batalhas = []

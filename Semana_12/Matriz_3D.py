# Creamos una matriz 3D para almacenar las temperaturas de las ciudades

# La Primera dimensión es de : 3 Ciudades
# La Segunda dimensión es de : Días de la semana (7 días)
# La Tercera dimensión es de : 4 Semanas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 20},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 40},
            {"dia": "Domingo", "temp": 45}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 16},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 31}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 78},
            {"dia": "Miércoles", "temp": 80},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 87},
            {"dia": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 14},
            {"dia": "Jueves", "temp": 13},
            {"dia": "Viernes", "temp": 12},
            {"dia": "Sábado", "temp": 11},
            {"dia": "Domingo", "temp": 10}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 20},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 12},
            {"dia": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 45},
            {"dia": "Martes", "temp": 40},
            {"dia": "Miércoles", "temp": 35},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 15}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"dia": "Lunes", "temp": 49},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 53},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 38},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 22},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 21},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 15},
            {"dia": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 70},
            {"dia": "Martes", "temp": 60},
            {"dia": "Miércoles", "temp": 50},
            {"dia": "Jueves", "temp": 40},
            {"dia": "Viernes", "temp": 30},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 10}
        ]
    ]
]

# Escogemos los nombres de las ciudades
ciudades = [ "Manabi", "Ambato", "Machala"]

# Calcular el promedio de temperaturas para cada ciudad y cada semana
for i, ciudad in enumerate(temperaturas):
    print(f"\nCiudad {ciudades[i]}:")
    for j, semana in enumerate(ciudad):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {j + 1}: Promedio {promedio:.2f}°F")



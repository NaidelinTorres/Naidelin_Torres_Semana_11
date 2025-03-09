# Creamos una matriz 3D para almacenar las temperaturas de las ciudades

# La Primera dimensión es de : 3 Ciudades
# La Segunda dimensión es de : Días de la semana (7 días)
# La Tercera dimensión es de : 4 Semanas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"dia": "Lunes", "temp": 78},
            {"dia": "Martes", "temp": 80},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 85},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 76},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 83},
            {"dia": "Jueves", "temp": 81},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 77},
            {"dia": "Martes", "temp": 81},
            {"dia": "Miércoles", "temp": 85},
            {"dia": "Jueves", "temp": 82},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 95}
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
            {"dia": "Lunes", "temp": 72},
            {"dia": "Martes", "temp": 74},
            {"dia": "Miércoles", "temp": 76},
            {"dia": "Jueves", "temp": 73},
            {"dia": "Viernes", "temp": 79},
            {"dia": "Sábado", "temp": 81},
            {"dia": "Domingo", "temp": 85}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 70},
            {"dia": "Martes", "temp": 72},
            {"dia": "Miércoles", "temp": 74},
            {"dia": "Jueves", "temp": 71},
            {"dia": "Viernes", "temp": 77},
            {"dia": "Sábado", "temp": 79},
            {"dia": "Domingo", "temp": 83}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 71},
            {"dia": "Martes", "temp": 75},
            {"dia": "Miércoles", "temp": 78},
            {"dia": "Jueves", "temp": 76},
            {"dia": "Viernes", "temp": 80},
            {"dia": "Sábado", "temp": 82},
            {"dia": "Domingo", "temp": 86}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 69},
            {"dia": "Martes", "temp": 71},
            {"dia": "Miércoles", "temp": 73},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 78},
            {"dia": "Sábado", "temp": 80},
            {"dia": "Domingo", "temp": 84}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"dia": "Lunes", "temp": 90},
            {"dia": "Martes", "temp": 92},
            {"dia": "Miércoles", "temp": 94},
            {"dia": "Jueves", "temp": 91},
            {"dia": "Viernes", "temp": 95},
            {"dia": "Sábado", "temp": 98},
            {"dia": "Domingo", "temp": 100}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 90},
            {"dia": "Miércoles", "temp": 92},
            {"dia": "Jueves", "temp": 89},
            {"dia": "Viernes", "temp": 93},
            {"dia": "Sábado", "temp": 96},
            {"dia": "Domingo", "temp": 99}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 89},
            {"dia": "Martes", "temp": 91},
            {"dia": "Miércoles", "temp": 93},
            {"dia": "Jueves", "temp": 92},
            {"dia": "Viernes", "temp": 94},
            {"dia": "Sábado", "temp": 97},
            {"dia": "Domingo", "temp": 101}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 87},
            {"dia": "Martes", "temp": 89},
            {"dia": "Miércoles", "temp": 91},
            {"dia": "Jueves", "temp": 90},
            {"dia": "Viernes", "temp": 92},
            {"dia": "Sábado", "temp": 95},
            {"dia": "Domingo", "temp": 98}
        ]
    ]
]

# Calcular el promedio de las temperaturas para cada ciudad y cada semana
for i, ciudad in enumerate(temperaturas):
    print(f"\nCiudad {i + 1}:")
    for j, semana in enumerate(ciudad):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {j + 1}: Promedio {promedio:.2f}°F")



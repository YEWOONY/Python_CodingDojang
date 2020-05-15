terrestrial_planet = {           # 지구형 행성
    'Mercury': {
        'mean_radius': 2439.7,   # 반지름
        'mass': 3.3022E+23,      # 질량
        'orbital_period': 87.969 # 공전주기
    },
    'Venus': {
        'mean_radius': 6051.8,   # 반지름
        'mass': 4.8676E+24,      # 질량
        'orbital_period': 224.70069 # 공전주기
    },
    'Earth': {
        'mean_radius': 6371.0,   # 반지름
        'mass': 5.97219E+24,      # 질량
        'orbital_period': 365.25641 # 공전주기
    },
    'Mars': {
        'mean_radius': 3389.5,   # 반지름
        'mass': 6.4185E+23,      # 질량
        'orbital_period': 686.9600 # 공전주기
    }
}

print(terrestrial_planet['Venus']['mean_radius'])
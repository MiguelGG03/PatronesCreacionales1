def mesToNumber(mes):
    meses = {
        'ENERO': 1,
        'FEBRERO': 2,
        'MARZO': 3,
        'ABRIL': 4,
        'MAYO': 5,
        'JUNIO': 6,
        'JULIO': 7,
        'AGOSTO': 8,
        'SEPTIEMBRE': 9,
        'OCTUBRE': 10,
        'NOVIEMBRE': 11,
        'DICIEMBRE': 12
    }
    mes_en_mayusculas = mes.upper()
    
    if mes_en_mayusculas in meses:
        return meses[mes_en_mayusculas]
    else:
        return None

def numberToMes(number):
    meses = {
        1: 'ENERO',
        2: 'FEBRERO',
        3: 'MARZO',
        4: 'ABRIL',
        5: 'MAYO',
        6: 'JUNIO',
        7: 'JULIO',
        8: 'AGOSTO',
        9: 'SEPTIEMBRE',
        10: 'OCTUBRE',
        11: 'NOVIEMBRE',
        12: 'DICIEMBRE'
    }
    
    if number in meses:
        return meses[number]
    else:
        return None



def horaToNumber(tiempo):
    horas, minutos, segundos = map(int, tiempo.split(':'))
    
    tiempo_en_horas = horas + minutos / 60 + segundos / 3600
    return tiempo_en_horas

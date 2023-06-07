def define_data(id):
  return [
    {
      "code": "111023C",
      "name": "MATEMÁTICAS BÁSICAS",
      "credits": 3,
      "group": "07",
      "horario": {"time": ["16:00-18:00", "7:00-9:00", "7:00-9:00"], "date": ["martes", "miercoles", "viernes"], "place": ["Edf. E23 (E23) -> 1006 -- TL -- MELENDEZ", "Edf. E20 (E20) -> 2104 -- MG -- MELENDEZ", "Edf. E20 (E20) -> 2115 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "111023C",
      "name": "MATEMÁTICAS BÁSICAS",
      "credits": 3,
      "group": "08",
      "horario": {"time": ["16:00-18:00", "7:00-9:00", "7:00-9:00"], "date": ["martes", "miercoles", "viernes"], "place": ["Edf. E23 (E23) -> 1015 -- TL -- MELENDEZ", "Edf. E20 (E20) -> 2111 -- MG -- MELENDEZ", "Edf. E20 (E20) -> 2023 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "404002C",
      "name": "DEPORTE Y SALUD",
      "credits": 2,
      "group": "26",
      "horario": {"time": ["14:00-16:00"], "date": ["sabado"], "place": ["sin espacio"]},
      "id_profesor": id
    },
    {
      "code": "404002C",
      "name": "DEPORTE Y SALUD",
      "credits": 2,
      "group": "27",
      "horario": {"time": ["14:00-16:00"], "date": ["sabado"], "place": ["sin espacio"]},
      "id_profesor": id
    },
    {
      "code": "750012C",
      "name": "FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA",
      "credits": 3,
      "group": "01",
      "horario": {"time": ["10:00-13:00"], "date": ["martes"], "place": ["Edf. B13 (B13) -> SALA 1 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "750012C",
      "name": "FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA",
      "credits": 3,
      "group": "02",
      "horario": {"time": ["10:00-13:00"], "date": ["martes"], "place": ["Edf. B13 (B13) -> SALA 6 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "701002C",
      "name": "TALLER DE INGENIERÍA I",
      "credits": 3,
      "group": "01",
      "horario": {"time": ["14:00-17:00"], "date": ["jueves"], "place": ["Edf. B13 (B13) -> AUD 3 -- TL -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "701002C",
      "name": "TALLER DE INGENIERÍA I",
      "credits": 3,
      "group": "02",
      "horario": {"time": ["14:00-17:00"], "date": ["jueves"], "place": ["Edf. E53 (E53) -> 2016 -- TL -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "701003C",
      "name": "INTRODUCCIÓN A LA INGENIERÍA",
      "credits": 2,
      "group": "08",
      "horario": {"time": ["7:00-9:00"], "date": ["jueves"], "place": ["Edf. E53 (E53) -> 2016 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "701003C",
      "name": "INTRODUCCIÓN A LA INGENIERÍA",
      "credits": 2,
      "group": "09",
      "horario": {"time": ["7:00-9:00"], "date": ["jueves"], "place": ["Edf. B13 (B13) -> AUD 2 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "111038C",
      "name": "ÁLGEBRA LINEAL",
      "credits": 3,
      "group": "01",
      "prerequisite": {"prerequisite_1": "111023C"},
      "horario": {"time": ["11:00-13:00","11:00-13:00","11:00-13:00"], "date": ["miercoles", "jueves", "viernes"], "place": ["Edf. E23 (E23) -> 1030 -- MG -- MELENDEZ", "Edf. E20 (E20) -> SC1 -- MG -- MELENDEZ", "Edf. B23 (B23) -> 2001 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "111021C",
      "name": "CÁLCULO MONOVARIABLE",
      "credits": 3,
      "group": "09",
      "prerequisite": {"prerequisite_1": "111023C"},
      "horario": {"time": ["14:00-16:00", "14:00-16:00", "14:00-16:00"], "date": ["miercoles", "jueves", "viernes"], "place": ["Edf. E37 (E37) -> AUD1 -- MG -- MELENDEZ", "Edf. E26 (E26) -> 1023 -- TL -- MELENDEZ", "Edf. E23 (E23) -> 1045 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "750015C",
      "name": "FUND.PROGRAMACIÓN ORIENTADA A OBJETOS",
      "credits": 3,
      "group": "01",
      "prerequisite": {"prerequisite_1": "750012C", "prerequisite_2": "701002C"},
      "horario": {"time": ["7:00-10:00"], "date": ["miercoles"], "place": ["Edf. B13 (B13) -> SALA 1 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "750015C",
      "name": "FUND.PROGRAMACIÓN ORIENTADA A OBJETOS",
      "credits": 3,
      "group": "02",
      "prerequisite": {"prerequisite_1": "750012C", "prerequisite_2": "701002C"},
      "horario": {"time": ["7:00-10:00"], "date": ["miercoles"], "place": ["Edf. B13 (B13) -> SALA 2 -- MG -- MELENDEZ"]},
      "id_profesor": id
    },
    {
      "code": "106012C",
      "name": "FÍSICA I + LABORATORIO",
      "credits": 4,
      "group": "04",
      "prerequisite": {"prerequisite_1": "111021C"},
      "horario": {"time": ["10:00-13:00","9:00-11:00","9:00-11:00"], "date": ["martes", "miercoles", "viernes"], "place": ["sin espacio", "Edf. E24 (E24) -> AUD1 -- MG -- MELENDEZ", "Edf. B23 (B23) -> 2002 -- MG -- MELENDEZ"]},
      "id_profesor": id
    }
  ]
  

def error_data(id):
  return [{
    "name": "FUND.PROGRAMACIÓN ORIENTADA A OBJETOS",
    "credits": 3,
    "group": "02",
    "prerequisite": {"prerequisite_1": "750012C", "prerequisite_2": "701002C"},
    "horario": {"time": ["7:00-10:00"], "date": ["miercoles"], "place": ["Edf. B13 (B13) -> SALA 2 -- MG -- MELENDEZ"]},
    "id_profesor": id
  }]
# -*- coding: utf-8 -*-

countries = {
  'México': 122,
  'Colombia': 49,
  'Argentina': 43,
  'Chile': 18,
  'Perú': 31,
}

while True:
  country = str(input('Escribe el nombre de un país: '))
  try:
    print('La población de {} es: {} millones'. format(country, countries[country]))
  except KeyError:
    print('No tenemos el dato de población de {}'.format(country))

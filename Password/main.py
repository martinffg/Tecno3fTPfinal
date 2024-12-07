import secrets, string, sys

# les paso un diccionario donde cada valor tendra una cadena, es decir letras tiene una cadena del alfabeto en mayusculas y minusculas, numeros tiene la cadena de numeros del 0 al 9 y lo mismo con caracteres

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

password = ''

# password.join(secrets.choice(tipo)) con ese comando podemos asignar a un strig que tome valores aleatorios de una lista (tipo)que le enviemos , en este caso la lista deberia ser una de las 3 del diccionario o una conbinacion.
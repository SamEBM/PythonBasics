import re

# VALIDACION DE CORREO
patron = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = 'samuelebm@hotmail.com'
email2 = 'saj@@hotmail.com'

a = patron.search(email)
print(a)

b = patron.search(email2)
print(b)

# VALIDACION DE CONTRASEÑA
# Debe tener al menos 8 caracteres
# Debe contener cualquier tipo de letra o los simbolos: $ % # @
# Debe terminar con un numero

password = re.compile(r"[a-zA-Z0-9$%#@]{8,}[0-9]")
pw = 'Contrasena10@1'

c = password.fullmatch(pw)
print(c)
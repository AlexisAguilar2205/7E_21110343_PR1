
def modus_ponens(llueve, suelo_mojado):
    if llueve:
        return "Est� lloviendo"
    else:
        return "No se puede inferir si est� lloviendo o no."

# Ejemplo de Modus Ponens
llueve = True
suelo_mojado = True

resultado = modus_ponens(llueve, suelo_mojado)
print(resultado)

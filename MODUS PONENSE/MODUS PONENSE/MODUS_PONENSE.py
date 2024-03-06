
def modus_ponens(llueve, suelo_mojado):
    if llueve:
        return "Está lloviendo"
    else:
        return "No se puede inferir si está lloviendo o no."

# Ejemplo de Modus Ponens
llueve = True
suelo_mojado = True

resultado = modus_ponens(llueve, suelo_mojado)
print(resultado)

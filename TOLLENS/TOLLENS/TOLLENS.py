
def modus_tollens(motor_funcionando, ruidos_extra�os):
    if not ruidos_extra�os:
        return "El motor est� funcionando correctamente"
    else:
        return "El motor no est� funcionando correctamente"

# Ejemplo de Modus Tollens
motor_funcionando = True
ruidos_extra�os = True

resultado = modus_tollens(motor_funcionando, ruidos_extra�os)
print(resultado)

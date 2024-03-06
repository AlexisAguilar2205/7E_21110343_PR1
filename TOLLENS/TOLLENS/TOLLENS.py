
def modus_tollens(motor_funcionando, ruidos_extraños):
    if not ruidos_extraños:
        return "El motor está funcionando correctamente"
    else:
        return "El motor no está funcionando correctamente"

# Ejemplo de Modus Tollens
motor_funcionando = True
ruidos_extraños = True

resultado = modus_tollens(motor_funcionando, ruidos_extraños)
print(resultado)

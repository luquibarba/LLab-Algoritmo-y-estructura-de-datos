msg = ["hola", "xd", "como andas?"]
def mostrar_mesnajes():
    for m in msg:
        print(m)
mostrar_mesnajes()

msg_enviados = []
def enviar_mensajes():
    while msg:
        mensaje = msg.pop()
        msg_enviados.append(mensaje)
    print (msg)
    print (msg_enviados)

enviar_mensajes()

mostrar_mesnajes()
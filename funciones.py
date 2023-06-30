def get_location(*distances):
    pass
	


def get_message(*messages):
    mensajeObtenido=[]
    for message in messages:
        messageValue=message
        for index, message in enumerate(messageValue):
            if(len(message)>0):
                try:
                    mensajePosition=mensajeObtenido[index]
                    if(mensajePosition!=message):
                        mensajeObtenido.insert(index, message)
                except:
                    mensajeObtenido.insert(index, message)
                
    return " ".join(mensajeObtenido)

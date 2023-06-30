from math import cos, sin, radians


antena_coords={
"wonderfulAntena1": (-25, -10),
"wonderfulAntena2": (5, -5),
"wonderfulAntena3": (25, 5),
}
def get_message(messages):
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
def calculoPosition(antena_name:str, distance:float):
    x, y = antena_coords[antena_name]
    angle = radians(x * 90)  # Convertir el ángulo a radianes
    x_sum = x * (distance * cos(angle))
    y_sum = y * (distance * sin(angle))
    return [x_sum, y_sum]
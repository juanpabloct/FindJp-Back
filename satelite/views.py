from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from pydantic import BaseModel
from json import loads
from typing import List
from satelite.controllers import get_message, antena_coords, calculoPosition


class Antena(BaseModel):
    name: str
    distance: float
    message: List[str]


class AllSatelites(BaseModel):
    antenas: List[Antena]


class Satelite(BaseModel):
    distance: float
    message: List[str]


@csrf_exempt
def satelite_views(request: HttpRequest):
    x_sum = 0
    y_sum = 0
    message = ""
    messages = []

    if request.method == 'POST':
        values_body = loads(request.body.decode('utf-8'))
        try:
            parsed_data = AllSatelites.parse_obj(values_body)
            for antena in parsed_data.antenas:
                antena_name = antena.name
                distance = antena.distance
                messages+=[antena.message]
                if antena_name in antena_coords:
                    x, y = calculoPosition(antena_name, distance)
                    x_sum += x
                    y_sum += y
            message = get_message(messages)
            return JsonResponse({
                "position": {"x": x_sum, "y": y_sum},
                "message": message
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'message': 'Método no permitido'})


@csrf_exempt
def localizacion_por_partes_views(request: HttpRequest, nombre_antena: str):
    x_sum = 0
    y_sum = 0
    message = ""

    if request.method == 'POST':
        values_body = loads(request.body.decode('utf-8'))
        try:
            parsed_data = Satelite.parse_obj(values_body)
            # Realiza los cálculos para obtener la posición según el nombre de la antena y los datos recibidos
            # ...
            message+=" ".join(parsed_data.message)
            x, y = calculoPosition(nombre_antena, parsed_data.distance)
            x_sum += x
            y_sum += y
            return JsonResponse({
                "position": {"x": x_sum, "y": y_sum},
                "message": message
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'message': 'Método no permitido'})

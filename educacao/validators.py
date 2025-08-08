from django.core.exceptions import ValidationError
from rest_framework import serializers

def validar_nota_maxima(atividade, nota):
    if nota and atividade:
        if nota > atividade.valor:
            error_msg = f'A nota máxima que pode ser atribuída é de {atividade.valor} pontos!'
            raise ValidationError(error_msg)
    return True
    
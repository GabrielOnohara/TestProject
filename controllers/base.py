import falcon
from db import Session
from models import User

# Classe base com a lógica compartilhada, incluindo validação de paginação
class BaseResource:
    def get_pagination_params(self, req):
        # Pegando os parâmetros de paginação da requisição
        page_size = req.get_param_as_int('page_size', default=5)  # Tamanho da página, default é 5
        page_number = req.get_param_as_int('page_number', default=1)  # Número da página, default é 1

        # Garantindo que o page_size seja um valor positivo
        if page_size <= 0:
            page_size = 5

        # Garantindo que o page_number seja um valor positivo
        if page_number <= 0:
            page_number = 1
        
        return page_size, page_number

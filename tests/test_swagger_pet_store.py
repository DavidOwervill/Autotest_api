import requests
import pytest
from base_classes.swagger_io import SwaggerDef
from models.swagger_pet import SwaggerPetSchema

@pytest.mark.parametrize('link_available, link_pending, link_sold',
                         [('https://petstore.swagger.io/v2/pet/findByStatus?status=available',
                           'https://petstore.swagger.io/v2/pet/findByStatus?status=pending',
                           'https://petstore.swagger.io/v2/pet/findByStatus?status=sold')]
                         )
def test_swagger_io_pet_get(link_available, link_pending, link_sold) -> None:
    """
    Важно, перед началом на сайте - https://petstore.swagger.io/#/pet/findPetsByStatus необходимо запустить api
    и затем закрыть, очень важно!
    :return:
    """
    response = requests.get(link_sold)
    SwaggerDef(response).assert_status_code(200)
    SwaggerDef(response).validate_schema(SwaggerPetSchema)

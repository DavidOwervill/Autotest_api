from jsonschema import validate


class SampleApiDef:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_schema(self, schema):
        """
        Данная функция проводит валидацию схемы
        :param schema: schema
        :return: validate schema amd  items in response
        """
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(schema=schema.schema(), instance=item)
        else:
            validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        """
        Данная функция проверяет статус код, принимая на вход необходимое значение
        :param status_code: int
        :return: assert status code in status code
        """
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self

    def __str__(self):
        return f'\nStatus code: {self.response_status_code}' \
               f'\nRequsted url: {self.response.url}'

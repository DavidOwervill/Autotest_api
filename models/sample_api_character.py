from pydantic import BaseModel, validator, Field
from src.enums.sample_api_characters_enum import StatusEnums, GenderEnums
from models.fakers import random_number, random_string, random_url


class SampleApiRMCharacterSchema(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)
    status: StatusEnums = Field(default_factory=random_string)
    species: str = Field(default_factory=random_string)
    type: str = Field(default_factory=random_string)
    gender: GenderEnums = Field(default_factory=random_string)
    origin: str = Field(default_factory=random_string)
    image: str = Field(default_factory=random_url)

    @validator("id")
    def get_validate_id(cls, id):
        if id > 0:
            return id
        else:
            raise ValueError("Id меньше нуля")


if __name__ == "__main__":
    from jsonschema import validate

    schema = SampleApiRMCharacterSchema().schema()
    print(schema)
    ans = [
        {'id': 1, 'name': 'Rick Sanchez', 'status': 'Alive', 'species': 'Human', 'type': 'Human', 'gender': 'Male',
         'origin': 'Earth (C-137)', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'},
        {'id': 2, 'name': 'Morty Smith', 'status': 'Alive', 'species': 'Human', 'type': 'Human', 'gender': 'Male',
         'origin': 'Earth (C-137)', 'image': 'https://rickandmortyapi.com/api/character/avatar/2.jpeg'},
        {'id': 3, 'name': 'Summer Smith', 'status': 'Alive', 'species': 'Human', 'type': 'Human', 'gender': 'Female',
         'origin': 'Earth (Replacement Dimension)', 'image': 'https://rickandmortyapi.com/api/character/avatar/3.jpeg'},
        {'id': 4, 'name': 'Beth Smith', 'status': 'Alive', 'species': 'Human', 'type': 'Human', 'gender': 'Female',
         'origin': 'Earth (Replacement Dimension)', 'image': 'https://rickandmortyapi.com/api/character/avatar/4.jpeg'}
    ]
    for item in ans:
        validate(instance=item, schema=schema)

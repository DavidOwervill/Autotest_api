from pydantic import BaseModel, Field
from models.fakers import random_number, random_string
from src.enums.swagger_enums import PetStoreStatus


class Category(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)


class Tags(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)


class SwaggerPetSchema(BaseModel):
    id: int = Field(default_factory=random_number)
    category: Category | None
    name: str = Field(default_factory=random_string)
    photoUrls: list[str] = Field(default_factory=random_string)
    tags: list[Tags]
    status: PetStoreStatus = Field(default_factory=random_string)




if __name__ == "__main__":
    from jsonschema import validate

    resp = {"id": 9223372016900013000, "category": {"id": 0, "name": "string"}, "name": "fish", "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}], "status": "available"}

    valid = SwaggerPetSchema.parse_obj(resp)
    schema = SwaggerPetSchema.schema()
    print(schema)

    validate(schema=schema, instance=resp)

from pydantic import BaseModel,  Field

from models.fakers import random_number, random_string


class SampleApiRMEpisodesSchema(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)
    air_date: str = Field(default_factory=random_string)
    episode: int = Field(default_factory=random_number)
    season: int = Field(default_factory=random_number)


if __name__ == "__main__":
    from jsonschema import validate

    schema = SampleApiRMEpisodesSchema().schema()
    ans = [
        {'id': 1, 'name': 'Pilot', 'air_date': 'December 2, 2013', 'episode': 1, 'season': 1},
        {'id': 2, 'name': 'Lawnmower Dog', 'air_date': 'December 9, 2013', 'episode': 2, 'season': 1},
        {'id': 3, 'name': 'Anatomy Park', 'air_date': 'December 16, 2013', 'episode': 3, 'season': 1},
        {'id': 4, 'name': 'M. Night Shaym-Aliens!', 'air_date': 'January 13, 2014', 'episode': 4, 'season': 1},
        {'id': 5, 'name': 'Meeseeks and Destroy', 'air_date': 'January 20, 2014', 'episode': 5, 'season': 1},
        {'id': 6, 'name': 'Rick Potion #9', 'air_date': 'January 27, 2014', 'episode': 6, 'season': 1},
        {'id': 7, 'name': 'Raising Gazorpazorp', 'air_date': 'March 10, 2014', 'episode': 7, 'season': 1},
        {'id': 8, 'name': 'Rixty Minutes', 'air_date': 'March 17, 2014', 'episode': 8, 'season': 1},
        {'id': 9, 'name': 'Something Ricked This Way Comes', 'air_date': 'March 24, 2014', 'episode': 9, 'season': 1},
        {'id': 10, 'name': 'Close Rick-counters of the Rick Kind', 'air_date': 'April 7, 2014', 'episode': 10,
         'season': 1},
    ]
    for item in ans:
        validate(schema=schema, instance=item)

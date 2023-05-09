import requests
import pytest
from base_classes.sampleapis_characters import SampleApiDef
from models.sample_api_character import SampleApiRMCharacterSchema
from models.sample_api_episodes import SampleApiRMEpisodesSchema


class TestSampleApi:
    @pytest.mark.parametrize('link, status', [("https://api.sampleapis.com/rickandmorty/characters", 200)])
    def test_get_characters_status_and_val_schema_rm(self, link, status):
        """
        Функция работает с сайтом sampleapis Rick and Morty раздел персонажи, проверяет статус код
        """
        response = requests.get(link)
        SampleApiDef(response).assert_status_code(status)
        SampleApiDef(response).validate_schema(SampleApiRMCharacterSchema)

    @pytest.mark.parametrize('link, status', [("https://api.sampleapis.com/rickandmorty/episodes", 200)])
    def test_get_episodes_status_and_val_schema_rm(self, link, status):
        """
        Функция работает с разделом про персонажей, проверяет статус код и валидирует схему
        :param link: https://api.sampleapis.com/rickandmorty/episodes
        :param status: 200
        """
        response = requests.get(link)
        SampleApiDef(response).assert_status_code(status)
        SampleApiDef(response).validate_schema(SampleApiRMEpisodesSchema)


if __name__ == "__main__":
    requests.Session()
    TestSampleApi.test_get_characters_status_and_val_schema_rm()
    TestSampleApi.test_get_episodes_status_and_val_schema_rm()

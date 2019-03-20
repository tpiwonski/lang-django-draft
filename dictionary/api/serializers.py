from rest_framework.serializers import Serializer, CharField, ChoiceField, UUIDField

from dictionary.models import LANGUAGES


class AddWordSerializer(Serializer):
    word = CharField()
    language = ChoiceField(choices=LANGUAGES)


class TranslationSerializer(Serializer):
    id = UUIDField()


class Translated(Serializer):
    id = UUIDField()
    word = CharField()
    language = ChoiceField(choices=LANGUAGES)


class WordSerializer(Serializer):
    id = UUIDField()
    word = CharField()
    language = ChoiceField(choices=LANGUAGES)
    translations = Translated(many=True)


class AddTranslationSerializer(Serializer):
    source_word_id = UUIDField()
    translated_word_id = UUIDField()

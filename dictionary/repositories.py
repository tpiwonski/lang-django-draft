import uuid

from django.db.models.expressions import Q

from dictionary.models import WordModel, TranslationModel
from dictionary.domain import Word


class WordRepository(object):
    
    @classmethod
    def save(cls, word):
        if word._data._state.adding:
            word._data.save(force_insert=True)
        else:
            word._data.save()

        for translated in word._data.translations:
            cls.save(translated)
            TranslationModel(id=uuid.uuid4(), source=word._data, translated=translated._data).save()

    @classmethod
    def get_by_id(cls, word_id):
        return Word(cls._load_with_translations(WordModel.objects.get(id=word_id)))

    @classmethod
    def get_all(cls):
        return [Word(cls._load_with_translations(word)) for word in WordModel.objects.all()]

    @classmethod
    def find_by_word(cls, word):
        word = WordModel.objects.filter(word__exact=word).first()
        if not word:
            return None

        return Word(cls._load_with_translations(word))

    @classmethod
    def _load_with_translations(cls, word):
        word.translations.extend([
            Word(t.source if t.translated == word else t.translated) 
            for t in TranslationModel.objects.filter(Q(source=word) | Q(translated=word))
        ])
        return word

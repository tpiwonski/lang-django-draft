import uuid

from dictionary.models import TranslationModel


class Entity(object):

    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data.id


class Word(Entity):

    def __init__(self, data):
        super(Word, self).__init__(data=data)

    @property
    def word(self):
        return self._data.word

    @property
    def language(self):
        return self._data.language

    @property
    def translations(self):
        return self._data.translations

    def add_translation(self, word):
        self._data.translations.append(word)



class Translation(Entity):

    def __init__(self, data):
        super(Translation, self).__init__(data)

    @property
    def source(self):
        return self._data.source

    @property
    def translated(self):
        return self._data.translated

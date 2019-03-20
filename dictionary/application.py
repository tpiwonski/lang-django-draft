import uuid

from dictionary.domain import Word
from dictionary.models import WordModel, TranslationModel
from dictionary.repositories import WordRepository


class AddWord(object):
    word_repository = WordRepository

    def execute(self, word, language) -> WordModel:
        word = Word(WordModel(id=uuid.uuid4(), word=word, language=language))
        self.word_repository.save(word)
        return word


class GetWords(object):
    word_repository = WordRepository

    def execute(self):
        return self.word_repository.get_all()


class GetWordByText(object):
    word_repository = WordRepository

    def execute(self, word):
        return self.word_repository.find_by_word(word)


class AddTranslation(object):
    word_repository = WordRepository

    def execute(self, source_word_id, translated_word_id):
        source_word = self.word_repository.get_by_id(source_word_id)
        translated_word = self.word_repository.get_by_id(translated_word_id)
        source_word.add_translation(translated_word)
        self.word_repository.save(source_word)
        return source_word

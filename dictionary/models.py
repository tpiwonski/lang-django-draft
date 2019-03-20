from django.db import models

from dictionary.utils import ModelDiffMixin


LANGUAGE_PL = 'pl'
LANGUAGE_EN = 'en'

LANGUAGES = (
    (LANGUAGE_PL, u'Polish'),
    (LANGUAGE_EN, u'English')
)


class WordModel(models.Model, ModelDiffMixin):
    id = models.UUIDField(primary_key=True)
    word = models.CharField(max_length=255)
    language = models.CharField(max_length=2, choices=LANGUAGES)

    class Meta:
        db_table = 'dictionary_word'
        unique_together = (('word', 'language'),)

    def __init__(self, *args, **kwargs):
        super(WordModel, self).__init__(*args, **kwargs)

        self.translations = []


class TranslationModel(models.Model, ModelDiffMixin):
    id = models.UUIDField(primary_key=True)
    source = models.ForeignKey(WordModel, on_delete=models.CASCADE, related_name='source')
    translated = models.ForeignKey(WordModel, on_delete=models.CASCADE, related_name='translated')

    class Meta:
        db_table = 'dictionary_translation'
        unique_together = (('source', 'translated'),)

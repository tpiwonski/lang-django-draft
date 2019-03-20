from rest_framework.views import APIView, Response

from dictionary.repositories import WordRepository
from dictionary.api.serializers import AddWordSerializer, WordSerializer, AddTranslationSerializer, TranslationSerializer
from dictionary.application import AddWord, GetWords, GetWordByText, AddTranslation


class WordsAPIView(APIView):

    def get(self, request):
        words = GetWords().execute()
        
        return Response(data={
            "data": [WordSerializer(word).data for word in words]
        })

    def post(self, request):
        serializer = AddWordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        word = serializer.validated_data['word']
        language = serializer.validated_data['language']

        word = AddWord().execute(word=word, language=language)

        return Response(data={
            "data": WordSerializer(word).data
        })


class WordAPIView(APIView):

    def get(self, request, word):
        result = GetWordByText().execute(word=word)
        if not result:
            data = None
        else:
            data = WordSerializer(result).data

        return Response(data={
            "data": data
        })


class TranslationAPIView(APIView):

    def post(self, request):
        serializer = AddTranslationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        source_word_id = serializer.validated_data['source_word_id']
        translated_word_id = serializer.validated_data['translated_word_id']

        translation = AddTranslation().execute(source_word_id, translated_word_id)

        return Response(data={
            "data": WordSerializer(translation).data
        })

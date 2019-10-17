from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

        # author 자동으로 채워지도록
        def perform_create(self, serializer):
            serializer.save(author = self.request.user)

class AlbumSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url = True)

    class Meta:
        model = Album
        fields = ('pk', 'image', 'desc', 'author_name')

        # author 자동으로 채워지도록
        def perform_create(self, serializer):
            serializer.save(author = self.request.user)


class FileSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')
    file = serializers.FileField(use_url = True)

    class Meta:
        model = Files
        fields = ('pk', 'file', 'desc', 'author_name')

        # author 자동으로 채워지도록
        def perform_create(self, serializer):
            serializer.save(author = self.request.user)

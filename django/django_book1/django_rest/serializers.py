from rest_framework import serializers

from .models import (Snippet, LANGUAGE_CHOICES, STYLE_CHOICES)


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        create and return a new 'Snippet' instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def updata(self, instance, validated_data):
        """
        update and return an existing 'Snippet' instance, given the validated data.
        """
        for key, value in validated_data.items():
            attr = getattr(instance, key)
            setattr(instance, validated_data.get(key, attr))
        instance.save()
        return instance

class SnippetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        ]
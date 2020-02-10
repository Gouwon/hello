from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (Snippet, LANGUAGE_CHOICES, STYLE_CHOICES)


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')

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
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        ]

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'snippets',
        ]

class SnippetHTMLModelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet_highlight', format='html'
    )

    class Meta:
        model = Snippet
        fields = [
            'url', 'id', 'highlight', 'owner',
            'title', 'code', 'linenos', 'language', 'style',
        ]

class UserHTMLModelSerializer(serializers.HyperlinkedModelSerializer):
    snippets =serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet_detail', read_only=True
    )

    class Meta:
        model = User
        fields = [
            'url', 'id', 'username', 'snippets', 
        ]
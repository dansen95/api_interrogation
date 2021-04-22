from rest_framework import serializers

from .models import Interrogation, Question, Answer


class InterrogationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Interrogation


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Answer

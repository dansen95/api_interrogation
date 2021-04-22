from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Interrogation, Question, Answer
from .permissions import IsAdminOrUserId, IsAdminOrReadOnly
from .serializers import (InterrogationSerializer,
                          QuestionSerializer,
                          AnswerSerializer)


class InterrogationViewSet(viewsets.ModelViewSet):
    queryset = Interrogation.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = InterrogationSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class AnswerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAdminOrUserId]
    serializer_class = AnswerSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']

    def get_queryset(self):
        queryset = Answer.objects.filter(user=self.request.user)
        return queryset

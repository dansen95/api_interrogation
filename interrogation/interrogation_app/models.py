from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Interrogation(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateTimeField(
        "Дата старта", auto_now_add=True
    )
    date_end = models.DateTimeField(
        "Дата окончания"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interrogations"
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT_ANSWER = 'TA'
    ONE_ANSWER = 'OA'
    MULTIPLE_ANSWERS = 'MA'

    ANSWER_TYPE = [
        (TEXT_ANSWER, 'Text answer'),
        (ONE_ANSWER, 'One answer'),
        (MULTIPLE_ANSWERS, 'Multiple answers'),
    ]
    text = models.TextField()
    type = models.CharField(
        max_length=2,
        choices=ANSWER_TYPE,
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="questions"
    )
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    A = models.TextField(blank=True, null=True)
    B = models.TextField(blank=True, null=True)
    C = models.TextField(blank=True, null=True)
    D = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    OPTION_A = 'A'
    OPTION_B = 'B'
    OPTION_C = 'C'
    OPTION_D = 'D'
    ANSWERS = [
        (OPTION_A, 'OPTION A'),
        (OPTION_B, 'OPTION B'),
        (OPTION_C, 'OPTION C'),
        (OPTION_D, 'OPTION D'),
    ]

    text_answer = models.TextField(blank=True, null=True, unique=True)
    first_answer = models.CharField(
        max_length=1, choices=ANSWERS, unique=True, blank=True, null=True
    )
    second_answer = models.CharField(
        max_length=1, choices=ANSWERS, unique=True, blank=True, null=True
    )
    third_answer = models.CharField(
        max_length=1, choices=ANSWERS, unique=True, blank=True, null=True
    )
    fourth_answer = models.CharField(
        max_length=1, choices=ANSWERS, unique=True, blank=True, null=True
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answers"
    )

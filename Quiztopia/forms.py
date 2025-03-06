from django import forms 
from models import Quiz, Question, Answer

class QuizForm(forms.ModelForm):

    title = forms.CharField(max_length=200, help_text="Quiz Name")
    category = forms.CharField(max_length=100, choices=Quiz.categories)
    difficulty = forms.CharField(max_length=100, choices=Quiz.difficulties)
    upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Quiz
        fields = ('title','category','difficulty')

class QuestionForm(forms.ModelForm):

    question_text = forms.CharField(max_length=500, help_text="Enter your question")

    class Meta:
        model = Question
        fields = ('question_text')

class AnswerForm(forms.ModelForm):

    answer_text = forms.CharField(max_length=200, help_text="Enter an answer")
    is_correct = forms.BooleanField()

    class Meta:
        model = Answer
        fields = ('answer_text')

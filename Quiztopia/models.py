from django.db import models

class User(models.Model):

    username = models.CharField(max_length=100, unique=True, primary_key=True)
    profile_picture = models.ImageField(upload_to='',blank=True)
    points = models.IntegerField(default=0)
    quizzes_taken = models.IntegerField(default=0)
    quizzes_created = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class Quiz(models.Model):

    categories = [
        ("Movies And TV" , "Movies And TV"),
        ("Animals" , "Animals"),
        ("General Knowledge" , "General Knowledge"),
        ("Sports" , "Sports"),
        ("Other" , "Other"),
    ]

    difficulties = [
        ("Easy" , "Easy"),
        ("Medium" , "Medium"),
        ("Hard" , "Hard"),
    ]

    quiz_ID = models.CharField(max_length=10, unique=True, primary_key=True)
    quiz_title = models.CharField(max_length=200)
    category = models.CharField(max_length=100,choices=categories)
    difficulty = models.CharField(max_length=100,choices=difficulties)
    upvotes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.quiz_title
    

class Question(models.Model):

    question_ID = models.CharField(max_length=10, unique=True, primary_key=True)
    question_text = models.CharField(max_length=500)
    quiz_ID = models.ForeignKey(Quiz, on_delete=models.CASCADE, to_field='quiz_ID')

    def __str__(self):
        return self.question_text
    
class Answer(models.Model):

    answer_ID = models.CharField(max_length=10, unique=True, primary_key=True)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question_ID = models.ForeignKey(Question, on_delete=models.CASCADE, to_field='question_ID')



    def __str__(self):
        return self.answer_text
    



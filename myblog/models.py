from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=250)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    class Meta:
        db_table = 'Comments'
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('created',)

    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, default="")
    email = models.EmailField(max_length=254, default="")
    text = models.TextField("Текст коментария")
    created = models.DateTimeField("Добавлен", auto_now_add=True)

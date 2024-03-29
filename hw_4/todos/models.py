from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'ID: {self.id} - {self.title}'


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id} - {self.title}'

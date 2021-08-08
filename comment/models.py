from django.db import models
from django.apps import apps
from django.core.validators import MinLengthValidator


# class AbstractComment(models.Model):
#     target = models.ForeignKey(
#         "community.Board", on_delete=models.CASCADE, verbose_name='게시글')
#     user = models.ForeignKey(
#         User, related_name='comment', on_delete=models.CASCADE, verbose_name='유저'
#     )
#     content = models.TextField(verbose_name='내용', validators=[
#         MinLengthValidator(15)])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# Board = apps.get_model(app_label='community', model_name='Board')


class Comment(models.Model):
    target = models.ForeignKey(
        "community.Board", related_name='comment', on_delete=models.CASCADE, verbose_name='게시글')
    user = models.ForeignKey(
        "users.User", related_name='comment', on_delete=models.CASCADE, verbose_name='유저'
    )
    content = models.TextField(verbose_name='내용', validators=[
        MinLengthValidator(15)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False, verbose_name='삭제여부')

    def __str__(self):
        return self.content

    class Meta:
        db_table = '자유게시판 댓글'
        verbose_name = '자유게시판 댓글'
        verbose_name_plural = '자유게시판 댓글'

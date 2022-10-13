from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    title = models.CharField(verbose_name="チケットの名前", max_length=64)
    target_date = models.DateField(verbose_name="実行日")
    is_approval = models.BooleanField(verbose_name="承認フラグ", default=False)
    is_done = models.BooleanField(verbose_name="完了フラグ", default=False)
    created_at = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now=True)
    from_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="発行元ユーザー",
        related_name="+",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="送信先ユーザー",
        related_name="+",
    )

    class Meta:
        db_table = "ticket"

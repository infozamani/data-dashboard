from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دیتاست")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان آپلود")
    column_names = models.JSONField(default=list, verbose_name="اسامی ستون‌ها")
    data = models.JSONField(default=list, verbose_name="داده‌ها (لیست دیکشنری‌ها)")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        ordering = ['-uploaded_at']
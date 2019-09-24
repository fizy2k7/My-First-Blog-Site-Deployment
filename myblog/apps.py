from django.apps import AppConfig
from django.db.models.signals import pre_save


class MyblogConfig(AppConfig):
    name = 'myblog'

    # def ready(self):
    #     import myblog.signals



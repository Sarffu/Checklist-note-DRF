from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  #  specifies the type of primary key field to   use for models in this app if no primary key is explicitly defined.
   
    name = 'core'

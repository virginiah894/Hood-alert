from django.apps import AppConfig

from django.apps import AppConfig
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals



class HoodConfig(AppConfig):
    name = 'hood'

from django.apps import AppConfig


class EcomConfig(AppConfig):
    name = 'ecom'

    def ready(self):
    	import ecom.signals
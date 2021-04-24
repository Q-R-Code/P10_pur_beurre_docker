from django.apps import AppConfig


class CatalogueConfig(AppConfig):
    name = 'catalogue'
    app_label = "my_catalogue"
    print(app_label)
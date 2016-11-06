import inspect
from importlib import import_module

from django.apps import apps
from django.forms.models import modelform_factory

CRUD_APPS = [
    "core",
]

def get_errors(form_errors):
    """Returns compiled form errors"""
    error_list = []
    errors = form_errors.as_data().copy()
    errors = [error_list.append(
        e + ': ' + str(
            list(errors[e][0])[0])) for e in errors]

    return list(set(error_list))


def discover():
    """Returns apps and models configured for CRUD operation"""
    discovered = {}
    for app in CRUD_APPS:
        name = apps.get_app_config(app).name
        discovered[app] = import_module(
            '{}.crud'.format(name)
        ).CRUD_MODELS_CONFIG

    return discovered


def extract_from_url(request, position):
    """Returns app/model from url"""
    return request.path.split('/')[position] if request else None


def get_app_name(request=None, **kwargs):
    """Returns the name of app"""
    return kwargs.get(
        'app_name', extract_from_url(request, 1))


def get_model_name(request=None, **kwargs):
    """Returns the name of model"""
    try:
        return kwargs.get(
            'model_name', extract_from_url(request, 2))
    except IndexError:
        pass


def get_model(**kwargs):
    """Returns model"""
    return apps.get_model(
        get_app_name(**kwargs),
        get_model_name(**kwargs)
    )


def get_model_instance(**kwargs):
    """Returns model instance"""
    return get_model(**kwargs).objects.get(id=kwargs.get("pk"))


def get_form_instance(**kwargs):
    """Returns form instance"""
    fields = []
    field_config = discover()[get_app_name(
        **kwargs)][get_model_name(**kwargs)]
    callee = type(inspect.currentframe().f_back.f_locals['self']).__name__
    operation = 'create' if 'Create' in callee else 'update'

    for field in field_config:
        if operation in field_config[field]:
            fields.append(field)

    return modelform_factory(get_model(**kwargs), fields=fields)

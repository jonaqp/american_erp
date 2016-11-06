from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='url_name')
def url_name(parser):
    url_parse = reverse('{0}'.format(str(parser)))
    return url_parse


@register.filter
def make_breadcrumbs(value):
    crumbs = value.split('/')[3:-1]
    home = 'administrator'
    point_breadcrumbs = u"<i class='fa fa-circle'></i>"

    link = u" <li><a href='{0:s}'>Home</a>{1:s}" \
           u"</li>".format(reverse(home + ':' + 'index'),
                           str(point_breadcrumbs))

    for index, name in enumerate(crumbs):
        if len(crumbs) - 1 == index:
            point_breadcrumbs = ''
        link += u" <li><span>{0:s}</span>" \
                u"</li>{1:s}".format(str(name).capitalize(),
                                     str(point_breadcrumbs))

    return link


@register.filter
def make_breadcrumbs_module(value):
    if value:
        crumbs = value.split('/')[3:-1]
        module = str(crumbs[0])
        return module.upper()


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def subtract_date(value, arg):
    result_date = (value - arg).days
    return result_date
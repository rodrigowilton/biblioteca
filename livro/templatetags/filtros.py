from django import template


register = template.Library()

@register.filter
def mostra_duracao(value1, velue2):
    return (value1-velue2).days

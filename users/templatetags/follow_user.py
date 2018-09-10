from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag(takes_context=True)
def follow_user_button(context):
    user_logado = context.get('user')
    user = context.get('profile')
    user_logado_follow_user = user_logado.following.filter(pk=user.pk).exists()

    if user_logado_follow_user:
        return format_html('Seguindo')
    return format_html('<i class="fas fa-plus"></i> Seguir')
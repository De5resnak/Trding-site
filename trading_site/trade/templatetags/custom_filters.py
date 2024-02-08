from django import template
import re

register = template.Library()

@register.filter(name='center_images')
def center_images(value):
    img_regex = re.compile(r'<img(.*?)>', re.DOTALL)

    def add_center_class(match):
        img_tag = match.group(0)
        if 'class=' in img_tag:
            img_tag = img_tag.replace('class="', 'class="center-image" ')
        else:
            img_tag = img_tag.replace('<img', '<img class="center-image"')
        return img_tag

    return img_regex.sub(add_center_class, value)
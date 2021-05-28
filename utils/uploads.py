
import uuid

from django.utils.safestring import mark_safe


def upload_instance(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return f'uploads/{instance.__class__.__name__}/{filename[2:3]}/{filename}'



# def get_image(self, obj):
#     return  mark_safe(f'<img src={obj.image.url} width="100" height="100"')
import os

from PIL import Image

from django.db.models.fields.files import (ImageField, ImageFieldFile)

FILE_TYPE = ['jpeg', 'jpg', 'png']


class ThumbnailImageFieldFile(ImageFieldFile):
    def _add_thumb(s):
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in FILE_TYPE:
            parts[-1] = 'jpg'
        return '.'.join(parts)
    
    # getter
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)
    
    @property
    def thumb_url(self):
        return self._add_thumb(self.url)
    
    def save(self, name, content, save=True):
        super().save(name, content, save)

        img = Image.open(self.path)
        size = (self.field.thumb_width. self.field.thumb_height)
        img.thumbnatil(size)
        background = Image.new(mode='RGB', size=size, color=(255, 255, 255))
        box = (
            int(
                (size[0] - img.size[0]) / 2
            ), 
            int(
                (size[1] - img.size[1]) / 2
            )
        )
        background.paste(im=img, box=box)
        background.save(fp=self.thumb_path, format='JPEG')
    
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)
    
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(
        self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name=verbose_name, **kwargs)
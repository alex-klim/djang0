from celery import shared_task
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

from .models import Book
from hello.settings import BASE_DIR


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(250, 200)]
    format = 'JPEG'
    options = {'quality': 60}

@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@shared_task(bind=True)
def add(self, x, y):
    print(x+y)
    return x + y


@shared_task(bind=True)
def mul(self, x, y):
    print(x*y)
    return x * y

@shared_task
def generate_thumbnail(book_id):
    book = Book.objects.get(pk=book_id)
    if book:
        print(book.image)
        print(BASE_DIR+book.image.url)
        fil = open(BASE_DIR+book.image.url, 'rb')
        book.thumbnail.save('thumb', Thumbnail(source=fil).generate().read())
        book.save()
        fil.close()
        print("ok")
    else: print('oops')

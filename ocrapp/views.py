from django.shortcuts import render
from .models import Profile
from django.views.generic import View
from django.conf import settings
from PIL import Image
from pytesseract import image_to_string


class ProfileView(View):
    model = Profile

    def get(self, request, *args, **kwargs):
        return render(request, 'image.html')

    def post(self, request, *args, **kwargs):
        pic = self.model()
        try:
            pic.picture = request.FILES.get("picture")
            pic.save()
            filename = pic.picture.name
            text = image_to_string(Image.open(settings.MEDIA_ROOT + '/' + filename))
            # print(text)
        except Exception:
            pass
        return render(request, 'saved.html', locals())

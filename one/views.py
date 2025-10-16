from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import base64
from .getSong import getSongName
from tempfile import NamedTemporaryFile
import os


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")


@csrf_exempt
def getTrack(request):
    if request.method == 'POST':
        print()
    print("Got the form via a POST request")
    if request.FILES:
        print("files exists...")
        audio = request.FILES["audio_data"]
        print(type(request.FILES["audio_data"]))
        content_type = getattr(audio, 'content_type', '') or ''
        suffix = '.webm' if 'webm' in content_type or not content_type else (
            '.wav' if 'wav' in content_type else '.webm'
        )
        with audio.open("rb") as cf:
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(cf.read())
                temp_path = tmp.name

        try:
            result = getSongName(temp_path)
        finally:
            try:
                os.remove(temp_path)
            except Exception:
                pass

        print(result)
        return JsonResponse(result, safe=False)

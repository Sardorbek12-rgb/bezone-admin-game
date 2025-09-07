from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Translation

class TranslationListAPIView(APIView):
    authentication_classes = []  # отключи если не нужно
    permission_classes = []

    def get(self, request):
        lang = request.GET.get('lang', 'ru')
        qs = Translation.objects.all()
        data = {t.key: t.ru if lang == 'ru' else t.uz for t in qs}
        return Response(data)


from django.http import JsonResponse

translations = {
    "ru": {
        "topbar.call1": "Позвонить",
        "topbar.order": "Оформить заявку"
    },
    "uz": {
        "topbar.call1": "Qo‘ng‘iroq qilish",
        "topbar.order": "Ariza yuborish"
    }
}

def get_translations(request):
    lang = request.GET.get("lang", "ru")
    return JsonResponse(translations.get(lang, translations["ru"]))
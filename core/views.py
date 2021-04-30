from django.views.generic import TemplateView, View
from django.http import JsonResponse
import qrcode
import qrcode.image.svg
from io import BytesIO

class Home(TemplateView):
	template_name = 'core/index.html'


class Generate(View):
	
	def get(self, request):
		return JsonResponse({"success": True,"message": "Hello, World!"})

	def post(self,request):
		key = request.POST.get('key', '')

		if key == '':
			return JsonResponse({"success": False, "message": "No input"})

		img = qrcode.make(key, image_factory = qrcode.image.svg.SvgImage, box_size = 20)
		stream = BytesIO()
		img.save(stream)
		svg = stream.getvalue().decode()

		return JsonResponse({"success":True, "message": "QR code ready", "qrcode": svg})
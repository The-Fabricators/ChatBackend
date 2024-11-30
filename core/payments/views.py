import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.payments.serializer import PaymentSerializer
from core.payments.payment import Payment
from django.http import JsonResponse
from core.payments.models import Payment as PaymentModel

class PaymentViewSet(ModelViewSet):


    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            payment = Payment()
            payment = payment.create_payment(data)
            PaymentModel.objects.create(
                payment_id=payment.get("id"),
                user=request.user,
                transaction_amount=payment.get("transaction_amount"),
                date_expiration=payment.get("date_expiration"),
                instalments=payment.get("instalments"),
            )
            return Response(payment)
        except Exception as e:
            return Response(e)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            payment = Payment()
            payment = payment.update_payment(data.get("payment_id"), data)
            return Response(payment)
        except Exception as e:
            return Response(e)

    def get_payment(self, request, *args, **kwargs):
        try:
            payment_id = kwargs.get("payment_id")
            payment = Payment()
            payment = payment.get_payment(payment_id)
            return Response(payment)
        except Exception as e:
            return Response(e)









@csrf_exempt
def webhook_receiver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            if data.get("action") == "payment.updated":
                id = data.get("data").get("id")
                print(f"Payment {id}")
                Payment.update_payment(id)

            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
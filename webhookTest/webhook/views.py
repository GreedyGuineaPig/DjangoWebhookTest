from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe
from ..webhookTest.local_settings import endpoint_secret

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body.decode("utf-8")
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'invoice.payment_failed':
	    print("failed to pay")
    
    return HttpResponse(status=200)
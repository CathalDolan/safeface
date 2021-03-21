from django.http import HttpResponse


# Handling Stripe Webhooks
class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    # Handles generic, unknown or unexpected webhook events
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Handles successful payment intents
    def handle_payment_intent_succeeded(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handles failed payment intents
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

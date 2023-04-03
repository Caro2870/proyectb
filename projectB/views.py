from django.http import HttpResponse
from azure.servicebus import ServiceBusClient
from django.conf import settings

def receive_message(request):
    servicebus_client = ServiceBusClient.from_connection_string(settings.SERVICE_BUS_CONNECTION_STRING)
    receiver = servicebus_client.get_queue_receiver(settings.SERVICE_BUS_QUEUE_NAME)

    messages = receiver.receive_messages(max_message_count=1)
    for msg in messages:
        print(str(msg))
        receiver.complete_message(msg)

    return HttpResponse("Mensaje recibido: " + str(messages[0]) if messages else "No hay mensajes.")

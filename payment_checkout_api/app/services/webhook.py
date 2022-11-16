
import os
import requests
import json
from payment_checkout_api.app.models import schemas

from payment_checkout_api.app.models.schemas import PaymentUpdateStatus


class Webhook():

    WEBHOOK_URL = os.getenv('WEBHOOK_URL', "WEBHOOK_URL_NOT_SET!_VERIFY_YOUR_DOCKER_COMPOSE_FILE!"

    request={}

    # new_json = '{ "type": "AdaptiveCard", "body": [ { "type": "TextBlock", "size": "Medium", "weight": "Bolder", "text": "Payment Status Update", "wrap": true, "style": "heading" }, { "type": "TextBlock", "text": "Great news, Order 1234 has been updated!", "wrap": true }, { "type": "FactSet", "facts": [ { "title": "Previous Status:", "value": "${previous}" }, { "title": "Previous Status:", "value": "${previous}" }, { "title": "Previous Status:", "value": "${previous}" }, { "title": "Previous Status:", "value": "${previous}" } ] }, { "type": "FactSet", "facts": [ { "title": "Actual Status:", "value": "${new}" }, { "title": "Actual Status:", "value": "${new}" }, { "title": "Actual Status:", "value": "${new}" }, { "title": "Actual Status:", "value": "${new}" } ] } ], "actions": [ { "type": "Action.OpenUrl", "title": "View Payments Webapp", "url": "localhost:4200" } ], "$schema": "http://adaptivecards.io/schemas/adaptive-card.json", "version": "1.4" }'
    # new_json2 = '{ "type":"message", "attachments":[ { "contentType":"application/vnd.microsoft.card.adaptive", "contentUrl":null, "content":{ "$schema":"http://adaptivecards.io/schemas/adaptive-card.json", "type":"AdaptiveCard", "version":"1.2", "body":[ { "type": "TextBlock", "text": "For Samples and Templates, see [https://adaptivecards.io/samples](https://adaptivecards.io/samples)" } ] } } ] }'

    def notify_msteams(self, paymentUpdateStatus: PaymentUpdateStatus):
        text=f'Payment ID {paymentUpdateStatus.payment_id} has been updated to {schemas.Status(paymentUpdateStatus.new_status_code).name}'
        self.request["text"]=text
        res=requests.post(self.WEBHOOK_URL, json=self.request)

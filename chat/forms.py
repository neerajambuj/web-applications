from chat.models import Trigger
from django import forms

class BOT(forms.Form):
    network = forms.ChoiceField(label=u'Run the bot', required=True)
    def start_bot():
        run_bot_task.delay()

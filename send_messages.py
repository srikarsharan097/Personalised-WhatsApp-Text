import pywhatkit as kit
from datetime import datetime

contacts = {
    'Contact 1': '+911234567890',
    'Contact 2': '+441234567890'
}

message_template = 'Hello {name}, This message is sent as a personalized text using the pywhatkit terminal.'
 
for name, phone in contacts.items():
    message = message_template.format(name=name)
    now = datetime.now()
    kit.sendwhatmsg(phone, message, now.hour, now.minute + 2)
    print(f'Message scheduled to {name} at {phone}')
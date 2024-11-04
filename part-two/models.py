import logging
from mongoengine import Document, StringField, EmailField, BooleanField, EnumField
from enum import Enum

logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PreferredContact(str, Enum):
    EMAIL = 'email'
    SMS = 'sms'

class Contact(Document):
    full_name = StringField(required=True)
    email = EmailField(required=True)
    phone = StringField()
    preferred_contact = EnumField(PreferredContact, default=PreferredContact.EMAIL)
    message_sent = BooleanField(default=False)
    address = StringField()
    company = StringField()
    position = StringField()
    
    meta = {'collection': 'contacts'}
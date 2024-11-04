import pika
import json
from faker import Faker
from mongoengine import connect
from models import Contact, PreferredContact
import random
import logging
import sys

logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    connect(host="mongodb+srv://goitlearn:FvTP85uVCXJ8443r@cluster0.sdejq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    logger.info("Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    sys.exit(1)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')
    channel.queue_declare(queue='sms_queue')
    logger.info("Successfully connected to RabbitMQ")
except Exception as e:
    logger.error(f"Failed to connect to RabbitMQ: {e}")
    sys.exit(1)

fake = Faker()

def generate_contacts(num_contacts):
    try:
        for i in range(num_contacts):
            contact = Contact(
                full_name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                preferred_contact=random.choice(list(PreferredContact)),
                address=fake.address(),
                company=fake.company(),
                position=fake.job()
            )
            contact.save()
            
            queue_name = 'sms_queue' if contact.preferred_contact == PreferredContact.SMS else 'email_queue'
            
            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=str(contact.id)
            )
            logger.info(f"Contact {i+1}/{num_contacts}: {contact.full_name} added to {queue_name}")
    except Exception as e:
        logger.error(f"Error generating contact: {e}")
        raise

if __name__ == "__main__":
    try:
        generate_contacts(10)
        logger.info("Successfully generated all contacts")
    except Exception as e:
        logger.error(f"Failed to generate contacts: {e}")
    finally:
        connection.close()
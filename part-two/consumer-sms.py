
import pika
from mongoengine import connect
from models import Contact
import time
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

def simulate_sms_sending(contact):
    logger.info(f"Simulating SMS sending to {contact.full_name} at {contact.phone}")
    time.sleep(1)
    return True

def callback(ch, method, properties, body):
    try:
        contact_id = body.decode()
        contact = Contact.objects(id=contact_id).first()
        
        if contact:
            if simulate_sms_sending(contact):
                contact.message_sent = True
                contact.save()
                logger.info(f"SMS sent and status updated for {contact.full_name}")
        else:
            logger.warning(f"Contact with id {contact_id} not found")
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        channel.queue_declare(queue='sms_queue')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='sms_queue', on_message_callback=callback)
        
        logger.info("Started consuming SMS queue. To exit press CTRL+C")
        channel.start_consuming()
    except KeyboardInterrupt:
        logger.info("Shutting down SMS consumer...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == "__main__":
    main()
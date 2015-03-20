import os
from kafka import SimpleProducer, KafkaConsumer, KafkaClient
from kafka.common import LeaderNotAvailableError
import logging

logging.basicConfig()
logger = logging.getLogger('kafka-app')

# Input stream topics
in_streams = ['test-topic', 'topic-b']

# IP:PORT of a Kafka broker. The typical port is 9092.
KAFKA_BROKER_IP_PORT = os.getenv('KAFKA_BROKER', '192.168.86.10:9092')
print "KAFKA BROKER: " + KAFKA_BROKER_IP_PORT
kafka = KafkaClient(KAFKA_BROKER_IP_PORT)
producer = SimpleProducer(kafka)
consumer = KafkaConsumer(*in_streams, group_id="my_group",
                         metadata_broker_list=[KAFKA_BROKER_IP_PORT])


for message in consumer:
    # message is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.decode('utf-8')`
    execute(message)

# kafka.close()

def execute(message):
	# IMPLEMENT THIS
	print message

def emit(topic, msg):
	"""
	topic : string
	msg : string
	"""
	try:
		producer.send_messages(topic, msg)
	except LeaderNotAvailableError:
		logger.warning('Caught a LeaderNotAvailableError. This seems to happen when auto-creating a new topic.')
		print('Caught a LeaderNotAvailableError. This seems to happen when auto-creating a new topic.')

def close():
	kafka.close()
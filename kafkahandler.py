from logging import StreamHandler
from mykafka import MyKafka

class KafkaHandler(StreamHandler):

    def __init__(self, broker, topic):
        StreamHandler.__init__(self)
        self.broker = broker
        self.topic = topic

        # Kafka Broker Configuration
        self.kafka_broker = MyKafka(broker)

    def emit(self, record):
        msg = self.format(record)
        self.kafka_broker.send(msg, self.topic)
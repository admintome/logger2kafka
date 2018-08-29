from kafka import KafkaProducer
import json


class MyKafka(object):

    def __init__(self, kafka_brokers, json=False):
        self.json = json
        if not json:
            self.producer = KafkaProducer(
                bootstrap_servers=kafka_brokers
            )
        else:
            self.producer = KafkaProducer(
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                bootstrap_servers=kafka_brokers
            )

    def send(self, data, topic):
        if self.json:
            result = self.producer.send(topic, key=b'log', value=data)
        else:
            result = self.producer.send(topic, bytes(data, 'utf-8'))
        print("kafka send result: {}".format(result.get()))



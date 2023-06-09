import json
import logging.config
import logging
import pickle
import yaml
import redis


with open(path, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
topic_name1 = "ultrasound_data_topic"
topic_name2 = "vibration_data_topic"
logger = logging.getLogger('redis')
r = redis.Redis(host='localhost', port=6379, db=0)


def create_consumer_data(topic_name):
    convert_data = r.get(topic_name)
    print("convert type", type(convert_data))
    print(bool(convert_data))
    consumer_data = pickle.loads(convert_data)
    return consumer_data


def print_consumer(consumer_data):
    logging.debug("data read to redis: ", consumer_data)
    print(" %s", consumer_data)


consumer_data1 = create_consumer_data(topic_name1)
print("\nsound_data\n")
print_consumer(consumer_data1)
print("\nvibration_data\n")
consumer_data2 = create_consumer_data(topic_name2)
print_consumer(consumer_data2)

from confluent_kafka import Producer


p = Producer({'bootstrap.servers': '13.235.120.21:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

some_data_source = ['a', 'b', 'c', 'd']
for data in some_data_source:
    p.poll(0)
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

p.flush()

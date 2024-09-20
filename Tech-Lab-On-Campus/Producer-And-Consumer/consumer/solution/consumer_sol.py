# this line imports pika which establishes the RabbitMQ Consumer
import pika
from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):

# consumer that is instantiating the class
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str):
        # body of constructor
        self.setupRMQConnection(exchange_name, exchange_type, binding_key, on_message_callback)

    def setupRMQConnection(queue_name, exchange_name, exchange_type, 
    binding_key, on_message_callback): 

        # connection parameters to set up initial connection
        connection_params = pika.ConnectionParameters('localhost')

        # This connection acts as the "bridge" between your application
        #  and the RabbitMQ broker
        connection = pika.BlockingConnection(connection_params)

        # opening a channel
        channel = connection.channel()

        # declare the exchange and directs your messages to the right queue
        channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

        channel.queue_declare(queue=queue_name)

        # binds the queue to the exchange, step 3
        channel.queue_bind(routing_key=binding_key, exchange=exchange_name, queue=queue_name,)

        # call back function, tells RabbitMQ that the consumer is ready to receive messages, core of consumer
        channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback, auto_ack=True)

        # keeps the consumer continuously listening to messages without stopping
        channel.start_consuming()

        def on_message_callback(ch, method, properties, body):
            print(" Consumer is working!")



        # closing the connection and channel
        connection.close()
        channel.close()
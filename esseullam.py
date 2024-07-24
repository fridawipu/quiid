import pika

# Set the connection parameters to connect to RabbitMQ on localhost
# using the default virtual host ("/") and the default credentials ("guest" / "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

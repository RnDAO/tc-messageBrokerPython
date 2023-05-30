from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue


if __name__ == "__main__":
    broker_url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    rabbit_mq = RabbitMQ(
        broker_url=broker_url, port=port, username=username, password=password
    )

    rabbit_mq.connect(Queue.DISCORD_BOT)

    content = {"data": {"guildId": "993163081939165234"}}

    rabbit_mq.publish(
        Queue.DISCORD_ANALYZER, event=Event.DISCORD_ANALYZER.RUN, content=content
    )

from tc_messageBroker.rabbit_mq.saga.transactions import (
    DISCORD_SCHEDULED_JOB_TRANSACTIONS,
    DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
    DISCORD_FETCH_MEMBERS_TRANSACTIONS,
)
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.status import Status


def test_discord_update_channels_tx():
    tx = DISCORD_UPDATE_CHANNELS_TRANSACTIONS

    assert len(tx) == 3
    assert tx[0].order == 1
    assert tx[0].queue == Queue.DISCORD_BOT
    assert tx[0].event == Event.DISCORD_BOT.FETCH
    assert tx[0].status == Status.NOT_STARTED

    assert tx[1].order == 2
    assert tx[1].queue == Queue.DISCORD_ANALYZER
    assert tx[1].event == Event.DISCORD_ANALYZER.RUN
    assert tx[1].status == Status.NOT_STARTED

    assert tx[2].order == 3
    assert tx[2].queue == Queue.DISCORD_BOT
    assert tx[2].event == Event.DISCORD_BOT.SEND_MESSAGE
    assert tx[2].status == Status.NOT_STARTED


def test_discord_scheduled_job_tx():
    tx = DISCORD_SCHEDULED_JOB_TRANSACTIONS

    assert len(tx) == 1
    # assert tx[0].order == 1
    # assert tx[0].queue == Queue.DISCORD_BOT
    # assert tx[0].event == Event.DISCORD_BOT.FETCH
    # assert tx[0].status == Status.NOT_STARTED

    assert tx[0].order == 1
    assert tx[0].queue == Queue.DISCORD_ANALYZER
    assert tx[0].event == Event.DISCORD_ANALYZER.RUN_ONCE
    assert tx[0].status == Status.NOT_STARTED


def test_discord_bot_fetch_tx():
    tx = DISCORD_FETCH_MEMBERS_TRANSACTIONS

    assert len(tx) == 1

    assert tx[0].order == 1
    assert tx[0].queue == Queue.DISCORD_BOT
    assert tx[0].event == Event.DISCORD_BOT.FETCH_MEMBERS
    assert tx[0].status == Status.NOT_STARTED

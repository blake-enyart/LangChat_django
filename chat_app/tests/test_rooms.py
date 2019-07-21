from django.contrib.auth import get_user_model
from django.test import Client
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
from nose.tools import assert_equal, assert_is_none, assert_is_not_none, assert_true
import pytest

from LangChat.routing import application
from chat_app.models import Room


TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


@database_sync_to_async
def create_user(
    *,
    username='rider@example.com',
    password='pAssw0rd!'
):
    # Create user.
    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )
    user.save()
    return user


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
class TestWebsockets:

    async def test_authorized_user_can_connect(self, settings):
        # Use in-memory channel layers for testing.
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS

        # Force authentication to get session ID.
        client = Client()
        user = await create_user()

        client.force_login(user=user)

        # Pass session ID in headers to authenticate.
        communicator = WebsocketCommunicator(
            application=application,
            path='/ws/chat_app/',
            headers=[(
                b'cookie',
                f'sessionid={client.cookies["sessionid"].value}'.encode('ascii')
            )]
        )
        connected, _ = await communicator.connect()
        assert_true(connected)
        await communicator.disconnect()

import pytest
from unittest.mock import AsyncMock
from bot.main import bot  # Import your bot instance if needed

pytestmark = pytest.mark.asyncio

# Test the greet command with a mocked context
async def test_greet_command(mocker):
    # Create a mock context object
    ctx = AsyncMock()
    ctx.send = AsyncMock()  # Mock the send method

    # Call the command
    await bot.greet(ctx, "Bob")

    # Check if ctx.send was called with the correct response
    ctx.send.assert_awaited_with("Hello, Bob!")
import pytest
from bot.commands import greet_user, add_numbers

# Mark the test file as asyncio-compatible
pytestmark = pytest.mark.asyncio

# Test the greet_user function
async def test_greet_user():
    result = await greet_user("Alice")
    assert result == "Hello, Alice!"

# Test the add_numbers function
async def test_add_numbers():
    result = await add_numbers(3, 5)
    assert result == 8

# Test edge case for add_numbers
async def test_add_numbers_negative():
    result = await add_numbers(-2, 7)
    assert result == 5
@pytest.fixture
def mock_context():
    ctx = AsyncMock()
    ctx.send = AsyncMock()
    return ctx

async def test_greet_command_with_fixture(mock_context):
    await bot.greet(mock_context, "Charlie")
    mock_context.send.assert_awaited_with("Hello, Charlie!")
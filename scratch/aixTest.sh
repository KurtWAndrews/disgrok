curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer xai-o0TedMCX7rhRYQ90l8zkW1sQ89a40W8CbnTZX11VdjOHqUCZy8XuiKja0ptcSa8IxOnQWFFF7Jj0tIHG" -d '
{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and nothing else."
    }
  ],
  "model": "grok-2-latest",
  "stream": false,
  "temperature": 0
}'
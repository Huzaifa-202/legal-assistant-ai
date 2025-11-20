from app import create_app

# Gunicorn with aiohttp will call this async function
# Do NOT use asyncio.run() here
app = create_app

from pathlib import Path

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from environs import Env
from redis.asyncio import Redis

BASE_DIR = (Path(__file__).resolve()).parent


env = Env()
env.read_env('.env')

BOT_TOKEN = env.str('BOT_TOKEN')
USE_REDIS = env.bool("USE_REDIS")
PROXY = env.str('PROXY')

ADMIN_IDS = [12345678, ]

redis = Redis(host='redis://127.0.0.1', port=6379)
storage = RedisStorage(redis=redis) if USE_REDIS else MemoryStorage()
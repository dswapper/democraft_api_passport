import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = os.environ['TELEGRAM_DATABASE_URI'].replace('postgresql://', 'postgresql+asyncpg://')
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

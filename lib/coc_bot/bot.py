import logging
import os
import traceback

import coc
import discord
from discord.ext import commands


DEVELOPER_EMAIL_COC_API = os.environ.get('DEVELOPER_EMAIL_COC_API')
DEVELOPER_PASSWORD_COC_API = os.environ.get('DEVELOPER_PASSWORD_COC_API')
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')


bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
coc_client = coc.login(
    DEVELOPER_EMAIL_COC_API,
    DEVELOPER_PASSWORD_COC_API,
    key_names="coc.py tests",
    client=coc.EventsClient,
)

logging.basicConfig(level=logging.ERROR)

from coc_bot.commands import clans, players
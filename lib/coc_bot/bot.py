import logging
import os
import traceback

import coc
import discord
from discord.ext import commands

from coc_bot.ssm import ssm

DEV_SITE_EMAIL = ssm.get_parameter_by_name("DEV_SITE_EMAIL")
DEV_SITE_PASSWORD = ssm.get_parameter_by_name("DEV_SITE_PASSWORD")
DISCORD_BOT_TOKEN = ssm.get_parameter_by_name("DISCORD_BOT_TOKEN")


bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
coc_client = coc.login(
    DEV_SITE_EMAIL,
    DEV_SITE_PASSWORD,
    key_names="coc.py tests",
    client=coc.EventsClient,
)

logging.basicConfig(level=logging.ERROR)

from coc_bot.commands import clans, players
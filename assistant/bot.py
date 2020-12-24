# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["bot", "START_TIME"]

import time

from pyrogram import Client

from . import Config, logging

_LOG = logging.getLogger(__name__)
START_TIME = time.time()

plugins = dict(root="assistant.plugins")
bot = Client(
    'Damien Soukara',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)

_LOG.info("assistant-bot initialized!")

#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

EMOJI_TO_DAY = {
    '1⃣': 'Monday',
    '2⃣': 'Tuesday',
    '3⃣': 'Wednesday',
    '4⃣': 'Thursday',
    '5⃣': 'Friday',
    '6⃣': 'Saturday',
    '7⃣': 'Sunday',
}

async def _send_question(question):
    await client.wait_until_ready()
    channel = client.get_channel(int(os.environ.get('CHANNEL_ID')))
    message = await channel.send(question)
    for reaction in EMOJI_TO_DAY:
        await message.add_reaction(reaction)
    await client.logout()

def _get_poll_question():
    question = ['Weaboo whenday?']
    for emoji, day in EMOJI_TO_DAY.items():
        question.append('{}:{}'.format(emoji, day))
    return '\n'.join(question)

def main(event, context):
    question = _get_poll_question()
    client.loop.create_task(_send_question(question))
    client.run(os.environ.get('BOT_TOKEN'))

    return {'response': 'poll delivered'}
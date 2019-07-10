#!/usr/bin/env python3

import os

import discord
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

async def send_text(text):
    await client.wait_until_ready()
    channel = client.get_channel(os.environ.get('CHANNEL_ID'))
    await client.send_message(channel, text)
    await client.logout()

def lambda_polly(event, context):
    with open('poll_question.txt', 'r') as f:
        poll_question = f.read()
    client.loop.create_task(send_text(poll_question))
    client.run(os.environ.get('BOT_TOKEN'))

    return {'response': 'poll delivered'}

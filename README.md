# polly
An automated poll question!

An AWS Lambda function that logs into a Discord bot and posts a custom poll question.

## Setup
First, set up your environment

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then add your bot token/channel ID to the `.env` file


Then, format the poll question you want posted in `polly/poll_question.txt`.

## Build

To build your lambda function, run:

```
python setup.py ldist
```

A .zip file will be generated in `/dist`.

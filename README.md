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

Add your bot token/channel ID to the `.env` file and source it
```
source .env
```

## Run
```
python polly/polly.py
```

## Build
```
python setup.py ldist
```

A .zip file will be generated in `/dist`.

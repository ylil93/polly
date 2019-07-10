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

Add your bot token/channel ID to the `.env` file
```
vim .env
```

## Test/Run
```
python polly/polly.py
```

## Build
```
python setup.py ldist
```

A .zip file will be generated in `/dist`.

## Troubleshooting
For mac users using Python 3.6+
```
Cannot connect to host discordapp.com:443 ssl:True [Can not connect to discordapp.com:443 [[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

Navigate to your `Applications/Python 3.6/` folder and double click the `Install Certificates.command`
Detailed explanation [here](https://github.com/Rapptz/discord.py/issues/423#issuecomment-272093801).
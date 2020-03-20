# ModelWatch

## Getting Started
__ModelWatch__ sends model training progress updates to your Slack channel. No SDK required, the script simply checks a folder that you pass in at your desired notification interval, and uploads the newest file in that folder to Slack.

## Installation

First you need to install the Slack App

After installation, an Oauth token will be posted to your Slack channel, which you'll need to run the script.

Then install requirements and run the modelwatch.py script while training your model.

```bash
(modelwatch) $ pip install -r requirements.txt
```

## Arguments
- __interval__: notification interval in minutes

- __folder__: path to folder with preview files

- __token__: Slack access token

- __channel__: ID of Slack channel to upload files

## Usage

Run modelwatch.py in the background or else the thread may get blocked and you won't receive the updates at the expected interval.

On Windows:

```bash
> start python modelwatch.py
```

On macOS/Linux:

```bash
$ python modelwatch.py &
```  

## LATEST UPDATES

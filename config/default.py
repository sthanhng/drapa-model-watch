import os

from yacs.config import CfgNode as CN


_C = CN()

_C.WORKSPACE = CN()
# Base directory path
_C.WORKSPACE.BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

_C.MODELWATCH = CN()
# Notification interval in minutes
_C.MODELWATCH.INTERVAL = 1
# Path to folder with preview files
_C.MODELWATCH.DIR = os.path.join(_C.WORKSPACE.BASE_DIR, 'logs')
# Slack access token
_C.MODELWATCH.TOKEN = "YOU_OAUTH_TOKEN"
# ID of Slack channel to upload files
_C.MODELWATCH.CHANNEL = "YOUR_CHANNEL_ID"

cfg = _C

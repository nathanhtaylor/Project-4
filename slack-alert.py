import os
from slackclient import slackclient

slack_token = os.environ["xoxb-522948478901-583357389586-3cWfxNKoXNjGWCmDOZDSgrGs"]
sc = SlackClient(slack_token)

sc.api_call(
    "chat.postMessage",
    chennel="#botspam-tcm",
    text="TESTING -Matt"
)
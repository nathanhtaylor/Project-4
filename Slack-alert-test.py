import requests
import json
web_hook_url = 'https://hooks.slack.com/services/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'

x = 6

slack_msg = {'text': x }

requests.post(web_hook_url,data=json.dumps(slack_msg))
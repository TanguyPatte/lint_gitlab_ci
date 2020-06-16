#!/usr/bin/env python
import requests
import json
import yaml

url = 'https://gitlab.com/api/v4/ci/lint'
ci_file = open(".gitlab-ci.yml", "r")
ci_content = yaml.safe_load(ci_file.read())

payload = {'content': '{}'.format(ci_content)}

response = requests.post(url, data = payload)
body = json.loads(response.text)
if body["status"] == "invalid":
  print(".gitlab-ci.yml invalid")
  for error in body["errors"]:
    print(error)
    exit(1)
else:
  print(".gitlab-ci.yml valid")

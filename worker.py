from flask import Flask, request, redirect
from flask_slackbot import SlackBot
from firebase import firebase
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

import twilio.twiml
import time

sc = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")
sc.rtm_connect()
while True:
    messages = sc.rtm_read()
    for m in messages:
        if m["type"] == "message":
            client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(to="+" + "12134469422", from_="+12139153611",
                                             body=m["text"])
            
    time.sleep(0.5)

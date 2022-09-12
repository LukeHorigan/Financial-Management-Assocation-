# import the required libraries
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
import time
import os
from fpdf import FPDF
import datetime
from base64 import b64decode
import pandas as pd
import email
from bs4 import BeautifulSoup


# Define the SCOPES. If modifying it, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def getEmails():
    print("getEmails running")
    # Variable creds will store the user access token.
    # If no valid token found, we will create one.
    creds = None

    # The file token.pickle contains the user access token.
    # Check if it exists
    if os.path.exists('token.pickle'):
        # Read the token from the file and store it in the variable creds
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If credentials are not available or are invalid, ask the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the access token in token.pickle file for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Connect to the Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # request a list of all the messages
    result = service.users().messages().list(userId='me').execute()

    # We can also pass maxResults to get any number of emails. Like this:
    # result = service.users().messages().list(maxResults=200, userId='me').execute()
    messages = result.get('messages')

    # messages is a list of dictionaries where each dictionary contains a message id.
    print(messages)
    # iterate through all the messages
    for msg in messages:
        # Get the message from its id
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()


        # Use try-except to avoid any Errors
        try:
            # Get value of 'payload' from dictionary 'txt'
            payload = txt['payload']
            headers = payload['headers']
            # Look for Subject and Sender Email in the headers
            #change the sender to Vital Knowledge later, and put in a variable for the subject

            print(headers)
            print("\n")
            #if (sender == '"Lucas Horigan (RIT Student)" <lah9270@rit.edu>'):
            print(headers['value'])
            if (headers["value"]) == '<lah9270@g.rit.edu>':
                print("passed logic conditional")
                # The Body of the message is in Encrypted format. So, we have to decode it.
                # Get the data and decode it with base 64 decoder.
                parts = payload.get('parts')[0]
                data = parts['body']['data']
                data = data.replace("-", "+").replace("_", "/")
                decoded_data = base64.b64decode(data, validate= True)
                html_print = decoded_data.decode('UTF-8')
                #print(html_print)
                html_print = html_print.replace('\n','<br>')
                #print(html_print)
                save_path = "C:/Users/Lhorigan/PycharmProjects/egon"
                complete = os.path.join(save_path,"sample.html")
                file = open(complete, "w")
                file.write(html_print)
                file.close()                                #os.path is taking the download default save and moving to the egon folder for the discord side to grab it

            else:
                print("HTML did not write")

        except:
            pass

getEmails()

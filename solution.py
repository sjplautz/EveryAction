import json
import requests
from requests.models import HTTPBasicAuth
from config import credentials, api_url

"""
Retrieves the entire collection of emails available at the BrodcastEmails endpoint
"""
def getEmails() -> json:
    # single API call caps out at 25 emails
    emailBatch = fetchEmailBatch(api_url)
    emails = emailBatch['items']

    # if there are more emails yet to be retrieved
    if('nextPageLink' in emailBatch.keys()):
        # keep fetching batches of emails until there is no next page link
        while(emailBatch['nextPageLink'] is not None):
            emailBatch = fetchEmailBatch(emailBatch['nextPageLink'])
            emails.extend(emailBatch['items'])

    return emails


"""
Fetches a batch of up to 25 emails from the specified url endpoint
"""
def fetchEmailBatch(url: str) -> json:
    return requests.get(
        url,
        auth=HTTPBasicAuth(credentials['username'], credentials['api_key'])
    ).json()


"""
Prints the formatted email results from a list of emails
"""
def printResults(emails: json) -> None:
    for email in emails:
        print(f'{email["emailMessageId"]} "{email["name"]}"')

    print('\nTotal:', len(emails), 'emails')


def main():
    emails = getEmails()
    printResults(emails)


if __name__ == "__main__":
    main()

# только для служебного пользования
# самой классной командой в компании
​
import warnings
warnings.filterwarnings("ignore")
​
from jira.client import JIRA
import argparse
import click
from datetime import datetime
 
​
# Get key by meeting
def keyOfMeeting(meeting):
​
    if meeting == 'daily':
        return ['DRIVEN-3953']
    
    elif meeting == 'retro':
        return ['DRIVEN-3955']
    
    elif meeting == 'backlog':
        return ['DRIVEN-3952']
    
    elif meeting == 'other':
        return ['DRIVEN-3958']
    
    else:
        print ("ERROR! You shoud choose right meeting name: daily, retro, backlog, other")
        exit(1)
​
​
# Initialize parser
parser = argparse.ArgumentParser()
 
​
# Adding required argument
parser.add_argument("-l", "--Login", help = "Use your Jira login", required=True)
parser.add_argument("-p", "--Password", help = "Use your Jira password", required=True)
parser.add_argument("-t", "--Total", help = "Total hours you are spent on tasks, for e.g. 2 or 0.5", required=True)
parser.add_argument("-s", "--Started", help="Moment when the work is logged (format: YYYY-MM-DD)", required=False)
parser.add_argument("-c", "--Comment", help = "Comment on log", required=True)
parser.add_argument("-k", "--Keys", nargs='+', help = "Keys of tasks, separated with spaces, you whant to log, for e.g. DRIVEN-4244 DRIVEN-4245", required=False)
parser.add_argument("-m", "--Meeting", help = "Meetings: daily, retro, backlog, other", required=False)
​
​
# Read arguments from command line
args = parser.parse_args()
​
​
# Check what we have to deal with Meeting or Keys?
if not args.Keys:
    if not args.Meeting:
        print ("ERROR! You shoud choose -k keys or -m Meeting")
        exit(1)
    else:
        keys = keyOfMeeting(args.Meeting)
else:
    keys = args.Keys
​
# Convert the 'started' argument to a datetime object if provided
if args.Started:
    try:
        pre_started_datetime = args.Started + "T00:00:00.000+0000"
        started_datetime = datetime.strptime(pre_started_datetime, "%Y-%m-%dT%H:%M:%S.000+0000")
    except ValueError:
        print("ERROR! Invalid 'started' datetime format. Use the format: YYYY-MM-DDTHH:MM:SS.000+0000")
        exit(1)
else:
    # If 'started' argument is not provided, use the current datetime as default
    started_datetime = datetime.now().strptime(args.Started, "%Y-%m-%dT%H:%M:%S.000+0000")
​
# count worklog 
time = float(args.Total)
timePart = round(time / len(keys), 2)
timePartText = '{}h'.format(timePart).replace('.',',')
​
# Create client and connect to JIRA
jira_client = JIRA(options={'server':'https://jira.app.local','verify':False}, basic_auth=(args.Login, args.Password))
​
# for nice output
print ('\n')
​
# Show issues to worklog
for issueKey in keys:
    issue = jira_client.issue(issueKey)
    print ('In issue {}: {} will be loged – {} hours'.format(issueKey, issue.fields.summary, timePartText))
​
# for nice output
print ('\n')
​
if click.confirm('Do you want to continue?', default=False):
    print("Let's do this for you!")
    # for nice output
    print ('\n')
​
    for issueKey in keys:
        issue = jira_client.issue(issueKey)
        jira_client.add_worklog(issue,timeSpent=timePartText,comment=args.Comment,started=started_datetime,)
        print ('Logging in issue {} - DONE!'.format(issueKey))
    
    # for nice output
    print ('\n')
    print("Have a nice day!")
else:
    print ('\n')
    print ("Goodbye!")

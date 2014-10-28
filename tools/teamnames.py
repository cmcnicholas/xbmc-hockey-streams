from BeautifulSoup import BeautifulSoup
import urllib2, json

# xbmc-hockey-streams
# author: craig mcnicholas
# contact: craig@designdotworks.co.uk

print '# XBMC Hockey Streams Team Names #'
print 'Script to strip short team names from the web!'

# Team names definition
url = 'http://en.wiktionary.org/wiki/Appendix:English_names_of_sports_teams'

# Setup request and get response, workaround to send headers
# so that wikipedia lets us get content, we dont do this often
# only once every few months so hopefully not a problem
request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(request)
page = response.read()
response.close()

print 'Got response, parsing team data...'

# Setup team dictionary
teams = {}

soup = BeautifulSoup(page)

# Find div
div = soup.find('div', {'id': 'mw-content-text'})
if div == None:
    print 'Failed to find div, cannot get teams'
    exit

# Find rows
for tr in div.findAll('tr'):
    tds = tr.findAll('td')

    # Strip out header
    if tds == None or len(tds) < 2:
        continue

    # Add teams
    teams[tds[1].text.lower()] = tds[0].text

# Get file handle
print 'Creating output file...'
f = open('teams.json', 'w')

# Output
print 'Converting to json...'
f.write(json.dumps(teams, sort_keys = True, indent = 4, separators = (',', ': ')))

print 'Closing file...'
f.close()

print 'Success!'

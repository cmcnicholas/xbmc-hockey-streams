import hockeystreams

# xbmc-hockey-streams
# author: craig mcnicholas
# contact: craig@designdotworks.co.uk

print '# XBMC Hockey Streams Unit Tests #'
print 'I need some information before running these tests!'

# Get username and password
username = raw_input("Username: ")
password = raw_input("Password: ")

# Test logging in
session = hockeystreams.login(username, password)

print "Session: " + str(session)

# Test ip exception
ipException = hockeystreams.ipException(session)

print "IP Exception: " + str(ipException)

# Test ip check
ipCheck = hockeystreams.checkIp(username)

print "IP Check: " + str(ipCheck)

# Test retrieving the available archived game dates
dates = hockeystreams.availableDates(session)

print "Available Dates: " + ', '.join(map(str, dates))

# Test retrieving a single dates events
events = hockeystreams.eventsForDate(session, dates[0])

print "Events: " + '\n'.join(map(str, events))

# Test retrieving a map of event stream urls
streams = hockeystreams.eventStream(session, events[0])

if streams == None:
    print 'Stream: None'
else:
    for stream in streams:
        url = streams[stream]
        print 'Stream: (' + stream + ') ' + (url if url != None else 'None')

# Test retrieving teams
teams = hockeystreams.teams(session)

print "Teams: " + ', '.join(map(str, teams))

# Test retrieving events for a team

events = hockeystreams.eventsForTeam(session, teams[20])

print "Events: " + '\n'.join(map(str, events))

# Test retrieving future and live events

liveOrFuture = hockeystreams.liveEvents(session)

print "Live/Future: " + '\n'.join(map(str, liveOrFuture))

# Test retrieving stream url if available
if len(liveOrFuture) > 0:
    for event in liveOrFuture:
        if event.isLive:
            streams = hockeystreams.eventStream(session, event)
            if streams == None:
                print 'Stream: None'
            else:
                for stream in streams:
                    url = streams[stream]
                    print 'Stream: (' + stream + ') ' + (url if url != None else 'None')

# Test short team lookup

teamName = 'Phoenix Coyotes'
shortName = hockeystreams.shortTeamName(teamName, '')
print "Short Name For '" + teamName + "': " + (shortName if shortName != None else 'None')

# Test short team lookup (different casing)

teamName = 'phoenix COYOTES'
shortName = hockeystreams.shortTeamName(teamName, '')
print "Short Name For '" + teamName + "': " + (shortName if shortName != None else 'None')

# Test short team lookup (doesn't exist)

teamName = 'I Dont Exist!'
shortName = hockeystreams.shortTeamName(teamName, '')
print "Short Name For '" + teamName + "': " + (shortName if shortName != None else 'None')


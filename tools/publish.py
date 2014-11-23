import os, sys, zipfile, urllib
from xml.dom import minidom

def do_zip(xbmcName, version):

    # Create zip file name
    zipFilePath = 'xbmc-hockey-streams.' + xbmcName + '.' + version + '.zip'
    print 'Packaging the following files into ' + zipFilePath

    # Create file list to add to archive
    fileList = []
    fileList.append('addon.' + xbmcName + '.xml')
    fileList.append('changelog.txt')
    fileList.append('license.txt')
    fileList.append('default.py')
    fileList.append('hockeystreams.py')
    fileList.append('utils.py')
    fileList.append('icon.png')
    fileList.append('fanart.jpg')

    # Append resources directory and all files
    for base, dirs, files in os.walk('resources'):
        for file in files:
            filePath = os.path.join(base, file)
            if not '.svn' in filePath:
                fileList.append(filePath)

    # Print out the files
    print '\n'.join(fileList)

    # Create zip file
    zipFile = zipfile.ZipFile(zipFilePath, 'w')
    for fileName in fileList:
        if fileName.startswith('addon.'):
            zipFile.write(fileName, arcname = os.path.join('xbmc-hockey-streams', 'addon.xml'))
        else:
            zipFile.write(fileName, arcname = os.path.join('xbmc-hockey-streams', fileName))
    zipFile.close()
    print 'Zip file created! Testing archive is valid...'

    # Test zip file
    zipFile = zipfile.ZipFile(zipFilePath, 'r')
    result = zipFile.testzip()
    if result is not None:
        print 'The zip archive is invalid, problem with file: ' + result
        sys.exit(1)
    zipFile.close()

    print 'xbmc-hockey-streams version ' + version + ' packaged successfully!'



# Find version number from xml
print 'Reading xbmc-hockey-streams version'
dom = minidom.parse(urllib.urlopen('addon.gotham.xml'))
version = dom.getElementsByTagName('addon')[0].getAttribute('version')
print 'Version is ' + version

do_zip('gotham', version)
do_zip('pre-gotham', version)

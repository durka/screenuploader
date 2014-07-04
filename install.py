#!/usr/bin/env python
import sys, os, getpass, subprocess

import config
config_vars = ('INSTALL_PREFIX', 'WATCH_PATH', 'SERVER_NAME', 'SERVER_DIR', 'URL_PREFIX')
CONFIG = {var: config.__dict__[var] for var in config_vars}

# make sure all the config values are filled in
def check_config():
    def ask_create(n):
        if not os.path.exists(CONFIG[n]):
            print '%s: %s does not exist. Create it? [y/N] ' % (n, CONFIG[n]),
            if raw_input().lower() in ['y', 'yes']:
                os.makedirs(CONFIG[n])
                print '\tCreated.'
            else:
                raise '%s does not exist' % n

    for k, v in CONFIG.iteritems():
        if v == '':
            raise '%s undefined' % k

    ask_create('INSTALL_PREFIX')
    ask_create('WATCH_PATH')

# apply config and copy files into place
def install():
    locations = {
            'screenuploader.sh': (CONFIG['INSTALL_PREFIX'], 0755),
            'screenuploader.plist': ('/Users/%s/Library/LaunchAgents' % getpass.getuser(), 0644)
            }

    for filename, (destpath, perms) in locations.iteritems():
        with open(filename, 'r') as f:
            contents = f.read()
        for key, value in CONFIG.iteritems():
            contents = contents.replace('__%s__' % key, value)
        dest = os.path.join(destpath, filename)
        with open(dest, 'w') as f:
            f.write(contents)
        os.chmod(dest, perms)
        print 'Installed %s.' % filename

    if '\tscreenuploader\n' in subprocess.check_output(['launchctl', 'list']):
        # depends on screenuploader.plist being last in locations{} above
        subprocess.check_output(['launchctl', 'unload', dest])
        print 'Unloaded launch agent.'
    subprocess.check_output(['launchctl', 'load', dest])
    print 'Loaded launch agent.'

    print 'Finished!'

def main(argv):
    debug = '--debug' in argv

    try:
        check_config()
    except Exception, e:
        print 'Configuration error: %s' % e
        if debug:
            raise
        else:
            return 1

    try:
        install()
    except Exception, e:
        print 'Installation error: %s' % e
        if debug:
            raise
        else:
            return 1

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))


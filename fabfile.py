import fabric.api as fab


@fab.task
def develop():
    fab.local('virtualenv env')
    fab.local('./env/bin/pip install Markdown')
    fab.local('./env/bin/pip install --pre pytz')
    fab.local('./env/bin/pip install pelican')
    fab.local('./env/bin/pip install pelican-youtube')

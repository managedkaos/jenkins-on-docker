import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

with open(f"{settings.XML_DIR}/folders/base/config.xml") as config_file:
    config = config_file.read()

for team in settings.TEAMS:
    if j.job_exists(team):
        print("\tFolder exists; skipping: %s" % team)
    else:
        try:
            print("\tCreating folder: %s" % team)
            j.job_create(team, config)
        except JenkinsError as e:
            print("\tERROR: %s" % e)

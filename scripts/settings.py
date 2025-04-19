import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

XML_DIR = os.path.join(BASE_DIR, "scripts","xml")

#teams = ['Blazers', 'Bobcats', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pistons', 'Raptors', 'Rockets', 'Sixers', 'Spurs', 'Suns', 'Thunder', 'Timberwolves', 'Warriors', 'Wizards']
TEAMS = ['Cyclones', 'Clippers', 'Hawks', 'Heat', 'Hornets', 'Lakers', 'Magic', 'Warriors']

JOBS = ['BUILD', 'TEST', 'DEPLOY']

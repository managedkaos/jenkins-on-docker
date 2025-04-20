import os
from jenkinsapi.jenkins import Jenkins

def get_plugin_details(server):
    for plugin in server.get_plugins().values():
        print(f"# {plugin.shortName}")
        print(f"\tLong Name  : {plugin.longName}")
        print(f"\tVersion    : {plugin.version}")
        print(f"\tURL        : {plugin.url}")
        print(f"\tActive     : {plugin.active}")
        print(f"\tEnabled    : {plugin.enabled}")

if __name__ == '__main__':
    server = Jenkins(
        os.environ['ENDPOINT'],
        username=os.environ['USERNAME'],
        password=os.environ['PASSWORD'])

    print(server.version)
    get_plugin_details(server)

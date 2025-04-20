import os
import requests

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

XML_DIR = os.path.join(BASE_DIR, "scripts","xml")

TEAMS = [
  'Cyclones',
  'Clippers',
  'Hawks',
  'Heat',
  'Hornets',
  'Lakers',
  'Magic',
  'Warriors'
]

JOBS = ['BUILD', 'TEST', 'DEPLOY']


FOLDER_CONFIG_TEMPLATE = """<?xml version='1.1' encoding='UTF-8'?>
<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@6.18">
  <actions/>
  <properties/>
  <folderViews class="com.cloudbees.hudson.plugins.folder.views.DefaultFolderViewHolder">
    <views>
      <hudson.model.AllView>
        <owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../.."/>
        <name>All</name>
        <filterExecutors>false</filterExecutors>
        <filterQueue>false</filterQueue>
        <properties class="hudson.model.View$PropertyList"/>
      </hudson.model.AllView>
    </views>
    <tabBar class="hudson.views.DefaultViewsTabBar"/>
  </folderViews>
  <healthMetrics>
    <com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>
      <nonRecursive>false</nonRecursive>
    </com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>
  </healthMetrics>
  <icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/>
</com.cloudbees.hudson.plugins.folder.Folder>"""

JOB_CONFIG_TEMPLATE = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>"""


def get_jenkins_headers(endpoint, username, password):
    """Get Jenkins headers for API requests.

    Args:
        endpoint (str): Jenkins server URL
        username (str): Jenkins username
        password (str): Jenkins password or API token

    Returns:
        dict: Headers dictionary with Content-Type and Authorization
    """
    headers = {
        'Content-Type': 'application/xml',
    }

    return headers

def check_item_exists(endpoint, username, password, item_path):
    """Check if a Jenkins item (folder or job) exists.

    Args:
        endpoint (str): Jenkins server URL
        username (str): Jenkins username
        password (str): Jenkins password or API token
        item_path (str): Path to the item (e.g., 'folder' or 'folder/job')

    Returns:
        bool: True if item exists, False otherwise
    """
    try:
        response = requests.get(
            f"{endpoint}/job/{item_path}/api/json",
            auth=(username, password)
        )
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

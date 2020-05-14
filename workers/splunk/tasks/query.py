from workers.splunk.api.splunk import Splunk
from workers import app

@app.task(name='search.modules.splunk.sourcetypes')
def get_sourcetypes(earliest_time: str, latest_time: str):
    ''' Run splunk query to get sourcetypes'''
    query = '| metadata type=sourcetypes index=*'
    get_sourcetypes = Splunk(app_context='ThreatHunting').search(query, earliest_time)
    return get_sourcetypes


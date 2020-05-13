from workers.splunk.api.splunk import Splunk
from workers import app

@app.task(name='search.query.splunk.run')
def get_agents(query: str, earliest_time: str, latest_time: str):
    ''' Run splunk query '''
    # Examples, ignore
    query = 'search `sysmon` event_id=1 |stats earliest(_time) as first_seen, last(_time) as last_seen by host_name'
    Splunk(app_context='ThreatHunting').search(query, '-900d')
    print('test')


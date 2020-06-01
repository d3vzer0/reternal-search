from workers.splunk.api.splunk import Splunk
from workers import app

@app.task(name='search.age.splunk.run')
def get_indice_stats(earliest_time: str, latest_time: str):
    ''' Run splunk query to get average delay by source_type '''
    query = 'index=_internal metrics group=per_sourcetype_thruput| stats avg(avg_age) as avg_age by series| rename series as sourcetype'
    get_age_stats = Splunk().search(query, earliest_time)
    return get_age_stats


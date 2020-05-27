from workers.splunk.api.splunk import Splunk
from workers import app

@app.task(name='search.indices.splunk.run')
def get_indice_stats(earliest_time: str, latest_time: str):
    ''' Run splunk query to get sourcetype by index and source '''
    query = '| tstats values(sourcetype) AS sourcetype where index=* group by index, source| mvexpand sourcetype'
    get_indices_stats = Splunk().search(query, earliest_time)
    return get_indices_stats


from workers.environment import config
import splunklib.client as client
import splunklib.results as results
import functools
import logging

empirelog = logging.getLogger('rtsplunk')

# Generic EMPIRE API class
class Splunk:
    def __init__(self, host=config['SPLUNK_HOST'], port=config['SPLUNK_PORT'], app_context=config['SPLUNK_APP'],
        token=config['SPLUNK_TOKEN']):
        self.service = client.connect(host=host, app=app_context, port=port, splunkToken=token)

    def search(self, query, earliest_time, latest_time='now'):
        ''' Get search results from Splunk API '''
        search_job = self.service.jobs.export(query,
            earliest_time=earliest_time,  latest_time=latest_time, 
            search_mode="normal"
        )
        reader = results.ResultsReader(search_job)
        result_rows = [result for result in reader if isinstance(result,dict)]
        return result_rows
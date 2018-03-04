import elasticsearch
import logging
class StatsCollector(object):
    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger('esops.statscollector')
        self.stats_info = {}

    def get_stats(self):
        client=elasticsearch.Elasticsearch()


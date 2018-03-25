import logging
import time
import os
from esops.config import *
from esops.utils import *
from apscheduler.schedulers.background import BackgroundScheduler


class StatsCollector(object):
    def __init__(self):
        self.logger = logging.getLogger('esops.statscollector')

    def stats(self):
        source_elasticsearch_hosts = get_config('source.elasticsearch', 'HOSTS')
        target_elasticsearch_hosts = get_config('target.elasticsearch', 'HOSTS')
        source_client = get_client(hosts=source_elasticsearch_hosts)
        target_client = get_client(hosts=target_elasticsearch_hosts)
        record_stats_info(source_client=source_client, target_client=target_client)

    def collector(self):
        scheduler = BackgroundScheduler()
        interval = get_config('scheduler', 'INTERVAL')
        scheduler.add_job(self.stats, 'interval', seconds=int(interval))

        scheduler.start()

        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        try:

            # This is here to simulate application activity (which keeps the main thread alive).

            while True:
                time.sleep(2)

        except (KeyboardInterrupt, SystemExit):

            # Not strictly necessary if daemonic mode is enabled but should be done if possible

            scheduler.shutdown()
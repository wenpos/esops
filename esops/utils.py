import elasticsearch
import logging
from .exceptions import *
logger = logging.getLogger(__name__)

def get_stats_info(client):
    """
    Get the current list of indices from the cluster.

    :arg client: An :class:`elasticsearch.Elasticsearch` client object
    :rtype: map
    """
    try:

        stats = client.nodes.stats()
        for node in stats['nodes']:
            if stats['nodes'][node]['name'] == name:
                logger.debug('Found node_id "{0}" for name "{1}".'.format(node, name))
                return node
        logger.error('No node_id found matching name: "{0}"'.format(name))
        return None
    except Exception as e:
        raise FailedExecution('Failed to get indices. Error: {0}'.format(e))

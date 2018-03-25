import json

import elasticsearch
import logging

from esops.exceptions import *
logger = logging.getLogger(__name__)


def get_client(**kwargs):
    """
    Return an :class:`elasticsearch.Elasticsearch` client object using the
    provided parameters. Any of the keyword arguments the
    :class:`elasticsearch.Elasticsearch` client object can receive are valid,
    such as:

    :arg hosts: A list of one or more Elasticsearch client hostnames or IP
        addresses to connect to.  Can send a single host.
    :type hosts: list
    :arg hostd: ip or domain
    :type hostd: str
    :arg port: The Elasticsearch client port to connect to.
    :type port: int
    :type timeout: int
    :rtype: :class:`elasticsearch.Elasticsearch`
    """
    if 'host' in kwargs and 'hosts' in kwargs:
        raise ConfigurationError(
            'Both "host" and "hosts" are defined.  Pick only one.')
    elif not 'host' in kwargs and not 'hosts' in kwargs:
        raise ConfigurationError(
            '"host" or "hosts" are needed.  '
            '"host" together with "port", "hosts" listed "host:port", '
            'Pick only one.')
    if 'hosts' in kwargs and not 'host'in kwargs:
        kwargs['hosts'] = ensure_list(kwargs['hosts'])
    logger.info("kwargs = {0}".format(kwargs))
    try:
        client = elasticsearch.Elasticsearch(**kwargs)
        return client
    except Exception as e:
        raise elasticsearch.ElasticsearchException(
            'Unable to create client connection to Elasticsearch.  '
            'Error: {0}'.format(e)
        )


def ensure_list(indices):
    """
    Return a list, even if indices is a single value

    :arg indices: A list of indices to act upon
    :rtype: list
    """
    if not isinstance(indices, list):  # in case of a single value passed
        indices = [indices]
    return indices


def record_stats_info(source_client, target_client):
    """
    Bulk index the es status information to a specific Elasticsearch cluster.

    :arg source_client: An :class:`elasticsearch.Elasticsearch` client object
    :arg target_client: An :class:`elasticsearch.Elasticsearch` client object
    :rtype: map
    """
    bulk = []
    try:
        stats = source_client.nodes.stats()
        for node in stats['nodes']:
            node_status = stats['nodes'][node]
            doc_id = node + "-" + str(node_status['timestamp'])
            node_status = json.dumps(node_status)
            bulk.append({"index": {"_index": ".esops", "_type": "status", "_id": doc_id}})
            bulk.append(node_status)
            target_client.bulk(bulk, refresh=True)
    except Exception as e:
        raise FailedExecution('Failed to save node status info. Error: {0}'.format(e))

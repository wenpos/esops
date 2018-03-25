import configparser


def get_config(section, attr):
    """
        Get Elasticsearch config from config/config.ini.

        :arg section: An :str: section name
        :arg attr: An :str: attribution name in the section
        :rtype: object
    """
    config = configparser.ConfigParser()
    config.read('../config/config.ini')
    attribution_value = config[section][attr]
    return attribution_value


if __name__ == '__main__':
    hosts = get_config('source.elasticsearch','HOSTS')
    print(hosts)

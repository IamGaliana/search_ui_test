__author__ = 'gaoyanjun'
import ConfigParser
from log_handler import *

conf = ConfigParser.ConfigParser()


class ConfigHanlder(object):

    def __init__(self, configfile='search_query.cfg'):
        conf.read(self.configfile)

    # sections: ['sec_b', 'sec_a']
    def get_config_section(self):
        sections = conf.sections()
        log_info('sections:', sections)
        return sections

    # options: ['a_key1', 'a_key2']
    def get_config_options(self, section):
        options = conf.options(section)
        log_info('options of section %s: %s' % (section, options))
        return options

    # sec_a: [('a_key1', '20'), ('a_key2', '10')]
    def get_config_kvs(self,  section):
        kvs = conf.items(section)
        log_info('key value paris of section %s: %s' % (section, kvs))
        return kvs

    def get_str_value(self, section, option):
        str_val = conf.get(section, option)
        return str_val

    def get_int_value(self, section, option):
        int_val = conf.getint(section, option)
        return int_val

    def get_float_value(self, section, option):
        float_val = conf.getfloat(section, option)
        return float_val

    def get_boolean_value(self, section, option):
        boolean_val = conf.getboolean(section, option)
        return boolean_val

    def update_option(self, section, option, new_val):
        conf.set(section, option, new_val)
        conf.write(open(self.config_file, 'w'))

    def update_section(self, section, new_option, new_val):
        conf.set(section, new_option, new_val)
        conf.write(open(self.config_file, 'w'))

    def add_section(self, section, option, val):
        conf.add_section(section)
        conf.set(section, option, val)
        conf.write(open(self.config_file, 'w'))
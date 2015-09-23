#!/usr/bin/env python

import argparse
import commands

try:
    import json
except ImportError:
    import simplejson as json


class LXCInventory(object):

    def __init__(self):

        self.BASE_LXC_CMD = 'lxc-ls'
        self.BASE_LXC_IP_CMD = ' --fancy -F ipv4 %s | tail -1'
        self.BASE_LXC_STATE_CMD = ' --fancy -F state %s | tail -1'

        self.inventory = {}
        self.read_cli_args()

        self.inventory = self.get_containers()

        if self.args.list:
            print json.dumps(self.inventory)

    def get_containers(self):

        containers = []
        container_list = {}

        all_containers = self.execute_command(self.BASE_LXC_CMD).split()

        #check to ensure name format complies
        for item in all_containers:
            if '-' in item:
                containers.append(item)

        #init our roles
        for item in containers:
            container_list[item.split('-')[1]] = {}
            container_list[item.split('-')[1]]['hosts'] = {}

        #fill in the rest
        for item in containers:

            ip_address = self.execute_command(self.BASE_LXC_CMD + self.BASE_LXC_IP_CMD % item).strip()
            state = self.execute_command(self.BASE_LXC_CMD + self.BASE_LXC_STATE_CMD % item).strip()

            container_list[item.split('-')[1]]['hosts'][ip_address] = {}
            container_list[item.split('-')[1]]['hosts'][ip_address]['vars'] = {'State': state}

        return container_list

    def execute_command(self, cmd):

        return commands.getoutput(cmd)

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        self.args = parser.parse_args()


# Run Scalr Inventory
LXCInventory()

"""
Contains some base primitives that provide basic flow logic for the messages.

Based on a stripped down version of base.py in ActivityWatch.
"""


from abc import abstractmethod
import json
import logging

import threading
from datetime import datetime, timedelta

from typing import Iterable, List, Set

class Event(dict):
    """
    Used to represents an message.
    """
    def __init__(self, **kwargs):
        dict.__init__(self)

        self.update(kwargs)

        msg = ""
        msg += "Logged event '{}':".format(tags)
        msg += "  Type: {}".format(self["type"])
        msg += "  Started: {}".format(self["start"])
        msg += "  Ended: {}".format(self["end"])
        msg += "  Duration: {}".format(self.duration)
        if "cmd" in self:
            msg += "  Command: {}".format(self["cmd"])
        logging.debug(msg)

    def to_json_str(self) -> str:
        data = self.to_json_dict()
        return json.dumps(data)

from queue import Queue
class Agent(threading.Thread):
    _mailbox= Queue()
    _subscriptions = ["system_shutdown"]

    def post (self, msg):
        self._mailbox.put(msg)

    def next_event(self):
        return self._mailbox.get()

    @property
    def subscriptions(self):
        return self._subscriptions

    @abstractmethod
    def run(self):
        pass

    def stop(self):
        raise NotImplementedError

    @property
    def identifier(self):
        """Identifier for agent, used in settings and as a module name shorter than the class name"""
        return self.name[0:-len(self.agent_type)].lower()

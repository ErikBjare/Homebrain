from homebrain import Agent, Event
import requests

class SimLampHandler(Agent):
    """Listens to a trigger event, and sends a toggle command via REST to the simulated lamp hardware on the given url"""
    def __init__(self, url, target=None):
        super(SimLampHandler, self).__init__()
        self.target = target if target is not None else self.identifier
        self.url = url

    def run(self):
        while True:
            event = self.next_event()
            outgoing_event=Event(type="toggle_lamp", data={'data': event['data']})
            requests.request("POST", self.url, json=outgoing_event.to_json_str())

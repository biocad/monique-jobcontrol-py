import json


class JobcontrolConfig:
    def __init__(self,
                 queue_host,
                 from_queue_port):
        self.queue_host = queue_host
        self.from_queue_port = from_queue_port

    def queue_sub_address(self):
        """Returns formatted SUB address to receive messages from queue."""
        return "tcp://{}:{}".format(self.queue_host, self.from_queue_port)

    def queue_push_address(self):
        """Returns formatted PUSH address to send messages to queue."""
        return "tcp://{}:{}".format(self.queue_host, self.from_queue_port + 1)


def read_config(path_to_config):
    """Parses and returns configuration from чfile."""
    data = json.load(open(path_to_config))
    deploy = data['deploy']['monique']
    queue_host = deploy['queue_host']
    queue_port = deploy['queue_port']
    return JobcontrolConfig(queue_host, queue_port)

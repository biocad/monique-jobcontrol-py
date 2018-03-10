import zmq
import argparse
import threading
import json
from monique_jobcontrol_py.config import read_config
from monique_worker_py.qmessage import qmessage_from_json, create_qmessage
from monique_worker_py.task import create_task_id, create_task


class Jobcontrol:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--config', required=True, help='Path to config file')
        args = parser.parse_args()
        self.config = read_config(args.config)

    def run(self):
        """Runs application"""

        print("Connecting to queue...")
        # setup connection
        context = zmq.Context()

        # Socket to receive messages from queue
        from_queue = context.socket(zmq.SUB)
        from_queue.connect(self.config.queue_sub_address())

        # Subscribe to all messages (just for now, later selector will be added)
        from_queue.setsockopt(zmq.SUBSCRIBE, b"")

        # Socket to send messages to queue
        to_queue = context.socket(zmq.PUSH)
        to_queue.connect(self.config.queue_push_address())

        print("Connected to queue.")

        # Run thread to listen every messages from queue
        thread_listen = threading.Thread(target=listen_queue, args=(from_queue,))
        thread_listen.start()

        # Run thread to create new message and push it to queue
        thread_push = threading.Thread(target=push_to_queue, args=(to_queue,))
        thread_push.start()


def listen_queue(from_queue):
    """Listen queue and print every message from it in 3 lines:
       TAG:  envelops to efficient filter messages (http://zguide.zeromq.org/page:all#Pub-Sub-Message-Envelopes)
       MSG:  full QMessage that comes from queue
       CONTENT: parsed insides from QMessage (just to find it simpler)
    """
    while True:
        [address, in_message] = from_queue.recv_multipart()
        qmessage = qmessage_from_json(in_message)
        task_json = qmessage.cnt.contents.to_json()
        print('<<< TAG: {}\n'
              '    MSG: {}\n'
              'CONTENT: {}'.format(address.decode('utf8'),
                                   in_message.decode('utf8'),
                                   task_json.decode('utf8')))


def print_help():
    print("run <spec> <path to JSON file with task config>")


def push_to_queue(to_queue):
    """Listen user, creates Task from <spec> and <file to config>.
       Pay attention that file to config means file to Task config, not this application config.
    """
    print("Press <Enter> to print command format...")
    while True:
        try:
            command = input().split()
            if len(command) == 3 and command[0] == "run":
                task_id = create_task_id()
                task_user = "00000000-0000-0000-0000-000000000000"
                task_spec = command[1]
                with open(command[2], 'r') as file:
                    task_text = file.read()
                task_config = json.loads(task_text)
                task = create_task(task_id, task_user, task_spec, task_config)
                qmessage = create_qmessage(task)
                print('>>> {}'.format(qmessage.to_json().decode('utf8')))
                to_queue.send(qmessage.to_json())
            else:
                print_help()
        except Exception as e:
            print("Error happened: {}".format(str(e)))

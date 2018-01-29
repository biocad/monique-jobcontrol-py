# monique-jobcontrol-py
Simple jobcontrol for Monique System (Python)

## build
Library `pyzmq` required. It can be installed with command
```bash
pip3 install pyzmq
```

Library with worker wrapper required. It can be downloaded [here](https://github.com/biocad/monique-worker-py) and installed from inside of the directory with command
```bash
python3 setup.py install
```

Then jobcontol can be installed on your system from current directory with command
```bash
python3 setup.py install
```

## config.json
This file contains configurations for the app.
It has to be enough for local testing.

## run examples
Run all needed services for Monique (for example, Scheduler and Controllers).
For this moment it can be done with docker-container.

* Run all needed services from [monique repository](https://github.com/biocad/monique-queue) (but not workers).

* Run example worker from [this](https://github.com/biocad/monique-worker-py) repo.


* Run jobcontrol with command
  ```bash
  python3 monique_jobcontrol_py --config config.json
  ```

Last command will run 2 threads:
1. First thread listen every message from queue and print it.

1. Second thread will listen your commands. 
Press <Enter> to see expected format for the commands.
To run task for worker with name `exampleA` just type:
```bash
run exampleA examples/exampleA.json
``` 
to run task that should return `completed` message back and
```bash
run exampleA examples/exampleA-fail.json
```
to run task that should return `failed` message bask (to see why look into config and worker code).

 
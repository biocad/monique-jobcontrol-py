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
File with configurations for the app.
It has to be enough for local testing.

## run examples
Run all needed services for Monique (for example, Scheduler and Controllers).
For this moment it can be done with docker-container.
Run all needed services from [monique repository](https://github.com/biocad/monique-queue) (but not workers).

Run worker with following commands:
```bash
python3 examples/exampleA.py --config examples/configA.json
```
 
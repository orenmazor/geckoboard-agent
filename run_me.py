import daemon
from geckoboard_agent import run

with daemon.DaemonContext():
	run()
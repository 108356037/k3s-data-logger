#!/usr/bin/python3.8
import os
import glob
import sys
import subprocess
import shlex
from pathlib import Path


chart_path = str(Path(__file__).resolve().parent.parent)+'/'

values_files = (glob.glob(chart_path+"*Values.yaml"))

action = sys.argv[1]

if action=="install" or action=="upgrade":
    for _ in range(len(values_files)):
        deploy_name = "water-data-logger-"+str(_+1)
        process = subprocess.run(['/usr/sbin/helm', action, deploy_name, "--values", values_files[_], chart_path],
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True)
        print(process.stdout)

elif action=="uninstall":
    cmd1 = shlex.split("helm list")
    cmd2 = shlex.split("cut --delimiter=' ' --fields=1")
    process = subprocess.Popen(
        cmd1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process = subprocess.run(
        cmd2, stdin=process.stdout, stdout=subprocess.PIPE)
    process.stdout = process.stdout.decode().split('\n')

    for _ in process.stdout:
        _ = _.rstrip('\tdefault')
        if _.find("water") != -1:

            deploy_name = _
            process = subprocess.run(['/usr/sbin/helm', action, deploy_name],
                                     stdout=subprocess.PIPE,
                                     universal_newlines=True)
            print(process.stdout)
else:
    sys.stderr.write("Module Error: Only supports install/upgrade/uninstall currently.")
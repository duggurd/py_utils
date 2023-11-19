import argparse
from io import TextIOWrapper
import os
import string
import sys
import time
import psutil
import subprocess


def MeasureEfficiency(args):
    StartMeasurement(args[1])
    # ExecuteProgram()
    # StopMeasurement()
    # ShowResult()
    
def StartMeasurement(executeFile):
    cmd = ParseExecuteFile(executeFile)
    with open(f"measurements/{executeFile}Measurement.csv", "w") as csvFile:
        pid = subprocess.Popen(["cmd.exe", f"/c {cmd} ."]).pid
        
        measuredProcess = psutil.Process(pid)

        start_time = time.time()
        csvFile.write(str(start_time) + "\n")
        try:
            WriteToCsv(measuredProcess, csvFile)
        except psutil.NoSuchProcess:
            pass
        finally:
            end_time = time.time()
            csvFile.write(str(end_time - start_time) + "\n")
            print(end_time - start_time)
            csvFile.close()

def ProcessMeasurementsToCsv(process: psutil.Process): 
    return ",".join(
    [repr(process.cpu_times()),
    "cpu_percent=" + repr(process.cpu_percent()),
    repr(process.io_counters()),
    repr(process.memory_full_info()),
    "memory_percent=" + repr(process.memory_percent()),
    repr(process.num_ctx_switches())]
    )

def WriteToCsv(process: psutil.Process, file: TextIOWrapper):
    while process.is_running():
        file.write(ProcessMeasurementsToCsv(process) + "\n")

def ParseExecuteFile(path: string): 
    if not os.path.exists("measurements"):
        os.mkdir("measurements")
    elif ".py" in path:
        return "py " + path
    elif os.path.exists(path + "/Cargo.toml"):
        return f"cd {path} & cargo build & cargo run"
    elif ".rs" in path:
        return f"rustc {path} & main.exe"
    elif ".exe" in path:
        return path
    elif ".net" in os.path.curdir:
        return "dotnet build & dotnet run"
    else:
        print(f"'{path}' is not a valid path to a supported file")
        exit(1)

def Main(args):
    MeasureEfficiency(args)

if __name__ == "__main__":
    Main(sys.argv)

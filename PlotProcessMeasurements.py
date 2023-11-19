from matplotlib import pyplot as plt
import numpy as np

def LoadData(pathToFile):
    measurements = {}
    with open(f"{pathToFile}", "r") as file:
        file.readline()
        i = 0
        for line in file:
            measurements[i] = ParseMeasurementLine(line)
            i+=1
        file.close

    return measurements

def ParseMeasurementLine(line: str):
    data = line.split(",")
    cleanedData = {}
    # data = line.replace("\n", "")
    for datapoint in data:
        if "(" in datapoint:
            datapoint = datapoint.split("(")[1]
        datapoint = datapoint.replace(")", "")
        datapoint = datapoint.replace("\n", "")
        datapoint = datapoint.replace(" ", "")
        split = datapoint.split("=")
        try:
            cleanedData[split[0]] = split[1]
        except:
            pass
    return cleanedData

def ExtractMemoryPercent(measurements: dict):
    memoryPercent = np.empty([len(measurements) - 1], float)
    i = 0
    for measurement in measurements.values():
        try:
            dat = float(measurement["memory_percent"])
            memoryPercent[i] = dat
            i += 1
        except:
            pass
    return memoryPercent

def Plot(x: np.array, y: np.array):
    plt.plot(x, y)
    plt.show()

def main():
    memperc = ExtractMemoryPercent(LoadData("measurements/main.exeMeasurement.csv"))
    print(memperc)
    x = np.arange(len(memperc))
    Plot(x, memperc)
main()
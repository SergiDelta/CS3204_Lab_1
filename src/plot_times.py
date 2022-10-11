import numpy as np
import matplotlib.pyplot as plt
import csv


f = open("./execution_time_host.csv", "r") 
reader = csv.reader(f)
times_result_host = np.array(list(reader)[0]).astype(np.float64)
f.close()

f = open("./execution_time_vm.csv", "r") 
reader = csv.reader(f)
times_result_vm = np.array(list(reader)[0]).astype(np.float64)
f.close()

f = open("./execution_time_docker.csv", "r") 
reader = csv.reader(f)
times_result_docker = np.array(list(reader)[0]).astype(np.float64)
f.close()

n = len(times_result_host)

plt.figure()    
plt.plot(np.arange(2, n+2), times_result_host, "b")
plt.plot(np.arange(2, n+2), times_result_vm, "r")
plt.plot(np.arange(2, n+2), times_result_docker, "g")
plt.grid()
plt.xlabel("$N$")
plt.ylabel("$Time$ (s)")
plt.legend(["Host machine", "VM", "Docker"])
plt.title("Execution time of N-dimensional matrix multiplication")



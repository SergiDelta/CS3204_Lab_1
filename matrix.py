import numpy as np
import time
import csv

def matrix(n):
    
    times_result = []
    
    for count in range(2, n+1):           # Matrix dimension in each iteration
        
        A = np.random.rand(count, count)  # Generate random matrices A,B
        B = np.random.rand(count, count)
        
        start_time = time.time()
        result = np.zeros((count,count))
        
        for i in range(0, count):         # Compute matrix multiplication
            for j in range(0, count):
                row_sum = 0
                for k in range(0, count):
                    row_sum = row_sum + A[i][k] * B[k][j]
                result[i][j] = row_sum
                
        end_time = time.time()
        
        diff_time = end_time - start_time
        
        times_result.append(diff_time)
        
        print(f"N = {count} - Time = {diff_time} s")
        
    f = open("./execution_time.csv", "w") # Export results to a csv file
    writer = csv.writer(f)
    writer.writerow(times_result)
    f.close()
    
    
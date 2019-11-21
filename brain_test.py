import numpy as np
import subprocess

# create input file
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# know the expected result
expected = np.zeros(20)
expected[-1] = 1.0

# execute python program
subprocess.run(['python', 'sagital_brain.py'])
result = np.loadtxt("brain_average.csv", delimiter=",")

# check if arrays resut and expected are equal
np.testing.assert_array_equal(result, expected)

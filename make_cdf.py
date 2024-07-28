import numpy as np
import matplotlib.pyplot as plt

title_name = 'Insert Title Here'
x_label = 'Insert X Label Here'
y_label = 'Insert Y Label Here'
want_grid = True
output_file = 'cdf_testing.pdf'
nums = [1, 3, 3, 7, 10]

unique_vals, counts = np.unique(nums, return_counts=True)

cumulative_counts = np.cumsum(counts)

cdf = cumulative_counts / cumulative_counts[-1]

plt.plot(unique_vals, cdf, marker='o', linestyle='-', color='b')
plt.title(title_name)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid(want_grid)
plt.savefig(output_file)
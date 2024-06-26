import statistics

# List of infected patients per day
infected_patients = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Calculate statistics
minimum = min(infected_patients)
maximum = max(infected_patients)
range = maximum - minimum
mean = statistics.mean(infected_patients)
median = statistics.median(infected_patients)
variance = statistics.variance(infected_patients)
std_dev = statistics.stdev(infected_patients)

# Display statistics
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
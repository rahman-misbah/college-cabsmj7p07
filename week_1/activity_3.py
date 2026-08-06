# Event logs
log1_events = ["A101", "B202", "C303", "A101", "D404"]
log2_events = ["C303", "E505", "F606", "B202"]

# Unique events in each log
log1_unique = set(log1_events)
log2_unique = set(log2_events)

# Common logs
log_common = log1_unique & log2_unique
log_all = log1_unique | log2_unique

print("Common Logs:", log_common)
print("All Logs:", log_all)
# input user
hour = int(input("Enter Value hour : "))

# process
minute = 60
second = 3600

result_minute = hour * minute
result_seconds = hour * second

# output
print(f"{hour} hour is equal to {result_minute:,} minute or {result_seconds:,} second")
from datetime import datetime

# input user
first_time_string = str(input("Masukan jam pertama (H:M:S) : "))
second_time_string = str(input("Masukan jam kedua (H:M:S) : "))

# proses
first_datetime = datetime.strptime(first_time_string, "%H:%M:%S")
second_datetime = datetime.strptime(second_time_string, "%H:%M:%S")
time_delta = second_datetime - first_datetime

# output
print("-"*25)
print(f"Jam Ke-1 {first_time_string} <-----> Jam Ke-2 {second_time_string}")
print(f"Selisih Jam Ke-1 dan Jam Ke-2 Adalah {time_delta}")

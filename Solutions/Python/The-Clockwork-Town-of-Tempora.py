#Initialize Grand clock and clock times
grand_clock = "15:00"
clock_times = ["14:45", "15:05", "15:00", "14:40"]


#Create a function to calculate the time difference between the grand clock and the clock times
def calculate_time_difference(grand_clock, clock_times):
    time_differences = []
    for clock in clock_times:
        grand_hours, grand_minutes = map(int, grand_clock.split(":"))
        clock_hours, clock_minutes = map(int, clock.split(":"))
        grand_total_minutes = grand_hours * 60 + grand_minutes
        clock_total_minutes = clock_hours * 60 + clock_minutes
        time_difference = clock_total_minutes - grand_total_minutes
        time_differences.append(time_difference)
    return time_differences

#print the time differences to console
print(calculate_time_difference(grand_clock, clock_times)) # Outputs: [-15, 5, 0, -20]
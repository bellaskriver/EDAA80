
# Beräkna medeltemperatur per månad/år manuellt
def calculate_avg_temp(temp_list: list[float]) -> float:
    total_temp = 0
    days = 0

    for temp in temp_list:
        days += 1
        total_temp += temp

    return total_temp / days

# 
def when_is_spring(temp_list):
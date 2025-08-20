from pathlib import Path
import file_reader 
import weather_functions as wf

#from weather_functions import calculate_avg_temp
#calculate_avg_temp(temp_list)

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)


avg_temp = sum(temp_list)/len(temp_list)
format(avg_temp, '.2f')
print(avg_temp)

wf.calculate_avg_temp(temp_list)
print(wf.calculate_avg_temp(temp_list))


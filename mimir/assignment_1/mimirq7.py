years_str = input("Years: ") # do not change this line
years_int = int(years_str)
pop_int = 307357870
seconds_per_year_int = 60 * 60 * 24 * 365  # Missing lines here
new_population = years_int * ((seconds_per_year_int) / 7 - (seconds_per_year_int) / 13 + (seconds_per_year_int) / 35) + pop_int
print("New population after", years_int, " years is ", int(new_population)) # do not change this line

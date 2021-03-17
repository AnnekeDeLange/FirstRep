# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_most_spoken_language = 'Castilian Spanish'
switzerland_most_spoken_language = 'Swiss German'
print(spain_most_spoken_language == switzerland_most_spoken_language)
spain_most_prevalent_religion = 'Roman Catholic'
switzerland_most_prevalent_religion = 'Roman Catholic'
print(spain_most_prevalent_religion == switzerland_most_prevalent_religion)
spain_capitol = 'Madrid'
switzerland_capitol = 'Bern'
print(len(spain_capitol) != len(switzerland_capitol))
spain_gdp = 1778000000000.00
switzerland_gdp = 580000000000.00
print(switzerland_gdp > spain_gdp)
spain_population_growth_percentage = 0.67
switzerland_population_growth_percentage = 0.66
print(switzerland_population_growth_percentage < 1.0 and spain_population_growth_percentage < 1.0)
spain_population_count = 50000000
switzerland_population_count = 8400000
print((spain_population_count or switzerland_population_count) > 10000000)
print(not(spain_population_count and switzerland_population_count) > 10000000)

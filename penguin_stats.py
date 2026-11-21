
#penguin_stats.py
#Russell Thompson
#Submission data
#Functions for calculating classifying penguin statistics

#calculate penguin percentage
def calculate_percentage(count, total):
    percentage = (count / total) * 100
    return percentage

#determine selected species
def classify_species(percent):
    if percent < 25:
        size_catagory = "small"
        return size_catagory
    elif 25 <= percent < 40:
        size_catagory = "medium"
        return size_catagory
    else:
        size_catagory = "large"
        return size_catagory

#display species statistics
def get_position_description(selected_species, largest_species,
    smallest_species):    
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"




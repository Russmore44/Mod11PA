# PalmerPenguinM11.py
# Russell Thompson
# 11/21/2026
# Organize Palmer Penguin analysis using custom modules

import math
from penguin import Penguin
import penguin_stats

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

# constrants for number of penguins
NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

#instructor provided function
def read_penguin_row(row_number):
    penguin_row = ""
    try:
        with open("PalmerPenguins.csv", "r") as penguin_file:
            penguin_file.readline()

            current_row = 1

            #search for the requested data row
            for row in penguin_file:
                if current_row == row_number:
                    penguin_row = row.strip()
                    break

                current_row += 1

    except FileNotFoundError:
        print("Error: PalmerPenguins.csv was not found.")

    if penguin_row == "":
        raise ValueError(f"Penguin observation {row_number} "
                             f"could not be retrieved.")
    return penguin_row

#display species statistics
def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        count = counts[index]
        percent = percentages[index]
        print(f"{species}: {count} ({percent:.2f}%)")

#function display selected species
def display_penguin_observation(sample, species, bill_length, bill_depth, \
    body_mass, sex):
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")
    print()
    print(f"Sample Number: {sample}")
    print(f"Species:       {species}")
    print(f"Bill Length:   {bill_length} mm")
    print(f"Bill Depth:    {bill_depth} mm")
    print(f"Body Mass:     {body_mass} g")
    print(f"Sex:           {sex}")

# retrieve sample penguin data
def process_penguin_row(row_number):
    try:
        penguin_row = read_penguin_row(row_number)
        print("\nSample dataset row:")
        print(penguin_row)
        # split the CSV row into individual values
        penguin_data = penguin_row.split(",")
        # DEBUG
        print(penguin_data)

        # retrieve and convert individual values
        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        bill_length = float(penguin_data[2])
        bill_depth = float(penguin_data[3])
        body_mass = int(penguin_data[5])
        sex = penguin_data[6]

        # display the penguin observation
        display_penguin_observation(
            sample_number,
            species,
            bill_length,
            bill_depth,
            body_mass,
            sex
        )
      
    except ValueError as excpt:
        print(f"Error: {excpt}")
    except IndexError:
        print(f"Error: The penguin observation is incomplete")
    print()
#validate selections
valid_selections = 0
#main function
def main():
    from penguin_stats import calculate_percentage
    # list of species names
    species_names = [SP_CHINSTRAP, SP_GENTOO, SP_ADELIE]
    # list of species counts
    species_counts = [NUM_CHINSTRAP, NUM_GENTOO, NUM_ADELIE]
    # determine the number of species
    total_species = len(species_names)
    # calculate the total number of penguins
    total_penguins = sum(species_counts)
    #calculate species percentages
    species_percentages = [penguin_stats.calculate_percentage(count,\
    total_penguins) for count in species_counts]
    # calculate the average number of penguins per species
    average_penguins = total_penguins / total_species
    # calculate the rounded-up average
    average_penguins_rounded_up = math.ceil(average_penguins)
    # find the species with most and fewest observations
    largest_count = max(species_counts)
    smallest_count = min(species_counts)
    # where do values occur
    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)
    # use indexes to retrieve the corresponding species names:
    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output the species names with introductory text
    print("Introducing the Palmer Penguins:")
    print()
    print("\t" + SP_CHINSTRAP + "!")
    print("\t" + SP_GENTOO + "!")
    print("and last but not least...")
    print("\t" + SP_ADELIE + "!")
    print()
    print(f"There are a total of {total_species} penguin species in this "
        f"dataset.")
    
    # display details of penguins averages
    print(f"There are a total {total_penguins} penguins in the dataset.")
    print(f"The average number of penguins per species is "
        f"{average_penguins:.1f}.")
    print()

    # number of penguins
    display_species_statistics(species_names, species_counts,
        species_percentages)
    print()

    # penguin observations
    print(f"The species with the most observations is {largest_species} with "
    f"{largest_count} penguins")
    print(f"The species with the fewest observations is {smallest_species} with"
    f" {smallest_count} penguins.")
    print()
    
    print("Module Import Demonstration")
    percentage = calculate_percentage(species_counts[0], total_penguins)
    print(f"Chinstrap percentage: {percentage:.2f}%")
    print()
    print("Custom Module Location")
    print(penguin_stats.__file__)
    print()

    print(f"Sample Penguin Observation")

    #retrieve and process two sample observations
    process_penguin_row(1)
    process_penguin_row(153)

    #demonstrate exception handling
    print("\nException Handling Demonstration")
    process_penguin_row(999)
    print()


    #list of penguin row numbers and body masses
    sample_rows = [1,2,3,4,5]
    body_masses = []
    for row_number in sample_rows:
        penguin_row = read_penguin_row(row_number)
        penguin_data = penguin_row.split(",")
        body_mass = int(penguin_data[5])
        body_masses.append(body_mass)

    #calculate summary statistics
    print(f"Sample Body Masses")
    print(body_masses)
    print(f"Body Mass Summary")
    print(f"Observations:       {len(body_masses)}")
    print(f"Total body mass:    {sum(body_masses)} g")
    print(f"Smallest body mass: {min(body_masses)} g")
    print(f"Largest body mass:  {max(body_masses)} g")
    print(f"Average body mass:  {sum(body_masses) / len(body_masses):.2f} g")
    print()
    print(f"Species Counts Using a Dictionary")

    #create dictionary of species counts
    species_dictionary = {
        SP_CHINSTRAP: (NUM_CHINSTRAP),
        SP_GENTOO:    (NUM_GENTOO),
        SP_ADELIE:    (NUM_ADELIE)
    }

    #access and display dictionary
    for species in species_dictionary:
        count = species_dictionary[species]
        print(f"{species}: {count}")
    print()

    #create a penguin object
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")
    sample_penguin = Penguin(
        int(penguin_data[0]),
        penguin_data[1],
        int(penguin_data[5])
    )
    print("Penguin Object Demonstration")
    sample_penguin.display_info()

    #create a list of penguin objects
    sample_rows = [1,2,3,4,5]
    penguin_objects = []
    for row_number in sample_rows:
        penguin_row = read_penguin_row(row_number).strip()
        penguin_data = penguin_row.split(",")
        sample_penguin = Penguin(
            int(penguin_data[0]),
            penguin_data[1],
            int(penguin_data[5]),
            )
        penguin_objects.append(sample_penguin)
    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    #calculate an average using objects
    total_object_mass = 0
    for penguin in penguin_objects:
        total_object_mass += penguin.body_mass
    average_object_mass = total_object_mass / len(penguin_objects)
    print("\nObject-Based Body Mass Summary")
    print(f"Observations:       {len(penguin_objects)}")
    print(f"Total body mass:    {total_object_mass} g")
    print(f"Average body mass:  {average_object_mass:.2f} g")
    print()

    #species selection
    print(f"Explore the Palmer Penguins")
    valid_selections = 0

    print("Enter Chinstrap, Gentoo, or Adelie, or Done: ")
    species_choice = input("\nEnter a species: ")
    print()
    while species_choice != "Done":

        #process the user's selection
        if species_choice == "Sample":
            try:
                sample_number = int(input("Enter a sample number: "))
                process_penguin_row(sample_number)
            except ValueError:
                print("Please enter a valid sample number.")
            finally:
                print("Sample request completed.")
                print()


        elif species_choice not in species_names:
            print(f"{species_choice} is not one of the species in this"
                  f" dataset.")

        else:
            #exisiting species exploration logic
            if species_choice == species_names[0]:
                 selected_index = 0
            elif species_choice == species_names[1]:
                 selected_index = 1
            elif species_choice == species_names[2]:
                 selected_index = 2
             #exisiting species exploration logic;
            print()


            # retrieve the selected species data
            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]
            valid_selections +=1

            # classify the species by percentage
            size_catagory = penguin_stats.classify_species(selected_percent)
            # determine the species' relative position
            position_description = \
            penguin_stats.get_position_description(selected_species, \
            largest_species, smallest_species)

            # compare the selected count to the average
            average_position = "above" if selected_count > \
            average_penguins else "below"

            # Display the selected species statistics
            print(f"{selected_species} has {selected_count} observations, "
                    f"representing {selected_percent:.2f}% of the dataset.")
            print(f"{selected_species} is classified as a "
                    f"{size_catagory} species group.")
            print(f"{selected_species} is the {position_description} species "
                    f"group.")
            print(f"Its observation count is {average_position} the dataset "
                    f"average of {average_penguins:.1f}.")
        print()
        species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")
        print()

    #display the exploration summary
    print(f"You explored {valid_selections} valid species.")
    print(f"Exploration complete.")
    print()

if __name__ == "__main__":
    main()



























#!/usr/bin/python3

#load neccessary packages
from Bio import SearchIO        #stuff needed to parse the file
import argparse                 #stuff to read the file as arguments to the 
import csv

# Create an Argument Parser
parser = argparse.ArgumentParser(description="HMMER3 Tabular Output Parser")

# Define the Input and Output Arguments
parser.add_argument("-in", "--input", required=True, help="HMMER3 tabular output file")
parser.add_argument("-out", "--output", required=True, help="Output file for parsed results")

# Parse the Command-Line Arguments
args = parser.parse_args()

# Access the Argument Values
hmmer_output_file = args.input
output_file = args.output

# Parse the HMMER3 Tabular Output
hmmer_results = list(SearchIO.parse(hmmer_output_file, "hmmer3-tab"))

# Initialize list to store the parsed results
parsed_results = []

# Process the results to extract the information you are interested in
for result in hmmer_results:
    query_name = result.id
    for hit in result:
        hit_name = hit.id
        for hsp in hit:
            e_value = hsp.evalue # fetch the evalue
            bitscore = hsp.bitscore # fetch the bitscore
            parsed_results.append([query_name, hit_name, e_value, bitscore]) # put everything into the list

# Write the parsed results to the TSV file
with open(output_file, "w", newline="") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t') # tab separated
    writer.writerow(["Query", "Hit_name", "E-value", "Bitscore"])  # Write the header
    writer.writerows(parsed_results)

print(f"Results have been written to {output_file}") # print the location where they have been saved just in case

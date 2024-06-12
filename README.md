# HMMSCAN PARSER
Small script that allows to convert the "tabular" output from hmmscan into a tsv output which can be easily usable in downstream automated analyses 

## Why making a parser
The standar hmmscan output, even when specifying the tabular output format, is a text file which a better spacing system that makes it visually readable but a nightmare to use in automated downstream analyses
The simple python script convert the original tabular output to a more usable tsv file. It simply extracts the e-value and bitscore for each match but this can be modified in the future

## Requirements
Bio.SearchIO package from [Biopython](https://biopython.org/) 
[argparse](https://pypi.org/project/argparse/)  
[python csv](https://pypi.org/project/python-csv/)

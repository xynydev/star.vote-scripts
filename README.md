Scripts for counting ballots and runoff with the star.vote ballot record. 

# CalculateTotal.py
Calculates the total votes for each candidate, no runoff.
## Arguments:
  -h, --help            show this help message and exit

  -I INPUT, --input INPUT
                        Path to the input .csv from star.vote. (eg. ~/Desktop/starvoting_ballots_1234678_20210414010104.csv)
                        
  -O OUTPUT, --output OUTPUT
                        Path to the output file (eg. ~/Desktop/totalvotes.csv)
import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    database = []
    header = []
    names = []
    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            database.append(row)
            names.append(row[0])

    # TODO: Read DNA sequence file into a variable
    f = open(sys.argv[2])
    sequence = f.read()

    counts = []
    # TODO: Find longest match of each STR in DNA sequence
    for i in range(1, len(header)):
        count = longest_match(sequence, header[i])
        counts.append(count)

    # TODO: Check database for matching profiles
    counter = 0
    # iterate through the list that contains the number of each STR
    # and we compare each of the numbers to the all the STRs of each person

    for i in range(0, len(names)):
        for j in range(0, len(counts)):
            num = int(database[i][j+1])
            if counts[j] == num:
                # when it is the same number we increment the counter by 1
                counter += 1
            # if the counter is equal to the number of STRs which means
            # that all the STR numbers match the person's number
            # we quit

                if(counter == len(counts)):
                    print(names[i])
                    sys.exit()

                else:
                    continue

            # if it is not the same number the counter stays as it is and we
            else:
                counter += 0
            # when we finish the iteration for all the first person, if it is not the person
            # we reset the counter to 0
        counter = 0
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

         # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

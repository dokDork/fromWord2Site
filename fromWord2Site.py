import sys

def generate_combinations(words, prefixes, suffixes):
    # Create a list to hold the new combinations
    combinations = []
    
    # Iterate through each word
    for word in words:
        # Iterate through each prefix
        for prefix in prefixes:
            # Iterate through each suffix
            for suffix in suffixes:
                # Create the new combination and add it to the list
                combinations.append(f"{prefix}.{word}.{suffix}")
    
    return combinations

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python fromWord2Site.py <input_file> <prefixes> <suffixes>")
        print("This script generates new words by combining prefixes and suffixes with words from an input file.")
        print("Parameters:")
        print("  <input_file>: A text file containing a list of words.")
        print("  <prefixes>: A comma-separated list of prefixes.")
        print("  <suffixes>: A comma-separated list of suffixes.")
        sys.exit(1)

    input_file = sys.argv[1]
    prefixes_input = sys.argv[2]
    suffixes_input = sys.argv[3]

    # Read the list of words from the input file
    try:
        with open(input_file, 'r') as file:
            words = [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)

    # Split the prefixes and suffixes into lists
    prefixes = [prefix.strip() for prefix in prefixes_input.split(',')]
    suffixes = [suffix.strip() for suffix in suffixes_input.split(',')]

    # Generate all combinations
    combinations = generate_combinations(words, prefixes, suffixes)

    # Create output filename based on input filename
    output_file = f"{input_file}.output"

    # Write the combinations to the output file
    with open(output_file, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')

    print(f"Combinations have been written to '{output_file}'.")

if __name__ == "__main__":
    main()

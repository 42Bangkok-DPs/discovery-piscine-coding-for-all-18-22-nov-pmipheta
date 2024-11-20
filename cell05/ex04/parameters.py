import sys

def main():
    # sys.argv includes the script name as the first argument, so we subtract 1 to get the number of parameters.
    num_params = len(sys.argv) - 1
    
    # Print the output
    print(f"Number of parameters: {num_params}.")
    
# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()

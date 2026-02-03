"""
Project: End-to-End Data Cleaning Pipeline
Author: Alaa Zaitoon
Description: 
    This script demonstrates a simple end-to-end data cleaning workflow:
    1) Generate a dummy raw text file containing noise and duplicate emails.
    2) Read the file and extract emails using RegEx.
    3) Clean the results (deduplicate) and compute basic statistics.
    4) Export the cleaned emails to a CSV file.
"""
import re
import os

# --- Part 1: Generate Dummy Data ---
def create_dummy_data(filename):
    """Create a raw text file containing noisy data for testing."""
    content = """
    Hello AI Student, contact us at support@google.com for help.
    If you like Python, email guido@python.org immediately.
    SPAM ALERT: fake@virus.net is bad.
    Duplicate email here: support@google.com (do not extract twice).
    Another user: alaa@horus.edu is learning AI.
    Test email: user123@yahoo.com and admin@yahoo.com
    Garbage text... 12345... #@!$
    """
    # Save the sample content to a file
    with open(filename, 'w') as f:
        f.write(content)
    print(f"[Success] Dummy data file '{filename}' created.")


# --- Part 2: Process & Clean Data ---
def process_data(input_file, output_file):
    """Extract emails from a raw text file, deduplicate them, and export to CSV."""
    
    # Ensure the input file exists before reading
    if not os.path.exists(input_file):
        print(f"[Error] File '{input_file}' not found!")
        return

    # 1) Read raw text content
    with open(input_file, 'r') as f:
        text_content = f.read()
    
    # 2) Extract emails using RegEx (capturing groups -> tuples)
    email_pattern = re.compile(r'([\w\.]+)@(\w+)\.([a-z]{3})')
    matches = email_pattern.findall(text_content)
    
    print(f"\n--- Processing '{input_file}' ---")
    print(f"Raw matches found: {len(matches)}")

    # 3) Clean and analyze results (set for uniqueness, dict for counts)
    unique_emails = set()
    domain_counts = {}

    for match in matches:
        username, domain, extension = match  # Tuple unpacking
        full_email = f"{username}@{domain}.{extension}"
        
        # Deduplicate emails automatically
        unique_emails.add(full_email)
        
        # Count domain occurrences
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    # 4) Export cleaned emails to CSV
    with open(output_file, 'w') as f:
        f.write("Email,Domain\n")  # CSV header
        for email in unique_emails:
            dom = email.split('@')[1].split('.')[0]
            f.write(f"{email},{dom}\n")

    # 5) Print a simple summary report
    print(f"Unique emails saved: {len(unique_emails)}")
    print("Domain Stats:", domain_counts)
    print(f"[Success] Clean data saved to '{output_file}'")


# --- Main Execution ---
if __name__ == "__main__":
    raw_filename = "raw_data.txt"
    csv_filename = "cleaned_emails.csv"

    # Step 1: Generate test data
    create_dummy_data(raw_filename)

    # Step 2: Extract, clean, and export results
    process_data(raw_filename, csv_filename)
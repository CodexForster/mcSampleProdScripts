# Read the file paths from find_query_list_test.txt
with open('find_query_list_test.txt', 'r') as f:
    new_file_paths = f.read().strip().split('\n')

# Format the new file paths for Python syntax
formatted_paths = [f"    '{path}'," for path in new_file_paths]
formatted_paths[-1] = formatted_paths[-1][:-1]  # Remove the trailing comma from the last line
# Read the contents of DRPremix_cfg.py
with open('DRPremix_cfg.py', 'r') as f:
    lines = f.readlines()

# Replace the file paths in DRPremix_cfg.py
with open('DRPremix_cfg.py', 'w') as f:
    inside_file_names = False
    for line in lines:
        if 'process.mixData.input.fileNames = cms.untracked.vstring([' in line:
            f.write(line)  # Write the line with the fileNames declaration
            inside_file_names = True
            # Handle the case where the list is empty
            if 'cms.untracked.vstring([])' in line:
                f.writelines('\n'.join(formatted_paths) + '\n')
                inside_file_names = False
        elif inside_file_names:
            if '])' in line:  # End of the fileNames list
                f.writelines('\n'.join(formatted_paths) + '\n')
                f.write(line)  # Write the closing bracket
                inside_file_names = False
            # Skip the old file paths
        else:
            f.write(line)  # Write other lines unchanged
# Read the file paths from find_query_list_test.txt
with open('find_query_list_test.txt', 'r') as f:
    new_file_paths = f.read().strip().split('\n')

# Format the new file paths for Python syntax
formatted_paths = [f"    '{path}'," for path in new_file_paths]
formatted_paths[-1] = formatted_paths[-1][:-1]  # Remove the trailing comma from the last line

# Read the contents of DRPremix_cfg.py
with open('DRPremix_cfg.py', 'r') as f:
    lines = f.readlines()

# Replace the fileNames line in DRPremix_cfg.py while maintaining the order
with open('DRPremix_cfg2.py', 'w') as f:
    for line in lines:
        # Replace the line that starts with the fileNames declaration
        if line.strip().startswith('process.mixData.input.fileNames = cms.untracked.vstring(['):
            f.write('process.mixData.input.fileNames = cms.untracked.vstring([\n')
            f.writelines('\n'.join(formatted_paths) + '\n])\n')
        else:
            f.write(line)  # Write all other lines unchanged
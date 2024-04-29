import subprocess
# import subprocess

# Run the Bash script and capture its output
output = subprocess.check_output(['bash', 'read_ini.sh']).decode('utf-8')

# Process the output as needed
print(output)

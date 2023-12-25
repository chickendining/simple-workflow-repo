import subprocess

# Function to execute a shell command and return its output
def run_shell_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

# Inside main.py
# List current directory contents
output, error = run_shell_command("ls -a")
if error:
    print("Error:", error.decode())
else:
    print("Current directory contents:\n", output.decode())

# Then, read the file
try:
    with open("../caller_repo/config/org.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

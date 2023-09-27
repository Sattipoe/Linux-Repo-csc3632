import os

# Function to compile .md files
def compile_md_files(root_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as compile_file:
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith('.md'):
                    file_path = os.path.join(foldername, filename)
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        compile_file.write(md_file.read() + '\n')

if __name__ == "__main__":
    root_folder = "/home/student/VMtest/Linux-Repo-csc3632/known-cyber-attacks"  # Updated path
    output_file = "Compile.md"  # Name of the compiled output file

    compile_md_files(root_folder, output_file)
print(f"Compilation complete. Compiled MD file saved as '{output_file}'")

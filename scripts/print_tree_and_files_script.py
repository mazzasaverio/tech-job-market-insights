
import subprocess
import os

def run_tree_command(output_file_path, exclude_patterns):
    """
    Run the tree command and save the output to a specified file.

    Args:
        output_file_path (str): The path to the file where the output will be saved.
        exclude_patterns (str): Patterns to exclude from the tree command.
    """
    command = f"tree -a -I {exclude_patterns}"
    try:
        with open(output_file_path, 'w') as f:
            subprocess.run(command, stdout=f, shell=True)
    except Exception as e:
        print(f"An error occurred while running the tree command: {e}")

def append_file_content_to_output(output_file_path, file_list):
    """
    Append the content of each file in the given list to the specified file.

    Args:
        output_file_path (str): The path to the file where the content will be appended.
        file_list (list): List of file paths to read.
    """
    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            continue
        try:
            with open(file_path, 'r') as src_file:
                content = src_file.read()
            with open(output_file_path, 'a') as dest_file:
                dest_file.write(f"\n\n=== Content of {file_path} ===\n\n")
                dest_file.write(content)
        except Exception as e:
            print(f"An error occurred while reading/writing file {file_path}: {e}")

if __name__ == "__main__":
    output_file_path = "custom_tree_and_files_corrected.txt"
    exclude_patterns = "'__pycache__|node_modules|public|.venv|.git|.vscode|__init__.py|__init__.pyc|__py'"
    file_list = ["README.md",
        "backend/api/main.py",
                    "backend/api/db/database.py",
                   "backend/api/models/question.py",
                    "backend/api/routers/questions.py",
                    "frontend/src/index.js",
                    "frontend/src/App.js",
                    "frontend/src/components/QuestionList.js",
                    "frontend/src/components/HomePage.js"
                 ]

    run_tree_command(output_file_path, exclude_patterns)
    append_file_content_to_output(output_file_path, file_list)

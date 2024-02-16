import os


def find_folder_in_current_heirarchy(folder_name):
    """
    Search for a folder in the same directory as the Python file.
    """
    # Get the current directory of the Python file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Search for folders named '.venv_project_name' in the current directory
    for folder in os.listdir(current_dir):
        if folder == folder_name and os.path.isdir(os.path.join(current_dir, folder)):
            return os.path.join(current_dir, folder)

    # If no '.venv_project_name' folder is found, return None
    return None


def activate_virtualenv(venv_path):
    """
    Activate a virtual environment if it's not already active.

    :param venv_path: Path to the virtual environment directory.
    """
    # Check if the virtual environment is already activated
    if not os.environ.get("VIRTUAL_ENV"):
        # Activate the virtual environment
        activate_script = (
            os.path.join(venv_path, "Scripts/activate")
            if os.name == "nt"
            else os.path.join(venv_path, "bin/activate")
        )
        os.system(f"source {activate_script}")


# Example usage:
if __name__ == "__main__":
    # Specify the path to your virtual environment
    venv_path = "/path/to/your/virtualenv"
    activate_virtualenv(venv_path)

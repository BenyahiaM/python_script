import sys
from projects import python_project, node_project

def main():
    if len(sys.argv) < 2:
        print("Please provide a project type ('python' or 'node').")
        sys.exit(1)

    project_type = sys.argv[1].lower()

    if project_type == "python":
        python_project.setup()
    elif project_type == "node":
        node_project.setup()
    else:
        print(f"Unsupported project type: {project_type}. Please use 'python' or 'node'.")

if __name__ == "__main__":
    main()

import json
import csv
import os

# Define file names
JSON_FILE = "projects.json"
CSV_FILE = "projects.csv"

# Define the Project class
class Project:
    def __init__(self, name, budget, description, sanctioned=False):
        self.name = name
        self.budget = budget
        self.description = description
        self.sanctioned = sanctioned

    def to_dict(self):
        return {
            "name": self.name,
            "budget": self.budget,
            "description": self.description,
            "sanctioned": self.sanctioned
        }

# Functions for CRUD operations
def create_project():
    name = input("Enter Project Name: ")
    budget = float(input("Enter Budget Required: "))
    description = input("Enter Project Description: ")
    sanctioned = input("Is the budget sanctioned? (yes/no): ").lower() == "yes"
    return Project(name, budget, description, sanctioned)

def read_projects():
    projects = load_projects()
    if projects:
        for idx, project in enumerate(projects, start=1):
            print(f"\nProject {idx}:")
            print(f"Name: {project['name']}")
            print(f"Budget: {project['budget']}")
            print(f"Description: {project['description']}")
            print(f"Sanctioned: {'Yes' if project['sanctioned'] else 'No'}")
    else:
        print("No projects found.")

def update_project():
    projects = load_projects()
    if not projects:
        print("No projects to update.")
        return
    read_projects()
    try:
        project_idx = int(input("Enter the project number to update: ")) - 1
        if 0 <= project_idx < len(projects):
            projects[project_idx]["name"] = input("Enter New Project Name: ")
            projects[project_idx]["budget"] = float(input("Enter New Budget Required: "))
            projects[project_idx]["description"] = input("Enter New Project Description: ")
            projects[project_idx]["sanctioned"] = input("Is the budget sanctioned? (yes/no): ").lower() == "yes"
            save_projects(projects)
            print("Project updated successfully.")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_project():
    projects = load_projects()
    if not projects:
        print("No projects to delete.")
        return
    read_projects()
    try:
        project_idx = int(input("Enter the project number to delete: ")) - 1
        if 0 <= project_idx < len(projects):
            projects.pop(project_idx)
            save_projects(projects)
            print("Project deleted successfully.")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Please enter a valid number.")

# Functions to handle data storage
def save_projects(projects):
    # Save to JSON
    with open(JSON_FILE, 'w') as json_file:
        json.dump(projects, json_file, indent=4)
    # Save to CSV
    with open(CSV_FILE, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "budget", "description", "sanctioned"])
        writer.writeheader()
        writer.writerows(projects)

def load_projects():
    # Load from JSON if file exists
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as json_file:
            return json.load(json_file)
    return []

# User-friendly CLI
def main():
    while True:
        print("\nProject Budget Manager")
        print("1. Create a new project")
        print("2. View all projects")
        print("3. Update a project")
        print("4. Delete a project")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            new_project = create_project()
            projects = load_projects()
            projects.append(new_project.to_dict())
            save_projects(projects)
            print("Project added successfully.")
        elif choice == "2":
            read_projects()
        elif choice == "3":
            update_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the CLI
if __name__ == "__main__":
    main()

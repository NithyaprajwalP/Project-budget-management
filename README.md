# Project-budget-management

## Overview
The *Project Budget Manager* is a Python CLI-based application for managing project budgets. It allows users to create, view, update, and delete project entries. Each project entry contains details such as project name, required budget, description, and whether the budget has been sanctioned. All project data is saved in both JSON and CSV formats, providing persistent storage and easy data access.

## Features
- *Create a Project*: Add a new project with details like name, budget, description, and sanction status.
- *View All Projects*: Display a list of all existing projects along with their details.
- *Update a Project*: Modify the details of an existing project.
- *Delete a Project*: Remove a project from the list.
- *Data Persistence*: Saves and loads data from projects.json and projects.csv files.

## Requirements
- Python 3.x
- No external dependencies are required.

## How to Use
1. *Clone or Download* the repository.
2. *Run the Script*: Execute the script using the command:
    bash
    python project_budget_manager.py
    
3. *Choose an Option* from the menu:
    - Enter 1 to create a new project.
    - Enter 2 to view all projects.
    - Enter 3 to update an existing project.
    - Enter 4 to delete a project.
    - Enter 5 to exit the program.

4. *Follow the Prompts*: Input the required details as prompted by the CLI.

## Data Storage
- Project data is stored in two formats:
  - *JSON*: projects.json
  - *CSV*: projects.csv

## Example Usage
1. *Creating a New Project*:
    
    Enter Project Name: Website Redesign
    Enter Budget Required: 15000
    Enter Project Description: Redesign the company website for better user experience.
    Is the budget sanctioned? (yes/no): yes
    Project added successfully.
    

2. *Viewing All Projects*:
    
    List of Projects:

    Project 1:
    Name: Website Redesign
    Budget: $15,000.00
    Description: Redesign the company website for better user experience.
    Sanctioned: Yes
    

3. *Updating a Project*:
    
    Enter the project number to update: 1
    Enter New Project Name: Website Revamp
    Enter New Budget Required: 18000
    Enter New Project Description: Complete overhaul of the website design.
    Is the budget sanctioned? (yes/no): yes
    Project updated successfully.
    

4. *Deleting a Project*:
    
    Enter the project number to delete: 1
    Project deleted successfully.
    

## Notes
- Ensure that the projects.json and projects.csv files are in the same directory as the script, or they will be created automatically if they do not exist.
- Input validation is included for numerical entries such as the project budget to prevent errors.

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute as per the terms of the license.

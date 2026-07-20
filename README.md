<div align="center">

  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Selenium Logo" width="120" height="120" />

  # Selenium Pytest Automation Framework
  [![Follow](https://img.shields.io/badge/Follow-Neelima-blue?style=flat-square&logo=github)](https://github.com/NeelimaReddy123)
  [![Framework](https://img.shields.io/badge/Architecture-Pytest-green?style=flat-square&logo=pytest)](https://docs.pytest.org/)
  [![Docker](https://img.shields.io/badge/Grid-Docker--Enabled-blue?style=flat-square&logo=docker)](https://www.docker.com/)
  [![CI/CD Pipeline](https://img.shields.io/badge/Jenkins-Passing-brightgreen?style=flat-square&logo=jenkins)](https://www.jenkins.io/)
  [![Reporting](https://img.shields.io/badge/Allure-Enabled-orange?style=flat-square)](https://allurereport.org/)
  ![img.png](img.png) 
  ---
</div>

# About

### An enterprise-grade, highly scalable automation framework designed with Python, Pytest, Selenium 4, and Docker. It features multi-threaded parallel execution, a comprehensive logging engine, dynamic local/remote execution modes, and fully interactive Allure reporting built directly into a Jenkins CI/CD pipeline.

----------

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Setup & Prerequisites](#%EF%B8%8F-project-setup--prerequisites)
5. [Project Directory Structure](#%EF%B8%8F-project-directory-structure)
6. [Future Enhancements](#future-enhancements)
7. [Contributors & Credits](#contributors--credits)
8. [License](#license)

----------

## Project Overview

This project automates functional testing for a demo e-commerce web application  [https://tutorialsninja.com/demo](https://tutorialsninja.com/demo).  It is built on a robust hybrid automation framework using:

-   **Page Object Model (POM)**: For maintainable and reusable code.
-   **Selenium**: For web browser automation.
-   **Pytest**: For scalable and flexible test execution.
-   **Allure Reports**: For visually appealing test results.
-   **Selenium Grid (Docker)**: For parallel and cross-browser testing.
-   **Jenkins**: For CI/CD pipelines and scheduled test executions.
----------

## Features

-   **Functional Coverage**:
    -   User login tests
    -   Registration tests
-   **Parallel Test Execution**  with  `pytest-xdist`.
-   **Allure Integration**  for detailed reporting.
-   **Dockerized Selenium Grid**  for distributed testing.
----------

## Technologies Used

-   **Programming Language**: Python
-   **Frameworks**: Pytest, Selenium, POM
-   **Reporting**: Allure Reports
-   **CI/CD**: Jenkins
-   **Containerization**: Docker and Docker Compose

----------
## 🛠️ Project Setup & Prerequisites

### 1. Local Workspace Initialization

Before executing tests locally, ensure your machine meets the following environment requirements:

- **Python 3.9+** – Installed and added to system paths.
- **Node.js Environment** – Required to manage the Allure Reporting command-line binaries. Download from the [Official Node.js Website](https://nodejs.org/).
- **Allure CLI Installation** – Run the global installation package manager command:
```bash
npm install -g allure-commandline
```

Verify Allure Installation:
```bash
    allure --version
```

### 2. Clone the Repository & Install Dependencies

Clone your project workspace to your local directory and install dependencies:

```bash
git clone [https://github.com/NeelimaReddy123/selenium-pytest-framework.git](https://github.com/NeelimaReddy123/selenium-pytest-framework.git)
cd selenium-pytest-framework
pip install -r Requirements.txt
```

### 3.🛠️ Local Test Execution Configurations
This framework leverages customizable runtime command-line options to determine the browser engine, runtime infrastructure, parallelism rules, and execution modes.
1. Sequential Execution Workflow
To run the automated suite linearly, executing one test case at a time on your local workspace:
```bash
pytest tests/ --alluredir=reports --browser chrome --env local --mode normal
```

2. Multi-Threaded Parallel Execution (pytest-xdist)
To minimize execution bottlenecks, run multiple test workers simultaneously using the -n flag (distributing tests across 3 dedicated worker threads):
```bash
pytest tests/ --alluredir=reports -n 3 --browser chrome --env local --mode normal
```

3. Isolated Selenium Grid Pipeline Simulation (Docker Mode)
To replicate enterprise Jenkins CI/CD execution directly on your local machine, route test threads through scalable Docker containers:
#### A. Orchestrate the Selenium Hub and spin up 3 isolated Chrome execution nodes
```bash
docker compose -f docker-compose.yml up -d --scale chrome=3
```

#### B. Execute the test suite directly at the active grid cluster
```bash
pytest tests/ --alluredir=reports -n 3 --browser chrome --env remote --mode headless
```

#### C. Spin down and clean the containerized grid once execution completes
```bash
docker compose -f docker-compose.yml down
```
 
### 4.📋 Logging & Reporting Engine Guide

#### 📝 Live Framework Logging System
Runtime activities are logged dynamically and routed to logs/automation_run.log. Logging behavior is configured through the pytest.ini file.

> **Note**: Active logs (logs/), raw test reports (reports/), and generated reports (allure_reports/) are excluded from version control via .gitignore to prevent merge conflicts and repository bloat.

####  📊 Allure Reporting Operations
Stream a Quick Ephemeral Report
Compile raw JSON metadata into a temporary local report server for immediate review:
allure serve reports

Compile and Archive a Permanent Report
Build a standalone, long-term mini-website with styling sheets, execution data, and assets:
```bash
allure generate reports --clean -o allure_reports
```
View Archived Reports Correctly
Modern web browser security (CORS policies) blocks direct file access. Use the Allure CLI to host a local proxy server:
### View your test execution results:
```bash
- allure open allure_reports
```

### View the sample reference report:
```bash
allure open sample_allure_report
```
Press Ctrl + C in your terminal to close the reporting server when finished.
 
### 5.🚀 Running Tests with Cloud Integration (CI/CD)
1. Dockerized Selenium Grid Setup
The framework includes a docker-compose.yml blueprint that automatically deploys:
An enterprise-grade elastic Selenium Hub
Chrome, Firefox, and Edge browser node workers
Isolated execution dependencies from the host system

2. Automated Jenkins Infrastructure Configurations
Verify the following configurations under Jenkins Global Tool Configuration:
Java Environment Setup:
Name: Java 21 (or matching runtime version)
JAVA_HOME Directory: Your environment path (e.g., /usr/lib/jvm/java-21-amazon-corretto)
> **Note**: Leave "Install automatically" unselected if already installed on the host
Allure Reporting Binary Tool Configuration:
Name: Allure CLI (must match the Jenkinsfile reference)
Installation Path: Your installation location (e.g., /opt/allure)

3. Orchestrating a New Jenkins Pipeline Execution Instance
Access your Jenkins dashboard and select New Item
Define a project name and select Pipeline project type
Under Pipeline settings, select Pipeline Script from SCM

Set Source Code Management to Git and paste your repository URL:
https://github.com/NeelimaReddy123/selenium-pytest-framework.git
In the Script Path option, specify: Jenkinsfile
Click Save and select Build Now to verify the pipeline executes successfully


## 🏗️ Project Directory Structure

```text
selenium-pytest-framework/
├── Configurations/         # Global environment variables and config.ini
├── pageObjects/            # Encapsulated web elements and page action methods
├── reports/                # Raw JSON test result outputs (git-ignored)
├── tests/                  # Pytest automation scripts and conftest.py fixtures
├── test_data/              # External files (Excel/JSON) for data-driven testing
├── utils/                  # Custom logger, config readers, and driver handlers
├── docker-compose.yml      # Configuration for local Selenium Grid setup
├── Jenkinsfile             # Declarative pipeline instructions for CI/CD
├── Requirements.txt        # Frozen Python package dependencies
└── README.md               # Project documentation
```


## Future Enhancements

-   Add more test cases for payment gateway integration.
-   Implement API testing for backend functionalities.

## Contributors & Credits

- Neelima Busireddy - Automation Engineer & Framework Architect

- Docker Selenium: The docker-compose.yml baseline is adapted from Selenium's official GitHub repository.

## License

This project is licensed under the  [MIT License](file:///home/neelima/Documents/CloudEcomAutomation/LICENSE).  Feel free to use,  modify,  and distribute the code with attribution.

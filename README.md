# Selenium-pytest-Framework

### A Hybrid Automation Framework for Testing an E-commerce Application Using Selenium, Pytest, Allure, Docker, Jenkins

----------

## Table of Contents

1.  [Project Overview](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#project-overview)
2.  [Features](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#features)
3.  [Technologies Used](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#technologies-used)
4.  [Project Setup](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#project-setup)
5.  [Running Tests Locally](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#running-tests-locally)
6.  [Running Tests with Cloud Integration](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#running-tests-with-cloud-integration)
7.  [Sample Reports](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#sample-reports)
8.  [Folder Structure](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#folder-structure)
9.  [Future Enhancements](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#future-enhancements)
10.  [Contributors](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#contributors)
11.  [Credits](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#credits)
12.  [License](http://localhost:63342/markdownPreview/1232844968/markdown-preview-index-s6hkpc3v82vbsu4lv2lm9orbvd.html#license)

----------

## Project Overview

This project automates functional testing for a demo e-commerce web application  [https://demo.opencart.com/](https://demo.opencart.com/).  It is built on a robust hybrid automation framework using:

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
    -   Product search tests
    -   Add to cart functionality
    -   Cart and checkout page validations
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

## Project Setup

### 1. Prerequisites

⚙️ Installation & Setup
Prerequisites
Python 3.8 or higher installed

pip (Python package manager)
Chrome/Firefox/Edge browser

python -m venv .venv
.venv\Scripts\activate
macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Configure WebDriver
The framework uses Selenium WebDriver. Ensure the appropriate driver (ChromeDriver, GeckoDriver, etc.) is installed and available in your system PATH, or use WebDriver Manager for automatic driver management.


### 2. Clone the Repository

https://github.com/NeelimaReddy123/selenium-pytest-framework/

remote: cd selenium-pytest-framework` 

## Folder Structure

selenium-pytest-framework/
├── assets/                 # Screenshots and report images for documentation
├── Configurations/         # Global environment variables and config.ini
├── pageObjects/            # Encapsulated web elements and page action methods
├── tests/              # Pytest automation scripts and conftest.py fixtures
├── testData/               # External files (Excel/JSON) for data-driven testing
├── utilities/              # Custom logger, config readers, and driver handlers
├── docker-compose.yml      # Configuration for local Selenium Grid setup
├── Jenkinsfile             # Declarative pipeline instructions for CI/CD
├── requirements.txt        # Frozen Python package dependencies
└── README.md               # Project documentation

## Future Enhancements

-   Add more test cases for payment gateway integration.
-   Implement API testing for backend functionalities.

## Contributors

**Neelima Busireddy**  (Owner and Contributor)

## Credits

The  `docker-compose.yml`  file is adapted from  [Selenium's official GitHub repository](https://github.com/SeleniumHQ/docker-selenium).

## License

This project is licensed under the  [MIT License](file:///home/neelima/Documents/CloudEcomAutomation/LICENSE).  Feel free to use,  modify,  and distribute the code with attribution.
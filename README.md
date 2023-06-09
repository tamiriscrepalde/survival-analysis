# Survival Analysis - Packages Cancellation

- [Survival Analysis - Packages Cancellation](#survival-analysis---packages-cancellation)
  - [Context](#context)
  - [Files in the repository](#files-in-the-repository)
  - [Setup Instructions](#setup-instructions)

## Context

This project was developed together with Udacity as part of the Data Science Nanodegree Program.

The main objective of the project is to explore a travel package cancellation dataset. Which is provided by a Brazilian Online Travel Agency.

One of this OTA's main products is travel packages, a combination of hotel reservations and flight tickets. When the package already has a specific date for the client to travel, it's called a 'fixed date package,' and when it's not attached to a specific date, it's called a 'flexible date package.'

Flexible date packages offer the client the opportunity to fill up a form informing three desired dates to travel. It has competitive prices and flexible payment options, a top-selling product. Usually, this product has an extensive valid period, reaching two years in many cases, and flexible cancellation policies.

The process of hotel reservation and flight ticket scheduling commonly occurs within 45 days before the first desired date. And this process is called 'operation.'

Due to the vast time range between the order and the travel itself, financial planning is complex. Additionally, the uncertainty of the cancellation volume adds to this complexity.

Therefore, this analysis aims to analyze the cancellation of flexible date packages and answer the following questions:
- Are international travels more canceled than national ones?
- Is the number of status changes related to the cancellation process?
- Which are the features that have the most impact on cancellation?

An article was posted on Medium related to this project, you can read it [here](https://medium.com/@tamiriscrepalde/exploratory-data-analysis-on-travel-packages-cancellation-5e3972d50121).

## Files in the repository
Repository structure:

- notebooks
  - exploratory_data_analysis
    - packages_cancellation_analysis.ipynb
    - README.md
- src
  - visualization
    - visualization_utils.py
  - utils.py
- .gitignore
- GoogleUtils.py
- README.md
- requirements.txt

The `notebooks` folder contains the jupyter notebook containing the analysis and a REAME.md file with information about the dataset.

The `source` folder contains files containing python functions to help in processes such as dataset load, visualizations and data transformation.

The repository also contains the files: .gitignore which establishes which files and directories must be ignored by Git; README.md which brings these instructions; and requirements.txt which has the required libraries to reproduce this project.


## Setup Instructions

The data used in this project, as well as the query file used to recover the data, were not included in the repository due to confidential matters. Although, to reproduce the analysis independently of the data, follow the instructions below.

1. It's recommended to start a virtual environment.

2. Clone this repository:
   `git clone git@github.com:TamirisCrepalde/survival-analysis.git`.

3. Install the required libraries by running the command: `pip install -r requirements.txt`.

4. Add your own data at `src/data`.

5. Run the notebook.

# Linear Regression Simulation

This project is a simple Flask web application that allows users to explore the impact of various parameters on linear regression. The tool generates random data, performs linear regression, and displays the results in the form of a scatter plot with a regression line and a histogram of slopes and intercepts from multiple simulations.

## Features

- **Scatter Plot and Regression Line**: Generates a scatter plot of random data points and fits a linear regression line.
- **Histogram of Slope and Intercept Values**: Runs multiple simulations to show the distribution of slopes and intercepts.

## Requirements

- Python 3.7+
- Flask
- numpy
- matplotlib
- scikit-learn

## Installation

1. Clone the repository or download the zip file.
2. Navigate to the project directory in your terminal.
3. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   or
   pip install flask numpy matplotlib scikit-learn

## Usage

1. Run the Flask application by executing the following command:

   ```bash
   python3 app.py

2. Open your web browser and go to http://127.0.0.1:5000/.
3. Enter the following input parameters:
Sample Size (N): Number of data points to generate.
Mean (μ): Mean of the normal error term added to Y.
- Variance (σ²): Variance of the normal error term.
- Number of Simulations (S): Number of datasets to simulate for histogram.
- Click "Generate" to view the results:
  - A scatter plot with a regression line based on the generated data.
  - A histogram showing the distribution of slopes and intercepts from the simulations.

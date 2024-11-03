import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def generate_data(N, mu, sigma2):
    X = np.random.rand(N)
    Y = mu + np.random.normal(0, np.sqrt(sigma2), N)
    return X, Y

def perform_linear_regression(X, Y):
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), Y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return slope, intercept

def create_scatter_plot(X, Y, slope, intercept):
    plt.figure()
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.plot(X, slope * X + intercept, color='red', label=f'Fitted Line: y = {intercept:.2f} + {slope:.2f}x')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.title("Scatter Plot with Regression Line")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close()
    return plot_data

def create_histogram(slopes, intercepts, base_slope, base_intercept):
    plt.figure()
    plt.hist(slopes, bins=20, alpha=0.5, label="Slopes", color="blue")
    plt.hist(intercepts, bins=20, alpha=0.5, label="Intercepts", color="orange")
    plt.axvline(base_slope, color="blue", linestyle="--", label=f"Slope: {base_slope:.2f}")
    plt.axvline(base_intercept, color="orange", linestyle="--", label=f"Intercept: {base_intercept:.2f}")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.title("Histogram of Slopes and Intercepts")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    histogram_data = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close()
    return histogram_data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            N = int(request.form["N"])
            mu = float(request.form["mu"])
            sigma2 = float(request.form["sigma2"])
            S = int(request.form["S"])

            # Generate initial data and perform regression
            X, Y = generate_data(N, mu, sigma2)
            slope, intercept = perform_linear_regression(X, Y)
            scatter_plot = create_scatter_plot(X, Y, slope, intercept)

            # Simulate multiple datasets for histogram
            slopes, intercepts = [], []
            for _ in range(S):
                Y_simulated = mu + np.random.normal(0, np.sqrt(sigma2), N)
                sim_slope, sim_intercept = perform_linear_regression(X, Y_simulated)
                slopes.append(sim_slope)
                intercepts.append(sim_intercept)

            histogram_plot = create_histogram(slopes, intercepts, slope, intercept)

            return render_template("index.html", scatter_plot=scatter_plot, histogram_plot=histogram_plot)
        except Exception as e:
            return f"An error occurred: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

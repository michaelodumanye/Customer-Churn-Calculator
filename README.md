# Customer Churn Prediction App

Welcome to the **Customer Churn Prediction App**! This application leverages a machine learning model to predict whether a customer will churn based on various inputs. The app is built using Streamlit, a powerful framework for creating interactive web applications in Python.

## Features

- **Interactive Interface:** Users can input customer data to predict the likelihood of churn.
- **Machine Learning Model:** The app uses a pre-trained machine learning model for making predictions.
- **Real-Time Predictions:** Instantly see the results of the prediction as you change the input values.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.8+ installed on your system. You also need to have the following Python packages installed:

- Streamlit
- Scikit-learn
- NumPy
- Pandas

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Customer-Churn-Calculator.git
   cd Customer-Churn-Calculator
   ```

2. **Set up the virtual environment:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   source myenv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   The app will automatically open in your default web browser. If not, navigate to `http://localhost:8501`.

## Usage

Once the app is running:

1. Enter the customer data in the input fields provided.
2. Click on the **Predict** button to see the churn prediction.
3. The app will display whether the customer is likely to churn based on the input data.

## Deployment

### Deploying on Streamlit Community Cloud

1. Push the project to your GitHub repository.
2. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Link your GitHub repository and deploy the app directly from there.

### Deploying on Render

1. Set up `render.yaml` for deployment on Render.
2. Link your GitHub repository to Render and follow the deployment process.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact modumanye@gmail.com

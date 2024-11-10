
# Smoker Status Prediction using Bio-Signals

## Project Overview

This project aims to build a classification model that predicts smoking status based on bio-signal data. Leveraging advanced data analysis techniques and machine learning models, we explore relationships between various biometric measurements and smoking habits. The dataset includes a range of bio-signal features that help in predicting the likelihood of an individual being a smoker.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Results](#results)
- [Visualization](#visualization)
- [Installation and Usage](#installation-and-usage)
- [Downloading the Project Files](#downloading-the-project-files)

## Dataset

The dataset contains various features related to bio-signals and health metrics. The main features used include:

- **Physical Measurements:** height, weight, waist size, eyesight, and hearing metrics
- **Blood Metrics:** systolic and diastolic blood pressure, triglyceride, HDL, LDL, hemoglobin levels
- **Other Bio-Signals:** liver enzyme levels (AST, ALT, GTP), dental caries presence, urine protein levels
- **Generated Features:** BMI, Waist-to-Height Ratio, Blood Pressure Category, Cholesterol Ratio, etc.

The target variable is `smoking`, which indicates the smoking status.

## Feature Engineering

Feature engineering plays a critical role in this project to derive meaningful features from raw data. The key engineering steps include:

- **Basic Calculations:** BMI, Waist-to-Height Ratio
- **Category Generation:** Blood Pressure Category, Cholesterol Ratio
- **Ordinal Encoding:** Age, Waist, and Triglyceride categories
- **Ratio Features:** Hemoglobin to GTP Ratio, Liver Enzyme Ratio
- **Imbalance Metrics:** Hearing and Eyesight Imbalance

For detailed code, see [Project_5_moduls.py](./Project_5_moduls.py).

## Modeling

This project uses various machine learning models and pipelines for classification, including:

- **Data Preprocessing:** Ordinal encoding, feature scaling, and transformations
- **Model Training:** Models are selected and optimized based on performance on the validation set, aiming for high accuracy and AUC-ROC scores.

## Results

The model performance is evaluated using metrics such as Accuracy, Precision, Recall, and AUC-ROC. The best model is chosen based on these metrics and its ability to generalize on unseen data.

## Visualization

For in-depth exploration and insights, visualizations are included to depict data distributions, feature correlations, and model performance. Check out the visualization notebook [Project_5_Visualization.ipynb](./Project_5_Visualization.ipynb) for detailed graphs.

## Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sardor017/Project6.git
   ```
2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the main notebook for preprocessing and modeling:**
   ```bash
   jupyter notebook Project_5_main.ipynb
   ```

## Downloading the Project Files

To download the project files, follow these steps:

1. **Clone the repository from GitHub** (requires Git):
   ```bash
   git clone https://github.com/Sardor017/Project6.git
   ```
   This will create a local copy of the repository on your machine.

2. **Download as a ZIP file**:
   If you prefer not to use Git, you can download the repository as a ZIP file directly from GitHub:

   - Go to [https://github.com/Sardor017/Project6](https://github.com/Sardor017/Project6).
   - Click on the green "Code" button.
   - Select "Download ZIP" from the dropdown menu.
   - Extract the ZIP file to access the project files.

Once downloaded, follow the instructions in the [Installation and Usage](#installation-and-usage) section to set up the project.

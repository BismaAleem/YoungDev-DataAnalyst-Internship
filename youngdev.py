# -*- coding: utf-8 -*-
"""YoungDEV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UVi7XnfLZ-SWXX_VNGDPUo6I2628jgU3
"""



"""Data Exploration with Pandas:
 Load a dataset using Pandas.
 Display basic statistics (mean, median, etc.) for numerical columns.
 Count unique values in a categorical column.

# New Section
"""

# Import the pandas library
import pandas as pd

# Load the Iris dataset

dataset = pd.read_csv('/content/Iris.csv')
# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(dataset.head())

# Display the data types of each column
print("\nData types of each column:")
print(dataset.dtypes)

# Calculate and display basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(dataset.describe())



# Identify categorical columns
categorical_columns = dataset.select_dtypes(include=['object', 'category']).columns
print("\nCategorical columns in the Iris dataset:")
print(categorical_columns)
# Count unique values in the categorical column 'species'
print("\nUnique values in the 'species' column:")
unique_values = categorical_columns.value_counts()
print(unique_values)


# Count unique values in the categorical column 'species'
#print("\nUnique values in the 'species' column:")
#unique_values = dataset['Species'].value_counts()
#print(unique_values)

# Import necessary libraries
import pandas as pd

# Load the Iris dataset from your Colab file
# Adjust the file path to point to the location of 'iris.csv'
iris_dataset = pd.read_csv('/content/Iris.csv')

# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(iris_dataset.head())

# Display the data types of each column
print("\nData types of each column:")
print(iris_dataset.dtypes)

# Calculate and display basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(iris_dataset.describe())

# Count unique values in the categorical column 'species'
print("\nUnique values in the 'Species' column:")
unique_values = iris_dataset['Species'].value_counts()
print(unique_values)

# Plotting a histogram of a numerical column (e.g., sepal length)
import matplotlib.pyplot as plt
iris_dataset['SepalLengthCm'].hist()
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Plotting a bar chart of the unique values in the 'species' column
unique_values.plot(kind='bar')
plt.title('Count of Unique Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Calculate the correlation matrix for only numerical columns
numerical_columns = iris_dataset.select_dtypes(include=['float64', 'int64'])
print("\nCorrelation matrix for numerical columns:")
print(numerical_columns.corr())

# Plotting a heatmap of the correlation matrix
import seaborn as sns
sns.heatmap(numerical_columns.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Import the pandas library
import pandas as pd

# Load the Iris dataset

dataset = pd.read_csv('/content/Iris.csv')

# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(dataset.head())

# Display the data types of each column
print("\nData types of each column:")
print(dataset.dtypes)

# Calculate and display basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(dataset.describe())



# Automatically identify categorical columns
categorical_columns = dataset.select_dtypes(include=['object', 'category']).columns
print("\nCategorical columns in the Iris dataset:")
print(categorical_columns)

# Count unique values in categorical columns
print("\nCount of unique values in categorical columns:")
for column in categorical_columns:
    print(f"\nUnique values in '{column}' column:")
    print(dataset[column].value_counts())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset

dataset = pd.read_csv('/content/Iris.csv')
# Create a histogram to visualize the distribution of a numerical variable
print("Histogram")
#  visualizing the distribution of 'SepalLengthCm' column
plt.figure(figsize=(8, 6))
sns.histplot(dataset['SepalLengthCm'], kde=True, color='blue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()
# Example: visualizing the distribution of 'SepalWidth' column
plt.figure(figsize=(8, 6))
sns.histplot(dataset['SepalWidthCm'], kde=True, color='blue')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.show()
# Example: visualizing the distribution of 'PetalLengthCm' column
plt.figure(figsize=(8, 6))
sns.histplot(dataset['PetalLengthCm'], kde=True, color='blue')
plt.title('Distribution of Petal Length')
plt.xlabel('PetalLengthCm')
plt.ylabel('Frequency')
plt.show()
# Example: visualizing the distribution of 'PetalWidthCm' column
plt.figure(figsize=(8, 6))
sns.histplot(dataset['PetalWidthCm'], kde=True, color='blue')
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.show()

# Plot a bar chart to show the frequency of categories in a categorical variable
# Example: visualizing the frequency of categories in the 'species' column
plt.figure(figsize=(8, 6))
sns.countplot(x='Species', data=dataset, palette='viridis')
plt.title('Frequency of Categories in Species')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.show()

# Create a scatter plot to visualize the relationship between two numerical variables
print("Scatter plot ")
# Example: visualizing the relationship between 'sepal_length' and 'sepal_width'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', data=dataset, hue='Species', palette='viridis')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
# Example: visualizing the relationship between 'sepal_length' and 'sepal_width'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', data=dataset, hue='Species', palette='viridis')
plt.title('Scatter Plot of Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

import pandas as pd

# Load the Iris dataset
dataset = pd.read_csv('/content/Iris.csv')

# Group data by the categorical variable 'species' and calculate mean and median for each group
grouped_data = dataset.groupby('Species')

# Calculate mean for each group
mean_grouped = grouped_data.mean()
print("\nMean for each group (species):")
print(mean_grouped)

# Calculate median for each group
median_grouped = grouped_data.median()
print("\nMedian for each group (species):")
print(median_grouped)

# Calculate Standard Deviation for each group
std_grouped = grouped_data.std()
print("\nStandard Deviation for each group (species):")
print(median_grouped)

# Calculate Varience for each group
var_grouped = grouped_data.var()
print("\nVarience for each group (species):")
print(var_grouped)

import pandas as pd

# Load a time series dataset

dataset = pd.read_csv('/content/Electric_Production.csv')

# Convert the date column to datetime type
dataset['DATE'] = pd.to_datetime(dataset['DATE'])

# Set the date column as the index for the DataFrame
dataset.set_index('DATE', inplace=True)

# Aggregate data by daily averages
daily_avg = dataset.resample('D').mean()
print("\nDaily averages:")
print(daily_avg)

# Aggregate data by weekly averages
weekly_avg = dataset.resample('W').mean()
print("\nWeekly averages:")
print(weekly_avg)

# Aggregate data by monthly averages
monthly_avg = dataset.resample('M').mean()
print("\nMonthly averages:")
print(monthly_avg)
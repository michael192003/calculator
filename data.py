import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

def load_csv():
    """Load a CSV file in three ways: upload, input URL, or hardcoded URL."""
    choice = input("Choose CSV source (1: Upload, 2: Input URL, 3: Hardcoded URL): ")
    if choice == "1":
        uploaded = files.upload()
        filename = list(uploaded.keys())[0]
    elif choice == "2":
        url = input("Enter CSV URL: ")
        filename = url
    elif choice == "3":
        filename = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"  # Example
    else:
        print("Invalid choice. Using default CSV.")
        filename = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    
    return pd.read_csv(filename)

def explore_data(df):
    """Print headings and first two rows, store column names."""
    print("\nColumn Names:", df.columns.tolist())
    print("\nFirst Two Rows:\n", df.head(2))

def plot_data(df):
    """Allow the user to select columns and plot data as scatter or line graph."""
    print("Available columns:", df.columns.tolist())
    x_col = input("Enter column name for X-axis: ")
    y_col = input("Enter column name for Y-axis: ")
    
    if x_col not in df.columns or y_col not in df.columns:
        print("Invalid column names. Try again.")
        return
    
    x = np.array(df[x_col])
    y = np.array(df[y_col])
    
    plot_type = input("Choose plot type (scatter/line): ").strip().lower()
    plt.figure(figsize=(8,5))
    
    if plot_type == "scatter":
        plt.scatter(x, y, color='b', label=f'{x_col} vs {y_col}')
    else:
        plt.plot(x, y, color='r', marker='o', linestyle='-', label=f'{x_col} vs {y_col}')
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{x_col} vs {y_col}')
    plt.legend()
    plt.grid()
    plt.show()

# Run the functions
df = load_csv()
explore_data(df)
plot_data(df)

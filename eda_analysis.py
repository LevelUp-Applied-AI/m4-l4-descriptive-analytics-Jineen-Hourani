"""Lab 4 — Descriptive Analytics: Student Performance EDA

Conduct exploratory data analysis on the student performance dataset.
Produce distribution plots, correlation analysis, hypothesis tests,
and a written findings report.

Usage:
    python eda_analysis.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import io
path = "data/student_performance.csv"

def load_and_profile(filepath):
    """Load the dataset and generate a data profile report.

    Args:
        filepath: path to the CSV file (e.g., 'data/student_performance.csv')

    Returns:
        DataFrame: the loaded dataset

    Side effects:
        Saves a text profile to output/data_profile.txt containing:
        - Shape (rows, columns)
        - Data types for each column
        - Missing value counts per column
        - Descriptive statistics for numeric columns
    """
    # TODO: Load the dataset and report its shape, data types, missing values,
    #       and descriptive statistics to output/data_profile.txt
    df = pd.read_csv(filepath)
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_text = buffer.getvalue()

    with open("output/data_profile.txt", "w") as f:
        f.write("--- Data Profile Report ---\n\n")
        f.write(f"Shape: {df.shape}\n\n")
        f.write(f"info: {info_text}\n\n")
        f.write("Missing Values:\n")
        f.write(df.isnull().sum().to_string())
    # Impute commute_minutes with median (10% missing)
    df['commute_minutes'] = df['commute_minutes'].fillna(df['commute_minutes'].median())
    # Replacing both literal "None" strings and actual Nulls
    df['scholarship'] = df['scholarship'].fillna('No Scholarship').replace('None', 'No Scholarship')


    # Drop rows with missing study_hours_weekly (5% missing)
    df = df.dropna(subset=['study_hours_weekly'])
    return df

def plot_distributions(df):
    """Create distribution plots for key numeric variables.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        None

    Side effects:
        Saves at least 3 distribution plots (histograms with KDE or box plots)
        as PNG files in the output/ directory. Each plot should have a
        descriptive title that states what the distribution reveals.
    """
    # Set a global colorblind-safe palette
    sns.set_palette('colorblind')
    # TODO: Create distribution plots for numeric columns like GPA,
    #       study hours, attendance, and commute minutes
    # TODO: Use histograms with KDE overlay (sns.histplot) or box plots
    # TODO: Save each plot to the output/ directory

    # --- Plot 1: GPA Distribution ---

    # Setup the figure and axis using Object-Oriented style
    fig, ax = plt.subplots(figsize=(8, 5))

    #Select plot type (Histogram with KDE)
    #pass the 'ax' object to Seaborn to draw inside our prepared frame
    sns.histplot(data=df, x='gpa', kde=True, color='teal', ax=ax)
    
    #descriptive titles and labels
    ax.set_title('Distribution of Student GPA at Hashemite Technical University')
    ax.set_xlabel('GPA')
    ax.set_ylabel('Frequency')
    
    #Final layout adjustments and saving
    plt.tight_layout()
    fig.savefig('output/gpa_distribution.png')
    
    #Close the figure to free up memory
    plt.close(fig)


     # --- Plot 2: study_hours_weekly per department Distribution ---
     
    # Setup the figure and axis using Object-Oriented style
    fig, ax = plt.subplots(figsize=(8, 5))
    #Select plot type (Boxplot)
    #pass the 'ax' object to Seaborn to draw inside our prepared frame
    sns.boxplot(data=df,x= 'department',y='study_hours_weekly', color= 'indianred', ax=ax)
    plt.xticks(rotation=45)
    #descriptive titles and labels
    ax.set_title('Distribution of Student study_hours_weekly per department at HTU')
    ax.set_xlabel('department')
    ax.set_ylabel('study_hours_weekly')
    #Final layout adjustments and saving
    plt.tight_layout()
    fig.savefig('output/SHW_distribution.png') 
    #Close the figure to free up memory
    plt.close(fig)

    # --- Plot 3: Attendance by Scholarship and Internship Status ---
    
    # 1. Setup the figure
    fig, ax = plt.subplots(figsize=(12, 6))
    # 2. Draw the Bar Chart
    # By default, barplot shows the MEAN (average) of attendance_pct
    sns.barplot(
    data=df.assign(has_internship=df['has_internship'].map({'Yes': 'Has Internship', 'No': 'No Internship'})), 
    x='scholarship', 
    y='attendance_pct', 
    hue='has_internship', 
    ax=ax
    )
    # 3. Formatting
    ax.set_title('Average Attendance by Scholarship Type & Internship Status')
    ax.set_xlabel('Scholarship Category')
    ax.set_ylabel('Average Attendance %')
    plt.xticks(rotation=45)
    
    # Move the legend to a spot where it doesn't cover the bars
    ax.legend(title='Internship Status', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    fig.savefig('output/attendance_bar_advanced.png')
    plt.close(fig)



def plot_correlations(df):
    """Analyze and visualize relationships between numeric variables.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        None

    Side effects:
        Saves at least one correlation visualization to the output/ directory
        (e.g., a heatmap, scatter plot, or pair plot).
    """
    # TODO: Compute the correlation matrix for numeric columns
    # TODO: Create a heatmap or scatter plots showing key relationships
    # TODO: Save the visualization(s) to the output/ directory
    
    # --- Step 1: Compute Correlation Matrix for all numeric columns ---
    # We must filter only numeric columns because correlation can't be calculated for strings
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()

    # --- Step 2: Annotated Heatmap (Overall View) ---
    # This helps us see all relationships at once
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax1)
    ax1.set_title('Overall Pearson Correlation Heatmap')
    plt.tight_layout()
    fig1.savefig('output/correlation_heatmap.png')
    plt.close(fig1)

    # --- Step 3: Specific Scatter Plot (study_hours_weekly vs gpa) ---
    # This visualizes the relationship between effort and performance
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='study_hours_weekly', y='gpa', alpha=0.6, color='blue', ax=ax2)
    ax2.set_title('Correlation: Study Hours vs. GPA')
    ax2.set_xlabel('Weekly Study Hours')
    ax2.set_ylabel('GPA')
    plt.tight_layout()
    fig2.savefig('output/study_vs_gpa_scatter.png')
    plt.close(fig2)

    # --- Step 4: Specific Scatter Plot (commute_minutes vs attendance_pct) ---
    # This investigates if longer commute leads to lower attendance
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='commute_minutes', y='attendance_pct', alpha=0.6, color='red', ax=ax3)
    ax3.set_title('Correlation: Commute Minutes vs. Attendance %')
    ax3.set_xlabel('Commute Minutes')
    ax3.set_ylabel('Attendance Percentage')
    plt.tight_layout()
    fig3.savefig('output/commute_vs_attendance_scatter.png')
    plt.close(fig3)

    print("Correlation plots have been saved successfully to the output/ directory.")



def run_hypothesis_tests(df):
    """Run statistical tests to validate observed patterns.

    Args:
        df: pandas DataFrame with the student performance data

    Returns:
        dict: test results with keys like 'internship_ttest', 'dept_anova',
              each containing the test statistic and p-value

    Side effects:
        Prints test results to stdout with interpretation.

    Tests to consider:
        - t-test: Does GPA differ between students with and without internships?
        - ANOVA: Does GPA differ across departments?
        - Correlation test: Is the correlation between study hours and GPA significant?
    """
    # TODO: Run at least two hypothesis tests on patterns you observe in the data
    # TODO: Report the test statistic, p-value, and your interpretation
    """Run statistical tests to validate observed patterns."""
    print("\n" + "="*30)
    print("HYPOTHESIS TESTING RESULTS")
    print("="*30)

    # --- Hypothesis 1: Internship vs GPA (Independent T-Test) ---
    # 1. Separate the two groups
    with_internship = df[df['has_internship'] == 'Yes']['gpa']
    no_internship = df[df['has_internship'] == 'No']['gpa']

    # 2. Run the t-test
    t_stat, p_val_t = stats.ttest_ind(with_internship, no_internship)

    # 3. Calculate Cohen's d (Effect Size) - Simple formula
    # (Mean1 - Mean2) / Pooled Standard Deviation
    combined_std = np.sqrt((with_internship.std()**2 + no_internship.std()**2) / 2)
    cohens_d = (with_internship.mean() - no_internship.mean()) / combined_std

    print(f"\n1. T-TEST: GPA vs Internship")
    print(f"   t-statistic: {t_stat:.4f}")
    print(f"   p-value: {p_val_t:.4f}")
    print(f"   Cohen's d: {cohens_d:.4f}")
    
    if p_val_t < 0.05:
        print("   Interpretation: Significant difference! Internships impact GPA.")
    else:
        print("   Interpretation: No significant difference found.")

    # --- Hypothesis 2: Scholarship vs Department (Chi-Square) ---
    # 1. Create a contingency table (Crosstab)
    contingency_table = pd.crosstab(df['scholarship'], df['department'])

    # 2. Run the Chi-Square test
    chi2, p_val_chi, dof, expected = stats.chi2_contingency(contingency_table)

    print(f"\n2. CHI-SQUARE: Scholarship vs Department")
    print(f"   Chi-square stat: {chi2:.4f}")
    print(f"   p-value: {p_val_chi:.4f}")
    print(f"   Degrees of Freedom: {dof}")

    if p_val_chi < 0.05:
        print("   Interpretation: Significant association between Scholarship and Dept.")
    else:
        print("   Interpretation: No significant association found.")

    # Return results in a dictionary as requested
    return {
        'internship_ttest': {'t_stat': t_stat, 'p_value': p_val_t},
        'scholarship_chi2': {'chi2_stat': chi2, 'p_value': p_val_chi}
    }


def main():
    """Orchestrate the full EDA pipeline."""
    os.makedirs("output", exist_ok=True)

    # TODO: Load and profile the dataset
    df = load_and_profile(path)
    # TODO: Generate distribution plots
    plot_distributions(df)
    # TODO: Analyze correlations
    plot_correlations(df)
    # TODO: Run hypothesis tests
    run_hypothesis_tests(df)
    # TODO: Write a FINDINGS.md summarizing your analysis

if __name__ == "__main__":
    main()

# Student Performance Analysis Report - HTU
**Author:** Jineen Hourani  
**Date:** April 2026

## 1. Dataset Description
The dataset contains performance metrics for **2,000 students** at Hashemite Technical University (HTU), across **10 columns** including academic, behavioral, and demographic data.

### Notable Data Quality Issues:
* **Missing Values:** `scholarship` had 389 missing values (approx. 20%), and `commute_minutes` had 181 missing values.
* **Data Inconsistency:** The `scholarship` column contained mixed representations of "None" and actual Nulls, which were cleaned and categorized as "No Scholarship" for accurate analysis.
* **Imputation:** Commute times were filled using the median to maintain data integrity without skewing the distribution.

## 2. Key Distribution Findings
* **GPA Distribution:** The GPA follows a nearly normal distribution centered around **2.7 - 2.8**, indicating a healthy spread of academic performance across the student body. (See `output/gpa_distribution.png`).
* **Departmental Study Habits:** Box plots reveal that study hours are relatively consistent across departments (Biology, CS, Engineering, etc.), with a median of approximately **15 hours per week**. However, Engineering and Mathematics show slightly more outliers in high study hours. (See `output/SHW_distribution.png`).
* **Attendance Trends:** Average attendance remains high (above 70%) across all scholarship categories. Interestingly, students with "No Scholarship" maintain attendance levels comparable to those with Merit or Athletic scholarships. (See `output/attendance_bar_advanced.png`).

## 3. Notable Correlations
* **Strongest Relationship:** A strong positive correlation (**0.64**) exists between **Weekly Study Hours and GPA**. As study hours increase, GPA tends to rise significantly. (See `output/study_vs_gpa_scatter.png`).
* **Weakest Relationship:** There is **zero correlation (-0.00)** between **Commute Minutes and Attendance Percentage**. This surprising finding suggests that students manage to attend classes regardless of their travel distance. (See `output/commute_vs_attendance_scatter.png`).
* **Caveat:** While study hours and GPA are highly correlated, this does not strictly imply *causation*. Other factors like prior knowledge or study quality may influence both.

## 4. Hypothesis Test Results

### Hypothesis 1: Internship Impact
* **Hypothesis:** Students with internships have a higher GPA than those without.
* **Test Used:** Independent Samples T-Test.
* **Results:** t-statistic = **13.56**, p-value = **0.0000**.
* **Effect Size (Cohen's d):** **0.7061** (Large effect).
* **Interpretation:** The result is **statistically significant**. Internships have a substantial positive impact on academic performance.

### Hypothesis 2: Scholarship Distribution
* **Hypothesis:** Scholarship status is associated with specific departments.
* **Test Used:** Chi-Square Test of Independence.
* **Results:** Chi-square = **17.13**, p-value = **0.3769**.
* **Interpretation:** The result is **NOT statistically significant**. This indicates that scholarships are distributed fairly across all departments without bias toward any specific field.

## 5. Actionable Recommendations
1. **Expand Internship Programs:** Given the high correlation (0.64) and significant T-test results (p < 0.05), the university should partner with more industry leaders to provide internships, as they are a proven driver for higher GPA.
2. **Promote Study-Hour Workshops:** Since study hours are the primary numeric predictor of GPA, providing "Smart Studying" workshops could help students maximize the impact of their 15-hour weekly average.
3. **Maintain Fair Scholarship Policies:** The Chi-Square test confirmed a fair distribution of financial aid. The university should continue this unbiased approach to support diversity across all academic modules.
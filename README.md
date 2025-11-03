# Week 4 Assignment: AI in Software Engineering

**Student:** Langat Jackson Mutiso  
**Institution:** Power Learn Project  
**Theme:** Building Intelligent Software Solutions 💻🤖  
**Date:** [Insert Date]  

## Overview

This assignment demonstrates the application of AI in software engineering through theoretical analysis, practical implementation, and ethical reflection. It covers AI-driven code generation, automated testing, predictive analytics for resource allocation, and a bonus innovation proposal. The deliverables include well-commented code, performance metrics, screenshots, and analyses as per the grading rubric (Theoretical Depth & Accuracy: 30%, Code Functionality & Quality: 50%, Ethical Reflection: 10%, Creativity & Presentation: 10%).

## Table of Contents

- [Theoretical Analysis](#theoretical-analysis)
- [Practical Implementation](#practical-implementation)
  - [Task 1: AI-Powered Code Completion](#task-1-ai-powered-code-completion)
  - [Task 2: Automated Testing with AI Framework](#task-2-automated-testing-with-ai-framework)
  - [Task 3: Predictive Analytics for Resource Allocation](#task-3-predictive-analytics-for-resource-allocation)
- [Ethical Reflection](#ethical-reflection)
- [Bonus Task: Innovation Challenge](#bonus-task-innovation-challenge)
- [Submission Guidelines](#submission-guidelines)
- [Dependencies and Setup](#dependencies-and-setup)
- [Results and Outputs](#results-and-outputs)

## Theoretical Analysis

### Short Answer Questions

**Q1: Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?**  
AI tools like Copilot use machine learning on vast codebases to suggest completions, reducing time spent on boilerplate code and debugging. Limitations include potential biases from training data, over-reliance leading to unoriginal code, and security risks if suggestions include vulnerabilities.

**Q2: Compare supervised and unsupervised learning in the context of automated bug detection.**  
Supervised learning trains on labeled bug data for classification (e.g., predicting bug types). Unsupervised learning clusters anomalies without labels, useful for novel bugs but less precise.

**Q3: Why is bias mitigation critical when using AI for user experience personalization?**  
AI can perpetuate biases from data, leading to unfair personalization (e.g., excluding minorities). Mitigation ensures inclusivity and ethical deployment.

### Case Study Analysis

**AIOps in DevOps:** AIOps automates deployment by analyzing logs and metrics to predict failures, improving efficiency through proactive issue resolution and reduced downtime.

## Practical Implementation

### Task 1: AI-Powered Code Completion

**Objective:** Compare manual vs. AI-suggested Python functions for sorting dictionaries by key, including efficiency analysis.

**Files:** `ai_code_completion.py`

**Key Features:**
- Manual function: Direct lambda sorting (fast but assumes key exists).
- AI-suggested function: Error-handling with `item.get()` (robust but slight overhead).
- Timing comparison on sample data.
- ~200-word analysis: Manual preferred for speed in controlled environments; AI for reliability.

**Execution:** Run `python ai_code_completion.py` to see outputs (results and times).

### Task 2: Automated Testing with AI Framework

**Objective:** Automate login tests for valid/invalid credentials using Selenium with AI plugins (e.g., Testim.io), capture results, and explain AI's role in improving coverage.

**Files:** `selenium_test.py`, `login_test_result.png`

**Key Features:**
- Tests demo site (https://the-internet.herokuapp.com/login).
- Validates success/failure messages.
- Saves screenshot post-test.
- ~150-word summary: AI enhances coverage by automating generation, detecting changes, and integrating CI/CD.

**Execution:** Run `python selenium_test.py` (requires ChromeDriver; outputs test results and screenshot).

### Task 3: Predictive Analytics for Resource Allocation

**Objective:** Preprocess breast cancer dataset, train RandomForest to predict malignancy, evaluate with accuracy and F1-score.

**Files:** `predictive_analytics.ipynb`, `executed_predictive_analytics.ipynb`

**Key Features:**
- Dataset: sklearn's load_breast_cancer (569 samples, 30 features).
- Preprocessing: Scaling with StandardScaler (no missing values).
- Model: RandomForestClassifier (accuracy: 96.49%, F1: 96.47%).
- Outputs: Classification report for Malignant/Benign.

**Execution:** Open in Jupyter Notebook and run cells for metrics.

## Ethical Reflection

In deploying the predictive model, biases may arise from underrepresented demographics in the dataset (e.g., skewed towards certain populations). Tools like IBM AI Fairness 360 can audit and mitigate biases through fairness metrics and reweighting. Ethical AI requires transparency, consent, and continuous monitoring to ensure equitable outcomes.

## Bonus Task: Innovation Challenge

**Proposal: AutoDocify – AI-Powered Documentation Assistant**

**Purpose:** Automate documentation generation from code comments and Git history to reduce manual effort.

**Workflow:**
1. Parse codebases for comments and functions.
2. Extract logic and generate Markdown reports.
3. Suggest diagrams (e.g., via AI image generation).
4. Integrate with Git for versioned docs.

**Impact:** Enhances collaboration, ensures consistency, and frees developers for core tasks. Potential for open-source adoption in agile teams.

## Submission Guidelines

- **Code:** Shared on GitHub (this repo).
- **Report:** PDF with answers, screenshots, reflections (separate file).
- **Presentation:** 3-minute video demo (link in repo or shared separately).
- **Grading Focus:** Functionality, analysis depth, ethics, creativity.

## Dependencies and Setup

- **Python 3.x**
- Libraries: `selenium`, `scikit-learn`, `pandas`, `time` (install via `pip install selenium scikit-learn pandas`)
- ChromeDriver for Selenium (download from https://chromedriver.chromium.org/)
- Jupyter for notebooks

Run scripts in the project directory.

## Results and Outputs

- **Task 1:** Timing outputs (e.g., ~0.0s for both functions).
- **Task 2:** Test results (2/2 passed), screenshot (`login_test_result.png`).
- **Task 3:** Accuracy: 96.49%, F1: 96.47%, full report.
- All analyses included in code comments/docstrings.

For issues or questions, contact [Your Email].

---

**Prepared by:** Langat Jackson Mutiso  
**Institution:** Power Learn Project

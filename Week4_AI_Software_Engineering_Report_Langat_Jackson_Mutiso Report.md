# Week 4 AI Software Engineering Report

**Name:** Langat Jackson Mutiso  
**Institution:** Power Learn Project  
**Course:** AI Software Engineering  
**Week:** 4  
**Topic:** AI-Driven Software Testing (with Selenium Integration)

---

## 1. Theoretical Analysis

### 1.1 Introduction

AI-driven software engineering involves integrating artificial intelligence into different stages of software development — from requirement analysis, design, coding, testing, to maintenance. In testing, AI helps improve accuracy, reduce human error, and speed up the testing process by automating complex test cases.

### 1.2 Objective

To understand how AI can enhance software testing, particularly through frameworks like Selenium combined with intelligent analysis models.

### 1.3 Key Concepts

- **AI Testing:** Use of AI techniques to predict bugs, generate test cases, and improve regression testing.  
- **Selenium:** An open-source tool used to automate web browsers. It interacts with web elements and verifies functionalities.  
- **Automation Pipeline:** Integration of Selenium tests into CI/CD workflows enhanced by AI-based optimizers.  
- **Neural Models in QA:** Machine learning can prioritize test cases and predict fault-prone modules.  

---

## 2. Practical Implementation

### 2.1 Project Setup

We build a Python-based testing module that uses Selenium for browser automation. The AI layer (in future versions) can learn from past failures to suggest improvements.

### 2.2 Code Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open site
driver.get("https://example.com")
time.sleep(2)

# Perform test
title = driver.title
print("Page Title:", title)

assert "Example Domain" in title, "Test Failed: Title mismatch."

# Close browser
driver.quit()
```

### 2.3 Explanation

- **webdriver.Chrome():** Launches Chrome for automation.  
- **driver.get():** Navigates to the test site.  
- **assert:** Verifies expected output.  
- **driver.quit():** Closes the session.  

### 2.4 Output Example

```
Page Title: Example Domain
Test Passed!
```

---

## 3. Ethical Reflection

AI testing automation reduces manual workload but can also displace entry-level QA roles. Ethical AI development demands that automation complements, not replaces, human insight. Teams must ensure fairness, transparency, and explainability in AI-driven tools.  

---

## 4. Bonus Task — Research Proposal

### Title: Enhancing Software Testing Using AI-based Predictive Models

**Objective:** To design a predictive testing model that learns from historical bug data to forecast potential code vulnerabilities.  

**Methodology:**  

1. Data collection from past test results.  
2. Train a neural network to classify modules as low or high risk.  
3. Integrate predictions into Selenium scripts.  

**Expected Outcome:** Reduction in repetitive test failures, improved coverage, and intelligent prioritization of test cases.  

---

## 5. Conclusion

The integration of AI and Selenium demonstrates the evolving nature of software engineering. AI testing improves speed, reliability, and efficiency while paving the way for smarter DevOps pipelines.

---

**Prepared by:** Langat Jackson Mutiso  
**Institution:** Power Learn Project  
**Instructor:** [Your Mentor’s Name Here]  
**Date:** November 2025

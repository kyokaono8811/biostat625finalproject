biostats625finalproject
================

## Overview

<!-- badges: start -->

<!-- badges: end -->

The goal of this project is to find a machine learning model that yields
high performance for reflecting the association between the predictor
variables and the prevalence of heart attack within the study cohort.
Three classic machine learning models were used, which includes Logistic
Regression, Random Forest, and Logistic Generative Additive Model (GAM).
Model performance was compared using evaluation metrics such as
Accuracy, Precision, Recall, F1 Score, and AUROC.

## Data Background

This dataset is retrieved from the CDC Behavioral Risk Factor
Surveillance System (BRFSS) on Kaggle from 2022, and contains
observations of over 20,000 survey patients in the U.S.

## Installation

To run the python code on R Markdown, run the following code on the R
console first.

``` r
#install.packages("reticulate")
```

Then, run the following code on R chunk.

``` r
#library(reticulate)
```

Install and import all the necessary packages (e.g. pandas, matplotlib)
on the python chunk.

``` r
#reticulate::py_install("matplotlib")
#reticulate::py_install("pandas")
```

``` python
#import pandas as pd
#import matplotlib.pyplot as plt 
```

## Resuts Summary

All the models computed high AUROC, presenting high performance ability
in classifying between patients who had heart attack and those who did
not.

``` r
knitr::include_graphics("/Users/kyokaono/Desktop/roc_curve_comparison.png")
```

<img src="../roc_curve_comparison.png" width="1140" />

## Contributions

- Xiaoyu Lin: data description, data cleaning, writing report
- Kyoka Ono: model training, model evaluation, writing report

## References

- Pytlak, K. (n.d.). Personal key indicators of heart disease \[Data
  set\]. Kaggle.
  <https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/data>

- Centers for Disease Control and Prevention. (2024, December 2). Heart
  disease risk factors.
  <https://www.cdc.gov/heart-disease/risk-factors/?CDC_AAref_Val=https://www.cdc.gov/heartdisease/risk_factors.htm>

- Al-Zaiti, S.S., Martin-Gill, C., Zègre-Hemsey, J.K. et al. Machine
  learning for ECG diagnosis and risk stratification of occlusion
  myocardial infarction. Nat Med 29, 1804–1813 (2023).
  <https://doi.org/10.1038/s41591-023-02396-3>

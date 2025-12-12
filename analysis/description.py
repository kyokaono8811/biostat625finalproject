import matplotlib.pyplot as plt
import numpy as np

def description(heart_clean):
    # Variables
    categorical_vars = [
        "HadHeartAttack", "Sex", "PhysicalActivities", "HadStroke",
        "HadDiabetes", "SmokerStatus", "RaceEthnicityCategory",
        "AgeCategory", "AlcoholDrinkers"
    ]
    
    numeric_vars = ["SleepHours", "BMI"]
    
    all_vars = categorical_vars + numeric_vars
    
    # Order of categorical variables
    category_orders = {
        "HadHeartAttack": [0, 1],
        "Sex": [0, 1],
        "PhysicalActivities": [0, 1],
        "HadStroke": [0, 1],
        "HadDiabetes": [0, 1],
        "AlcoholDrinkers": [0, 1],
        "SmokerStatus": [0, 1, 2],
        "RaceEthnicityCategory": [0, 1, 2, 3, 4],
        "AgeCategory": list(range(1, 14))
    }
    
    # Layout
    n_plots = len(all_vars)
    n_cols = 3
    n_rows = (n_plots + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(20, 4 * n_rows),
        sharey=False
    )
    
    axes = axes.flatten()
    
    for i, col in enumerate(all_vars):
        ax = axes[i]
    
        # Categorical variables: bar plots
        if col in categorical_vars:
            counts = heart_clean[col].value_counts().reindex(category_orders[col])
            ax.bar(counts.index, counts.values)
            ax.set_xticks(category_orders[col])
            ax.tick_params(axis="x", labelrotation=45, labelsize=9)
    
        # Numerical variables: histograms
        else:
            ax.hist(heart_clean[col], bins=20)
            ax.tick_params(axis="x", labelrotation=45, labelsize=9)
    
        ax.set_title(col, fontsize=12)
        ax.tick_params(axis="y", labelsize=9)
        ax.set_xlabel("")
        ax.set_ylabel("")
    
    # Remove empty panels
    for j in range(len(all_vars), len(axes)):
        fig.delaxes(axes[j])
    
    # Shared y-axis label
    fig.text(0.04, 0.5, "Count", va="center", rotation="vertical", fontsize=12)
    
    # Adjust spacing
    plt.subplots_adjust(
        wspace=0.4,  # horizontal space
        hspace=0.6   # vertical space
    )
    # Save the figure
    fig.savefig("graphs/all_variables_plot.png", dpi=300, bbox_inches="tight")
    return fig

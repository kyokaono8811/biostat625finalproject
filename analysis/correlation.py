import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def correlation(heart_clean):
    vars_of_interest = [
        "HadHeartAttack",
        "Sex",
        "PhysicalActivities",
        "SleepHours",
        "HadStroke",
        "HadDiabetes",
        "SmokerStatus",
        "RaceEthnicityCategory",
        "AgeCategory",
        "BMI",
        "AlcoholDrinkers"
    ]
    
    df_corr = heart_clean[vars_of_interest].copy()
    
    # Compute Spearman correlation
    corr = df_corr.corr(method="spearman")
    
    # Mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1, vmax=1,
        square=True,
        linewidths=0.5,
        annot_kws={"size": 7},
        cbar_kws={"shrink": 0.75},
        ax=ax
    )
    
    ax.set_title("Correlation Table", fontsize=12)
    
    fig.tight_layout()

    fig.savefig("graphs/correlation_table.png", dpi=300, bbox_inches="tight")

    return fig


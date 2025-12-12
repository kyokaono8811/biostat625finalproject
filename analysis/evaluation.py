from sklearn.metrics import (
    precision_score,accuracy_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, classification_report, average_precision_score
)

def evaluate_model(name, y_true, y_pred, y_proba):
    print(f"Model: {name}")

    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred, pos_label=1))
    print("Recall:", recall_score(y_true, y_pred, pos_label=1))
    print("F1 Score:", f1_score(y_true, y_pred, pos_label=1))
    print("ROC-AUC:", roc_auc_score(y_true, y_proba))
    print("PR-AUC:", average_precision_score(y_true, y_proba))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, digits=3))

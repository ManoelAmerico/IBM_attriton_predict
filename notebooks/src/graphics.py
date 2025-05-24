import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(palette="bright")

PALETTE = "coolwarm"
SCATTER_ALPHA = 0.2


def plot_coefficients(df_coefs, title="Coefficients"):
    df_coefs.plot.barh(figsize=(10, 15))
    plt.title(title)
    plt.axvline(x=0, color=".5")
    plt.xlabel("Coefficients")
    plt.gca().get_legend().remove()
    plt.show()


def plot_compare_model_metrics(df_results):
    fig, axs = plt.subplots(4, 2, figsize=(9, 9), sharex=True)

    metric_columns = [
        "time_seconds",
        "test_accuracy",
        "test_balanced_accuracy",
        "test_f1",
        "test_precision",
        "test_recall",
        "test_roc_auc",
        "test_average_precision",
    ]

    metric_names = [
        "Time (s)",
        "Accuracy",
        "Balanced Accuracy",
        "F1",
        "Precision",
        "Recall",
        "AUROC",
        "AUPRC",
    ]

    for ax, metric, name in zip(axs.flatten(), metric_columns, metric_names):
        sns.boxplot(
            x="model",
            y=metric,
            data=df_results,
            ax=ax,
            showmeans=True,
        )
        ax.set_title(name)
        ax.set_ylabel(name)
        ax.tick_params(axis="x", rotation=90)

    plt.tight_layout()
    plt.show()
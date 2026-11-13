import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_target_by_category(data: pd.DataFrame, feature: str, target: str = 'default') -> None:
    """
    Ploting percent and count distribution target by category

    Parameters:

    data: pd.DataFrame
        processed data

    feature: str
        The category by whitch divide the target

    target: str
        Target of data

    Output:
    None
    """
    group_v = (
    data.groupby(feature)[target]
    .value_counts(normalize=True)
    .mul(100)
    .rename('percent')
    .reset_index()
    )

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

    sns.barplot(data=group_v, x=feature, hue=target, y='percent', ax= axes[0])
    for container in axes[0].containers:
        labels = [f'{float(v.get_height()):.2f}%' for v in container]
        axes[0].bar_label(container, labels=labels)
    axes[0].set_title(f'Процентное распределение таргета по группам в признаке {feature}')

    sns.countplot(data=data, x=feature, hue=target, ax=axes[1])
    for container in axes[1].containers:
        axes[1].bar_label(container)
    axes[1].set_title(f'Количественное распределение таргета по группам в признаке {feature}')

    plt.tight_layout()
    plt.show()


def main():
    pass

if __name__ == "__main__":
    main()
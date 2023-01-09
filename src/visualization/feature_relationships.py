import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sns.set(style="dark")


def vis_corr_matrix(df: pd.DataFrame) -> None:
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ullamcorper leo ut dignissim
    vulputate.
    Args:
        param1 (str): Description of `param1`.
    Returns:
        Lorem ipsum dolor sit amet
    """
    corr = df.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    plt.figure(figsize=(13, 13))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    with sns.axes_style("white"):
        sns.heatmap(corr, cmap=cmap, center=0, mask=mask,
                    square=True, linewidths=1.5, cbar_kws={"shrink": .5})

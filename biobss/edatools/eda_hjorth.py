from numpy.typing import ArrayLike

from biobss.common.signal_hjorth import *


def eda_hjorth_features(sig: ArrayLike, prefix="eda") -> dict:
    """Calculates Hjörth features for the EDA signal.
    For more details, see the https://en.wikipedia.org/wiki/Hjorth_parameters .

    Args:
        signal (ArrayLike): EDA signal.
        prefix (str, optional): Prefix for the features. Defaults to "eda".

    Returns:
        dict: Dictionary of calculated features.
    """

    h_features = {}
    h_features[prefix + "_activity"] = hjorth_activity(sig)
    h_features[prefix + "_complexity"], h_features[prefix + "_mobility"] = hjorth_complexity_mobility(sig)

    return h_features
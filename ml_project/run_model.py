from os import getcwd

import pandas as pd
from hydra.utils import instantiate
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate

from ml_project.metrics_storage import MetricStorage
from ml_project.structured_config import MLProjectConfig


def run_model(cfg: MLProjectConfig):
    # generate data, split, fit and score.
    X, y = make_classification(n_samples=1000)
    estimator = RandomForestClassifier(
        n_estimators=cfg.hyperparameters.n_estimators,
        criterion=cfg.hyperparameters.criterion.name,
        n_jobs=cfg.hyperparameters.n_jobs,
        random_state=cfg.hyperparameters.random_state,
    )
    cv_metrics = cross_validate(estimator, X, y, **cfg.cross_validation)

    # store metrics in DataFrame
    metrics = pd.DataFrame(cv_metrics)
    metrics["fold"] = metrics.index + 1
    metrics["hydra_dir"] = getcwd()

    # send to metrics storage
    metrics_storage: MetricStorage = instantiate(cfg.metrics_storage)
    metrics_storage.save(metrics)

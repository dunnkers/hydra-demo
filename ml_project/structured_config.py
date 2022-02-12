from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING


class Criterion(Enum):
    gini = 1
    entropy = 2


@dataclass
class RandomForestHyperparameters:
    n_estimators: Optional[int] = None
    criterion: Criterion = Criterion.gini
    n_jobs: Optional[int] = None
    random_state: Optional[int] = None


@dataclass
class CrossValidationConfig:
    cv: Optional[int] = None
    n_jobs: Optional[int] = None


@dataclass
class MetricStorageConfig:
    _target_: str = MISSING


@dataclass
class CSVFileConfig(MetricStorageConfig):
    filepath: str = MISSING


@dataclass
class SQLDatabaseConfig(MetricStorageConfig):
    con: str = MISSING
    table_name: str = "metrics"


@dataclass
class MLProjectConfig:
    hyperparameters: RandomForestHyperparameters = MISSING
    cross_validation: CrossValidationConfig = MISSING
    metrics_storage: MetricStorageConfig = MISSING


cs = ConfigStore.instance()
cs.store(name="base_config", node=MLProjectConfig)
cs.store(name="base_csv_file", node=CSVFileConfig, group="metrics_storage")
cs.store(name="base_sql_database", node=SQLDatabaseConfig, group="metrics_storage")

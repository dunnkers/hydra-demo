from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from ml_project.structured_config import CSVFileConfig, SQLDatabaseConfig


class MetricStorage:
    def save(self, results: pd.DataFrame):
        ...


@dataclass
class CSVFile(MetricStorage, CSVFileConfig):
    def save(self, results: pd.DataFrame):
        add_header = not Path(self.filepath).exists()
        results.to_csv(self.filepath, index=False, mode="a", header=add_header)
        print(f"wrote {len(results)} rows to {self.filepath} ✓")


@dataclass
class SQLDatabase(MetricStorage, SQLDatabaseConfig):
    def save(self, results: pd.DataFrame):
        results.to_sql(name=self.table_name, con=self.con, if_exists="append")
        print(f"wrote {len(results)} rows to {self.table_name} ✓")

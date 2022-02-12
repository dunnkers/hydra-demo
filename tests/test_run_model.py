from pathlib import Path
from tempfile import mkdtemp

import pandas as pd
from hydra import compose, initialize
from ml_project.run_model import run_model


def test_default_params():
    with initialize(config_path="../ml_project/conf"):
        # store metrics in SQLite DB, in a temporary dir
        metrics_file = Path(mkdtemp()) / "ml_project-results.sqlite"
        con = f"sqlite:///{metrics_file}"

        # compose config & run: simulates running via commandline
        cfg = compose(
            config_name="my_config",
            overrides=[
                "metrics_storage=sql_database",
                f"metrics_storage.con={con}",
            ],
        )
        run_model(cfg)

        # ensure metrics were correctly written
        metrics = pd.read_sql("metrics", con=con)
        assert "test_score" in metrics.columns
        assert len(metrics) >= 0
        assert not metrics["test_score"].isna().any()

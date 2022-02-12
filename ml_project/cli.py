import hydra
from omegaconf import OmegaConf

from ml_project.run_model import run_model

from .structured_config import MLProjectConfig


@hydra.main(config_path="conf", config_name="my_config")
def main(cfg: MLProjectConfig):
    # print(OmegaConf.to_yaml(cfg))
    run_model(cfg)


if __name__ == "__main__":
    main()

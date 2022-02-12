# hydra-demo

Demonstrates use of [Hydra](https://hydra.cc) with a small sample app.

## Install
```shell
pip install -r requirements.txt
```

## Usage
```shell
python -m ml_project.cli --help
```

For example:

```shell
python -m ml_project.cli --multirun hyperparameters.n_estimators="range(20,120,20)"
```

## About
Built by [Jeroen Overschie](https://jeroenoverschie.nl) at [GoDataDriven](https://godatadriven.com/). © 2022.
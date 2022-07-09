# hydra-demo

Demonstrates use of [Hydra](https://hydra.cc) with a small sample app.

[![Screenshot 2022-07-09 at 18 53 26](https://user-images.githubusercontent.com/744430/178115397-ff6b027d-ad39-474c-8ec0-6cc14c8df866.png)](https://docs.google.com/presentation/d/e/2PACX-1vSV1hz0dGUZ7aQ5nxYEdSAxUxtzwLgvEZDXcC8PTfGjC5CdYCUG0bY9slLGXPcSpFl0GIP459LjeZPC/pub?start=false&loop=false&delayms=3000)


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

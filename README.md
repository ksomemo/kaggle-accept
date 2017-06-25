# kaggle-accept
automation for acception rules

## installation
```sh
pip install git+https://github.com/ksomemo/kaggle-accept
```

## usage
```sh
# prepare
pip install kaggle-cli
kg config -u username -p password -g

# accept
python -m kaggle_accept -c competition-name
```

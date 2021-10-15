import pandas as pd

### Hashing Parameters and Functions

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"
current_game = "948c8867a6582fdf55ef05b09030cb1afccf7d90f1d6844382577e2fc34e3419"

### Train Test Split Parameters
train_pct = 0.8

### Experiment Parameters
multiplier_checkout_level = 2
bet_size = 0.1 #USD
batch_starting_capital = 50 #USD
batch_size = 100

def get_experiment_parameters():
    config_parameters = pd.Series({'multiplier_checkout_level': multiplier_checkout_level,
                                   'bet_size': bet_size,
                                   'batch_starting_capital': batch_starting_capital,
                                   'batch_size': batch_size})

    return config_parameters
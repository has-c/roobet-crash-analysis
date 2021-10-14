import numpy as np
import hashlib
import random
import string
import hmac
import config


def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(config.salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2 ** 52
    return (((100 * e - h) / (e - h)) // 1) / 100.0


def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()


def get_all_multipliers(first_game, game_hash):
    results = []
    count = 0
    while game_hash != first_game:
        count += 1
        results.append(get_result(game_hash))
        game_hash = get_prev_game(game_hash)

    # append first game
    results.append(get_result(first_game))
    results = np.array(results)

    return results
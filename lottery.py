import argparse

import numpy as np
import pandas as pd

from pathlib import Path
from tabulate import tabulate



def print_pairs(seed: int, xls_path: str) -> None:

    rng = np.random.default_rng(seed)

    xls = pd.ExcelFile(xls_path)

    first_sheet = xls.parse(0)

    names = list(first_sheet.iloc[3:-1, 0])

    n_participants = len(names)

    assert n_participants % 2 == 0, f'The number of participants is uneven, please find one more participant!'

    n_teams = n_participants // 2

    rng.shuffle(names)

    i = 0

    first = []
    second = []

    while i < len(names):

        first.append(names[i])
        second.append(names[i+1])

        i += 2

    d = {'Team Mate A': first, 'Team Mate B': second}
    df = pd.DataFrame(data=d)

    print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex=range(1, n_teams +1)))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-p', '--path', type=str,  default=str(Path.home() / 'Downloads' / 'Doodle.xls'), help='path to Excel file')
    parser.add_argument('-s', '--seed', type=int,  default=42, help='seed for random generator')

    args = parser.parse_args()

    print_pairs(seed=args.seed, xls_path=args.path)

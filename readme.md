# Instructions

1) Download the Doodle survey as Excel file.

2) Change the seed in the command below.

## Mac

```bash
git clone https://github.com/MartinHahner/KickerLottery.git
cd KickerLottery
conda env create -f mac.yml
conda activate kicker
python lottery.py --seed 42
```

## Linux

```bash
git clone https://github.com/MartinHahner/KickerLottery.git
cd KickerLottery
conda env create -f linux.yml
conda activate kicker
python lottery.py --seed 42
```

3) Enjoy the tournament!

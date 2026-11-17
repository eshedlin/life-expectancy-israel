# Life expectancy in Israel since 1950
In 1950 Israel's life expectancy was 23.5 years above the world average;
in 2023 the gap was 9.2 years.

## Question
How has life expectancy at birth in Israel changed since 1950,
compared with the US, the UK and the world average?

## Data
Our World in Data, life expectancy at birth. See data/README.md.

## Method
Filter four entities, plot one line per entity, compare the gap over time.
The script `src/make_chart.py` does all of this and prints the key numbers.

## Key finding
Israel's life expectancy rose from 69.9 years in 1950 to 82.4 in 2023.
The gap to the world average narrowed from 23.5 years (69.9 vs 46.4)
to 9.2 years (82.4 vs 73.2), because the world rose much faster.
![Life expectancy 1950-2023](reports/figures/life-expectancy-1950-2023.png)

## How to reproduce
1. Download the CSV described in data/README.md into data/raw
2. From the project root, run `python src/make_chart.py`
3. The chart is saved to reports/figures and the gap numbers are printed

## Status
In progress

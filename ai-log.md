# AI log

How AI was used in this project, what was kept, what was rejected, and how it was checked.

## 1. Chart design
- Asked: make the line chart clearer and more impressive
- Kept: highlighted Israel, direct labels, gap arrows, source line
- How I checked: compared the 1950 and 2023 values on the chart with the CSV

## 2. Explanation for the 1950s dip
- Asked: why did life expectancy drop between 1950 and 1954?
- AI suggested: mass immigration and high infant mortality in transit camps
- Verified: infant mortality rose from 29.2 (1947) to 51.7 (1949), CBS 1952
- Not verified: the timing; infant mortality was already falling by 1953-54,
  and CBS five-year life tables show no drop
- Decision: marked on the chart as a verified fact, not as the cause

## 3. Wrong numbers in the key finding
- What happened: the README said the gap was 6.6 and 3.4 years
- How I caught it: the numbers contradicted the chart subtitle (23.5 and 9.2)
- Fix: the script now prints the gap numbers, so the README can be checked against it

## 4. README improvement
- Asked: rewrite the README for a reader who does not know epidemiology,
  without adding numbers, causes or claims
- Kept: finding and chart at the top, numbered method, 1950s note moved from data/README
- Changed: [what you edited in the draft, or "nothing"]
- How I checked: compared every number with the script output and the chart;
  looked for added causes and for "not verified" claims turned into facts
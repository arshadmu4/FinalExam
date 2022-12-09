# FinalExam

The file gasoline_prices.csv contains the state average gasoline prices for each state (and Washington, DC) in the United States on November 29, 2022 according to AAA. The file state_abb_codes.csv provides a mapping of states & districts in the United States with their abbreviations, and the file censusRegions.csv provides a mapping of states and districts based on census regions. 

For each of the census regions, these scripts in R and python compute the mean state (that is, remove Washington, D.C.) percentage increase (difference) in the price of Diesel vs Regular gasoline ( (Diesel - Regular)/Regular*100), along with the corresponding standard deviation and coefficient of variation.

Coefficient of variation: It is the standard deviation divided by variability. It gives us a good meaure of relative variability in a dataset.

Northeast, Midwest, and South have similar mean price differences between diesel and regular but the midwest has over twice the variability in price difference of the other two. The west on the other hand, on average, has a much lower difference between diesel and regular prices. However, the variability in the price differences is also much greater than the other three regions.

| Functionality      | In R               | In Python        |
|--------------------|--------------------|------------------|
| reading from csv   | read_csv()         | pd.read_csv()    |
| merging datasets   | merge()            | pd.merge()       |
| merging from left  | by.x =             | left_on =        |
| merging from right | by.y =             | right_on =       |
| removing state     | filter(state != x) | data[state != x] |
| grouping by        | groupby()          | .groupby()       |
| creating column    | mutate()           | .assign()        |
| summary statistics | summarize()        | .agg()           |

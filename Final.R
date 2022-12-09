## Umar Arshad
## December 9, 2022
## Final Exam


library(tidyverse)
## reading datasets
prices <- read_csv("https://tjfisher19.github.io/data/gasoline_prices.csv")
codes <- read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
regions <- read_csv("https://tjfisher19.github.io/data/censusRegions.csv")
## merging data together
finaldata <- merge(codes, prices,
                   by.x = "State", by.y = "State")
finaldata <- merge(finaldata, regions,
                   by.x = "Code", by.y = "State")%>%
  ## removing DC then grouping by region
  filter(State != "District of Columbia")%>%
  group_by(Region)%>%
  mutate(pricediff = ((Diesel - Regular)/Regular)*100)%>%
  #creating summary statistics for each region
  summarize(Price_Difference = mean(pricediff),
            Standard_Deviation = sd(pricediff))%>%
  mutate(Coefficient_of_Variation = Standard_Deviation/Price_Difference)
finaldata

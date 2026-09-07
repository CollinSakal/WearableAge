# Run GAM and obtain WearableAge and WearableAgeGap (stage 2)

# Libraries
library(mgcv)
library(tidyverse)

# Load CatBoost predictions and age
df <- read_csv('output/df-risk-scores.csv')

# Load the GAM
gam <- readRDS('models/gam.RDS')

# Make predictions and add to df
wearableage <- as.numeric(predict(gam, newdata = df, type = 'response'))

df <- df %>% mutate(
  wearableage = wearableage,
  wearableagegap = wearableage-age
)

# Save
write_csv(df, 'output/df-out.csv')
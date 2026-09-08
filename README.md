# **A wearable-derived aging clock enables out-of-clinic prediction of mortality and cardiometabolic risk** 

This repository includes code to derive WearableAge and WearableAgeGap from the study *A wearable-derived aging clock enables out-of-clinic prediction of mortality and cardiometabolic risk* by Sakal et al. (2026, under review). Synthetic data is provided in ```/data``` facilitate testing the code. 

**Authors:** Collin Sakal** [1], Tong Chen [2], Wenxin Xu [2], Wei Zhang [3], Xinyue Li** [2]

**Co-corresponding authors

**Affiliations:**

[1] City University of Hong Kong (Dongguan), Songshan Lake High-Tech Industrial Development Zone, Dongguan, China

[2] Department of Data Science, College of Computing, City University of Hong Kong, Hong Kong SAR, China.

### Requirements

- ```Python 3.14+```
  - ```Polars 1.44.0+```
  - ```CatBoost 1.2.9+```

- ```R 4.5.1+```
  - ```mgcv 1.9.3+```
  - ```tidyverse 2.0.0+```

### Deriving WearableAge and WearableAgeGap

WearableAge was developed using a two-stage second generation aging clock approach. The first stage uses a Cox-loss CatBoost model to obtain all-cause mortality risk predictions based on features collectable on wearable health trackers. In the second stage, a generalized additive model (GAM) is used to predict chronological age as a function of the CatBoost risk predictions. The GAM predictions are WearableAge (risk equivalent age) and the difference between WearableAge and chronological age is WearableAgeGap (aging clock). The procedure for deriving WearableAge and WearableAgeGap is described below.

**(1) Obtain data with the necessary features for the CatBoost model**

The table below details the features required to obtain predictions using CatBoost. Note that the CatBoost model will run despite feature missingness, though predictive performance may suffer. 

| Feature                                | Variable Name      | Characteristics^                                             |
| -------------------------------------- | ------------------ | ------------------------------------------------------------ |
| Age                                    | age                | *Numeric*. Chronological age in years                        |
| Body mass index                        | bmi                | *Numeric*. Body mass index                                   |
| Sex                                    | sex                | *Categorical*. Biological sex {Male, Female}                 |
| Education                              | education          | *Categorical*. Highest level of education {A levels, CSEs, NVG NHD HNC, O levels, Other not listed, Other professional, University}. Mapping from UK-based education may be required. |
| Smoker                                 | smoker             | *Categorical*. Cigarette smoking status {Current, Former, Never} |
| Drinker                                | drinker            | *Categorical*. Alcohol consumption habits {Drinker, Non-drinker} |
| Shift worker                           | shift_work         | *Categorical*. Works shift schedules outside of a standard 9am - 5pm routine {Yes, No} |
| Night shift worker                     | night_shift        | *Categorical*. Works night shifts {Yes, No}                  |
| Fruit and vegetable servings           | fruit_veg_servings | *Numeric*. Daily fruit and vegetable servings. One serving of vegetables is defined as three heaped tablespoons cooked or uncooked, and one piece of fruit counts as one portion, with fresh and dried fruit counted equally. |
| Total acceleration (physical activity) | acc_tot_any_avg    | *Numeric*. Sum of minute-level epoch acceleration recordings from all wake-state epochs averaged across full days of data. |
| Minutes per day of MVPA                | min_day_mvp_avg    | *Numeric*. Minutes per day of MVPA defined using a 100mg acceleration threshold from minute-level wake-state epochs averaged across full days of data. |
| Minutes per day of VPA                 | min_day_vpa_avg    | *Numeric*. Minutes per day of VPA defined using a 400mg acceleration threshold from minute-level wake-state epochs averaged across full days of data. |
| Non-sedentary (active) bout duration   | bdr_day_act_avg    | *Numeric*. Longest daily bout of non-sedentary (active-state) activity defined using a 40mg acceleration threshold from minute-level wake-state epochs averaged across full days of data. |
| MVPA bout duration                     | bdr_day_mvp_avg    | *Numeric*. Longest daily bout of MVPA defined using a 100mg acceleration threshold from minute-level wake-state epochs averaged across full days of data. |
| VPA bout duration                      | bdr_day_vpa_avg    | *Numeric*. Longest daily bout of VPA defined using a 400mg acceleration threshold from minute-level wake-state epochs averaged across full days of data. |
| Self-reported CVD                      | cardio_selfrep     | *Categorical*. {Yes, No}                                     |
| Self-reported cancer                   | cancer_selfrep     | *Categorical*. {Yes, No}                                     |
| Self-reported diabetes                 | diabet_selfrep     | *Categorical*. {Yes, No}                                     |
| Self-reported hypertension             | hypert_selfrep     | *Categorical*. {Yes, No}                                     |
| Total sleep window                     | slp_dur_avg        | *Numeric*. Accelerometer-derived sleep duration (hours), framed as "total sleep window" due to likely overestimation from misclassifying wake-state time-in-bed as sleeping. Averaged across nights of sleep data. |
| Sleep efficiency                       | slp_eff_avg        | *Numeric*. Proportion of time estimated to be asleep during the total sleep window averaged across nights of sleep data. |
| Sleep onset                            | slp_ons_avg        | *Numeric*. Sleep onset encoded as hours from midnight and averaged across nights of sleep data. |
| Sleep offset                           | slp_off_avg        | *Numeric*. Sleep offset encoded as hours from midnight and averaged across nights of sleep data. |
| Total sleep window regularity          | slp_dur_std        | *Numeric*. SD of total sleep window across nights of sleep data. |
| Sleep efficiency regularity            | slp_eff_std        | *Numeric*. SD of sleep efficiency across nights of sleep data. |
| Sleep onset regularity                 | slp_ons_std        | *Numeric*. SD of sleep onset across nights of sleep data.    |
| Sleep offset regularity                | slp_off_std        | *Numeric*. SD of sleep offset across nights of sleep data.   |
| Difficulty getting up from sleep       | getting_up         | *Categorical*. {Fairly easy, Not at all easy, Not very easy, Very easy} |
| Frequency dozing off                   | dozing_off         | *Categorical*. {All the time, Never, Often, Sometimes}       |

**^** A "full day" of acceleration data is defined as wake-state accelerometer data occurring between two nights of valid sleep recordings, or in other words, wake-state activity data occurring within one full sleep-wake-sleep cycle. 

**(2) Obtain all-cause mortality predictions using the pre-trained CatBoost model.**

Replace the synthetic data frame in ```/data```, and run ```run_stage_1.py```, which will load the pre-trained CatBoost model and output all-cause mortality risk predictions. The CatBoost risk predictions will be saved in ```/output```.

**(3) Obtain WearableAge and WearableAgeGap from GAM predictions**

Run ```run_stage_2.R``` which will use the pre-trained GAM model to obtain chronological age predictions and calculate WearableAge and WearableAgeGap. A data frame will be saved in ```/output```.
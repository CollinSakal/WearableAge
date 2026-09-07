# Imports
import polars as pl

# Creating synthetic sample data
df = pl.DataFrame([
    pl.Series('id', [1,2,3]),
    pl.Series('age', [55, 65, 70]),
    pl.Series('bmi', [23, 26, 29]),
    pl.Series('sex', ['Male', 'Female', 'Male']),
    pl.Series('education', ['University', 'University', 'University']),
    pl.Series('smoker', ['Never', 'Former', 'Current']),
    pl.Series('drinker', ['Drinker', 'Drinker', 'Drinker']),
    pl.Series('shift_work', ['No', 'No', 'No']),
    pl.Series('night_shift', ['No', 'No', 'No']),
    pl.Series('fruit_veg_servings', [3, 4, 5]),
    pl.Series('acc_tot_any_avg', [43000, 35000, 28000]),
    pl.Series('min_day_mvp_avg', [120, 85, 55]),
    pl.Series('min_day_vpa_avg', [3, 2, 1]),
    pl.Series('bdr_day_act_avg', [50, 30, 20]),
    pl.Series('bdr_day_mvp_avg', [17, 10, 3]),
    pl.Series('bdr_day_vpa_avg', [0.5, 0.5, 0.5]),
    pl.Series('cardio_selfrep', ['No', 'No', 'No']),
    pl.Series('cancer_selfrep', ['No', 'No', 'No']),
    pl.Series('diabet_selfrep', ['No', 'No', 'No']),
    pl.Series('hypert_selfrep', ['No', 'No', 'No']),
    pl.Series('slp_dur_avg', [7, 8, 9]),
    pl.Series('slp_eff_avg', [0.9, 0.85, 0.92]),
    pl.Series('slp_off_avg', [5, 6, 7]),
    pl.Series('slp_ons_avg', [10, 10, 10]),
    pl.Series('slp_dur_std', [1, 1, 1]),
    pl.Series('slp_eff_std', [0.01, 0.01, 0.01]),
    pl.Series('slp_ons_std', [0.5, 0.7, 0.9]),
    pl.Series('slp_off_std', [0.5, 0.5, 0.5]),
    pl.Series('getting_up', ['Very easy', 'Very easy', 'Very easy']),
    pl.Series('dozing_off', ['Never', 'Never', 'Never'])
])

df.write_csv('data/df.csv')
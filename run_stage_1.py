# Run CatBoost model to get all-cause mortality risk scores (stage 1)

# Imports
import polars as pl
from catboost import CatBoostRegressor, Pool

# Initializing stuff
feature_cols = [
    'age', 'bmi', 'sex', 'education', 'smoker', 'drinker', 'shift_work', 'night_shift', 'fruit_veg_servings',
    'acc_tot_any_avg', 'min_day_mvp_avg', 'min_day_vpa_avg',
    'bdr_day_act_avg', 'bdr_day_mvp_avg', 'bdr_day_vpa_avg',
    'cardio_selfrep', 'cancer_selfrep', 'diabet_selfrep', 'hypert_selfrep',
    'slp_dur_avg', 'slp_eff_avg', 'slp_ons_avg', 'slp_off_avg',
    'slp_dur_std', 'slp_eff_std', 'slp_ons_std', 'slp_off_std',
    'getting_up', 'dozing_off'
]

cat_features = [
    'sex', 'education', 'smoker', 'drinker', 'diabet_selfrep', 'hypert_selfrep', 'cardio_selfrep',
    'cancer_selfrep', 'getting_up', 'dozing_off', 'night_shift', 'shift_work'
]

# Load synthetic data set
df = pl.read_csv('data/df.csv') # Should also include 'id' (individual identifier)
X = df.select(feature_cols)

# Load the model
model = CatBoostRegressor()
model.load_model('models/catboost.cbm', format='cbm')

# Make predictions
pool = Pool(data=X, cat_features=cat_features, feature_names=X.columns)

preds = model.predict(pool)

# Save for input into GAM model
df_out = pl.DataFrame([
    df.get_column('id'),
    df.get_column('age'),
    pl.Series('catboost_preds', preds),
])

df_out.write_csv('output/df-risk-scores.csv')
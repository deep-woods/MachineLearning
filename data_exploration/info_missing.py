def info_missing(df):
  features_w_na = []
  all_cols = df.columns
  n_columns = len(all_cols)
  for i in range(0, n_columns):
    if len(df[all_cols[i]].dropna()) < len(df):
      features_w_na.append(all_cols[i])

  if( len(features_w_na) == 0):
    print("This DataFrame has no missing data.")

  else: 
    print('<Features with missing values>')
    print(f'Count: %d features' %len(features_w_na))
    print()
    print(' #   column       na count   na ratio')
    print('---  ------       --------   --------')

    n_features = len(features_w_na)
    for i in range(0, n_features):
      na_name = features_w_na[i]
      na_index = list(all_cols).index(na_name)
      na_count = df[na_name].isna().sum()
      na_ratio = round(na_count / len(df), 3)
      print("{:<4} {:<15} {:5} {:10}".format(na_index, na_name, na_count, na_ratio))
      return na_name, na_index, na_count, na_ratio

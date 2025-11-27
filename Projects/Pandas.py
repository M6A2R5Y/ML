print("Setup complete.")

import pandas as pd
iowa_file_path = '../input/home/data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)
# step_1.check()

# step_1.hint()
# step_1.check()
# step_1.hint()
# step_1.solution()
avg_lot_size = home_data['LotArea'].mean().round()
newest_home_age = home_data['YrSold'].max() - home_data['YearBuilt'].min()

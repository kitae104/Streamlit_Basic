# 데이터 읽어오기 및 전처리

# Strip any leading or trailing whitespace from column names
data.columns = data.columns.str.strip()

# Pivot the data to have one row per date and columns for each station's boarding and alighting
pivot_data = data.pivot_table(index='통행일자', 
                              columns='역명', 
                              values=['승차인원', '하차인원'], 
                              aggfunc='sum')

# Flatten the column index
pivot_data.columns = [f'{station}_{action}' for action, station in pivot_data.columns]

# Reset index to make '통행일자' a column again
pivot_data.reset_index(inplace=True)

# Save the transformed data to a new CSV file
output_file_path = '/mnt/data/인천교통공사_일별_이용현황.csv'
pivot_data.to_csv(output_file_path, index=False, encoding='utf-8-sig')

import ace_tools as tools; tools.display_dataframe_to_user(name="Transformed Data", dataframe=pivot_data)

output_file_path
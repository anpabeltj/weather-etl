import pandas as pd
import extract as e

def transform(data, city_name):
    daily_data = data["daily"]
    df = pd.DataFrame(daily_data)
    df.columns = ['date', 'temp_max', 'temp_min', 'precipitation']
    df['city'] = city_name
    return df

if __name__ == "__main__":
    data = e.extract_city("Jakarta")
    df = transform(data, "Jakarta")
    print(df)
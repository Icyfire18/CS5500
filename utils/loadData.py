import pandas as pd
import sqlite3

class DataLoad:
    """
        Class Used to Process the Data Contain the Common functions
    """
    def __init__(self):
        pass
         
    def read_data(self, file_name, sheet_name, col_range, columns):
        """
            Read the Data from Excel file from a specific sheet & update column Names.
        """
        temp_df = pd.read_excel(file_name, sheet_name=sheet_name, skiprows=5, header=0, usecols=range(col_range))
        temp_df.columns = columns
        return temp_df

    def df_to_sqlite(self, df, db_name, table_name):
        """
            Used to write the Dataframe to the Specific Database and Table.
        """
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        df.to_sql(table_name, conn, index=False, if_exists="replace")
        conn.close()

    def transform_row(self, row):
        """
            Used to Transform the Row based on specific values.
        """
        current_year = pd.to_datetime('now').year

        if row["start_date"] == "Not Available":
            row["date"] = row["delivery_date"]
        else:
            row["date"] = row["start_date"]

        if row["quantity_units"] == "ccf (hundred cubic feet)":
            row["common_usage_units"] = row['quantity'] * 100000
        elif row["quantity_units"] == "kWh (thousand Watt-hours)":
            row["common_usage_units"] = row['quantity'] * 3413
        elif row["quantity_units"] == "Gallons (US)":
            row["common_usage_units"] = row['quantity'] * 83000

        row["units"] = "Btu(in Millions)"
        row["common_usage_units"] = row["common_usage_units"] / 1000000;


        if row["property_name"] == "Portland Museum of Art":
            row["usage_per_sq_feet"] = (row["common_usage_units"] * 1000) / 74500
            row["age"] = current_year - 1982
        elif row["property_name"] == "Charles Shipman Payson Building":
            row["usage_per_sq_feet"] = (row["common_usage_units"] * 1000) / 62500
            row["age"] = current_year - 1982
        elif row["property_name"] == "Clapp House":
            row["usage_per_sq_feet"] = (row["common_usage_units"] * 1000) / 2000
            row["age"] = current_year - 1982
        elif row["property_name"] == "Winslow Homer Studio":
            row["usage_per_sq_feet"] = (row["common_usage_units"] * 1000) / 1350
            row["age"] = current_year - 1982
        elif row["property_name"] == "142 Free St":
            row["usage_per_sq_feet"] = (row["common_usage_units"] * 1000) / 13000
            row["age"] = current_year - 1830

        if row["meter_id"] == 6329063:
            row["property_name"] = row["property_name"] + "-Fire Meter"
        else:
            row["property_name"] = row["property_name"]
            
        row["date"] = str(row["date"])
        return row

def main():
    load_file = "data/pma.xlsx"
    weather_file = "data/weather.xlsx"
    db_name = "db.sqlite3"

    meta_data_sheet = "Properties"
    meta_table_name = "pma_museum"

    data_sheet = "Meter Entries"
    data_table_name = "pma_usage"

    weather_data_sheet = "weather"
    weather_table_name = "pma_weather"

    meta_data_col = ["property_name", "property_id", "street_address_1", "street_address_2", "city", "state", "other_state", "postal_code", "country", "year_built", "type", "construction_status", "gross_floor_area", "gfa_units", "occupancy", "number_of_buildings", "no_of_building"]
    data_col = ["property_name", "property_id", "meter_id", "meter_name", "meter_type", "meter_consumption_id", "start_date", "end_date", 'delivery_date', "quantity", "quantity_units", "cost", "estimation", "demand", "demand_cost", "last_modified_date", "last_modified_by"]
    weather_data_col = ["date", "temperature", "location", "elevation", "latitude", "longitude"]

    loader = DataLoad()

    museum_df = loader.read_data(load_file, meta_data_sheet, 17, meta_data_col)
    loader.df_to_sqlite(museum_df, db_name, meta_table_name)

    usage_df = loader.read_data(load_file, data_sheet, 17, data_col)
    df_transformed = usage_df.assign(**usage_df.apply(loader.transform_row, axis=1))
    df_transformed["u_id"] = df_transformed.reset_index().index + 1
    df_transformed = df_transformed[["u_id","property_name", "property_id", "meter_id", "meter_name", "meter_type", "meter_consumption_id", "start_date", "end_date", 'delivery_date', "quantity", "quantity_units", "cost", "estimation", "demand", "demand_cost", "last_modified_date", "last_modified_by","age", "common_usage_units", "date","units", "usage_per_sq_feet"]]
    loader.df_to_sqlite(df_transformed, db_name, data_table_name)

    weather_df = loader.read_data(weather_file, weather_data_sheet, 6, weather_data_col)
    loader.df_to_sqlite(weather_df, db_name, weather_table_name)



if __name__ == "__main__":
    main()
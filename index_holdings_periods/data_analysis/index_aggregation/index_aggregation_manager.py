from . import index_aggregation_helpers


def run(df, list_of_periods):
    df_aggregated = index_aggregation_helpers.aggregate_index_from_constituents(df)
    df_cleaned = index_aggregation_helpers.remove_missing_data(
        df_aggregated, list_of_periods, False
    )

    df_cleaned_to_same_dt = index_aggregation_helpers.remove_missing_data(
        df_aggregated, list_of_periods, True
    )

    return df_cleaned, df_cleaned_to_same_dt

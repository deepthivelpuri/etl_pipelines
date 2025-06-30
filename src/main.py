from extract import extract_data
from load import load_to_sql
from transform  import transform_data

from transform2 import transformed_data


if __name__=="__main__":
    df=extract_data()

    df_flat, df_milestones, df_members=transform_data(df)
    df_flat2=transformed_data(df)

    load_to_sql(df_flat, df_milestones, df_members,df_flat2)


    df_flat2=transformed_data(df)
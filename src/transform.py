import pandas as pd

def transform_data(df):
    # Flatten nested fields
    df_flat = pd.json_normalize(
        df.to_dict(orient='records'),
        sep='_'
    )

    
    if 'milestones' in df.columns:
        df_flat['milestones'] = df['milestones'].apply(lambda x: x if isinstance(x, list) else [])

    # Explode milestones to multiple rows (optional)
    df_milestones = df[['project_id', 'milestones']].explode('milestones')
    df_milestones = pd.concat([
        df_milestones.drop(['milestones'], axis=1),
        df_milestones['milestones'].apply(pd.Series)
    ], axis=1)

    # Explode team members to another table (optional)
    df_members = df[['project_id', 'team']].copy()
    df_members['members'] = df_members['team'].apply(lambda x: x.get('members', []))
    df_members = df_members[['project_id', 'members']].explode('members')
    df_members = pd.concat([
        df_members.drop(['members'], axis=1),
        df_members['members'].apply(pd.Series)
    ], axis=1)

    return df_flat, df_milestones, df_members

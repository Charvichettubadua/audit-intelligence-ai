def calculate_risk(df):
    # Auto-mapping columns for flexibility
    amt_col = 'Amount' if 'Amount' in df.columns else (df.columns[0] if len(df.columns)>0 else None)
    
    # Logic
    df['Risk_Score'] = 0
    if amt_col:
        df['Risk_Score'] += df[amt_col].apply(lambda x: 40 if x > 10000 else 0)
    
    # Random flags for simulation if other columns missing
    if 'Class' in df.columns:
        df['Risk_Score'] += df['Class'].apply(lambda x: 50 if x == 1 else 0)
    
    def classify(s):
        if s >= 70: return 'High'
        elif s >= 40: return 'Medium'
        return 'Low'
        
    df['Risk_Level'] = df['Risk_Score'].apply(classify)
    return df
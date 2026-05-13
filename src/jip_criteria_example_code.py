def jip_criteria(row):
    """
    Simplified criteria to discern the joint involvement patterns
    
    Here clusters are labeled with an integer, where:
    0 = 'JIP-Foot'
    1 = 'JIP-Oligo'
    2 = 'JIP-Hand'
    3 = 'JIP-Poly'
    """
    if row['total_minus_28'] < 6: 
        if row['hand_das28_count'] < 9:
            # Low hand count and high feet count maps to Foot cluster
            return 1 if row['foot_das44_count'] < 6 else 0
        else: 
            # High hand count maps to Hand cluster
            return 1 if row['total_minus_foot'] < 9 else 2

    # --- BRANCH 2: High Variation (total_minus_28 > 5.0) ---
    else:
        if row['total_minus_28'] < 15:
            # limited joint involvement beside foot maps to Foot cluster
            return 0 if row['total_minus_foot'] < 26 else 3
        else: 
            # Very high variation maps to Poly cluster
            return 3 if row['total_minus_foot'] > 5 else 0

"""
Run like this on a pandas dataframe:

df = pd.read_csv('example_patient_table.csv')
df['pred_cluster'] = df.apply(lambda x : jip_criteria(x), axis =1)

"""
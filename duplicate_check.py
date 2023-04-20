def duplicate_check(df,var_name):
    check = df[var_name].value_counts()
    x = check.shape
    if x[0] < 5:
        print("There might be duplicate records. Check the rows listed below.")
        # Let's check where the duplicate is
        unique_id = df[var_name].drop_duplicates()
        for i in unique_id:
            if check[i] > 1:
                print(var_name,":",i)
                row_num = df[df[var_name]==i]
                print("Found in rows:",row_num.index.tolist())
                l = row_num.index.tolist()
               
    else:
        print("There are most likely no duplicate records.")

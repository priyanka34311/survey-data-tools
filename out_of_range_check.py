def out_of_range_check(df,varname,values):

    g = df[varname].value_counts()
    g_idx = g.index
    g_idx = g_idx.tolist()

    for k in g_idx:
        if k in values:
            pass
        else:
            print(k)
            row_id = df[df[varname]==k]
            print("Found in rows:",row_id.index.tolist())

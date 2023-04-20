# Recode string values to numerical values
# NOTE: Advisable to begin with 0 to aid in further analysis (i.e.,regression)
# EXAMPLE: recode_str_to_num(df,"Gender")

def recode_str_to_num(df,varname):
    l = list(df[varname])
    d = dict([(y,x) for x,y in enumerate(sorted(set(l)))])
    
    copy_column = df[varname]
    col_num = df.columns.get_loc(varname)
# Let's insert the copied column to the immediate right of the original column
    varname_num = varname+'_num'
    df.insert(col_num+1,varname_num,copy_column,True)
    df_new=df.replace({"Gender_num":d})
    return df_new

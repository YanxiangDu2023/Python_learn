import pandas as pd
df = pd.read_csv(r"/Users/amandadu/Desktop/coding/python/pandas/countries of the world.csv",header=None,names=["Country"])

# header=None:

# This parameter specifies that the first row of the file is not a header. That is, the CSV file does not contain column names, and all rows are considered data rows.
# names=["Country"]:
#
# Specifies the column name for the DataFrame as "Country". Since header=None, column names need to be provided manually. This assumes the CSV file has only one column of data, named "Country".


# print(df.head())


df = pd.read_csv(r"/Users/amandadu/Desktop/coding/python/pandas/countries of the world.txt",sep="\t")

# sep="\t" 是一个固定用法，用于告诉 Pandas 使用制表符作为分隔符来读取文件。这种用法在处理 TSV（制表符分隔值）文件时非常常见。只要记住在读取 TSV 文件时使用 sep="\t" 就可以了。这样 Pandas 就能正确地解析文件内容并生成 DataFrame。

# print(df.head())

df = pd.read_table(r"/Users/amandadu/Desktop/coding/python/pandas/countries of the world.csv",sep = ",")
# 概括：
#虽然这两个函数通常可以实现相同的结果，但 pd.read_csv 更专门用于 CSV 文件，而 pd.read_table 是更通用的函数，适用于各种分隔文件。在处理 CSV 文件时，使用 pd.read_csv 可以实现简单性和可读性，
# 使用 pd.read_table 可以灵活地处理其他分隔符。

df2 = pd.read_excel(r"/Users/amandadu/Desktop/coding/python/pandas/world_population_excel_workbook.xlsx",sheet_name = "Sheet1")
# print(df.head())

pd.set_option("display.max.rows",235)
# 设置 Pandas 显示选项，使得最大显示行数为 235。

maxrow = pd.get_option("display.max.rows",235)


# display.max.columns: 设置最大显示列数。
# display.max.colwidth: 设置每列的最大字符宽度。
# display.precision: 设置显示浮点数的精度。


print(maxrow)
print(df)

pd.set_option("display.max.columns",235)
# 获取当前的设置值，以确认是否成功更改。

maxcolumns = pd.get_option("display.max.columns",40)
print(maxcolumns)

df2.info()

df2.tail(10) # last 10

rank = df2["Rank"]
print(rank)

loc = df2.loc[224] #第224行的内容
print(loc)





import pandas as pd

dataProduct = 'INSTALLATION_PROJECTS'

filter_values = ['y','Y']
file_name = 'mapping.py'

class generateMapping :

    def read_excel_data(self):
        df = pd.read_excel('C:/Users/nlarc/AppData/Local/Programs/Python/Python310/Scripts/GenerateMapping/MappingReference.xlsx')
        return df

    def append_import_lines(self):
        f= open(file_name,"w+")
        f.write("from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, DoubleType, BooleanType,TimestampType \r\n")
        f.close()

    def append_all_column_names(self,df):
        f= open(file_name,"a")
        f.write(f'{dataProduct}_NAMES = ' +  "{ \n")

        for i in df.index:
            cl = df['ColumnName'][i]
            f.write("\t" + f'\'{cl}\':\'{cl}\'')
            if i+1 == len(df):
                f.write("\n } \r\n")
            else:
                f.write(", \n")

    def append_sdp_schema_content(self,df):

        df_sdp = df[df['InSource'].isin(filter_values)].reset_index(drop=True)

        f= open(file_name,"a")
        

        f.write(f'SDP_{dataProduct}_SCHEMA = ' +  "StructType([ \n")

        for i in df_sdp.index:
            cl = df_sdp['ColumnName'][i]
            ct = df_sdp['ColumnType'][i]
            f.write('\t \t \t \t StructField(' +  f'{dataProduct}_NAMES' + f'[\'{cl}\'],{ct}(), True)')
            if i+1 == len(df_sdp):
                f.write("]) \r\n")
            else:
                f.write(", \n")

        f.close()

    def append_bronze_schema_content(self,df):

        df_bronze = df[df['InBronze'].isin(filter_values)].reset_index(drop=True)

        f= open(file_name,"a")

        f.write(f'BDP_{dataProduct}_BRONZE_SCHEMA = ' +  "StructType([ \n")

        for i in df_bronze.index:
            cl = df_bronze['ColumnName'][i]
            ct = df_bronze['ColumnType'][i]
            f.write('\t \t \t \t StructField(' +  f'{dataProduct}_NAMES' + f'[\'{cl}\'],{ct}(), True)')

            if i+1 == len(df_bronze):
                f.write("]) \r\n")
            else:
                f.write(", \n")

        f.close()

    def append_silver_schema_content(self,df):

        df_bronze = df[df['InSilver'].isin(filter_values)].reset_index(drop=True)

        f= open(file_name,"a")

        f.write(f'BDP_{dataProduct}_SILVER_SCHEMA = ' +  "StructType([ \n")

        for i in df_bronze.index:
            cl = df_bronze['ColumnName'][i]
            ct = df_bronze['ColumnType'][i]
            f.write('\t \t \t \t StructField(' +  f'{dataProduct}_NAMES' + f'[\'{cl}\'],{ct}(), True)')

            if i+1 == len(df_bronze):
                f.write("]) \r\n")
            else:
                f.write(", \n")

        f.close()

    def append_gold_schema_content(self,df):

        df_bronze = df[df['InGold'].isin(filter_values)].reset_index(drop=True)

        f= open(file_name,"a")

        f.write(f'BDP_{dataProduct}_GOLD_SCHEMA = ' +  "StructType([ \n")

        for i in df_bronze.index:
            cl = df_bronze['ColumnName'][i]
            ct = df_bronze['ColumnType'][i]
            f.write('\t \t \t \t StructField(' +  f'{dataProduct}_NAMES' + f'[\'{cl}\'],{ct}(), True)')

            if i+1 == len(df_bronze):
                f.write("]) \r\n")
            else:
                f.write(", \n")

        f.close()

    def create_mapping_file(self):
        df = self.read_excel_data()
        self.append_import_lines()
        self.append_all_column_names(df)
        self.append_sdp_schema_content(df)
        self.append_bronze_schema_content(df)
        self.append_silver_schema_content(df)
        self.append_gold_schema_content(df)

    
mp = generateMapping()
mp.create_mapping_file()




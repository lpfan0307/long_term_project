import pandas as pd
from config import config
class ComData():
    def __init__(self, sy_file, dz_file,sep='\t'):
        print('sy, dz data init...')
        self.sy_df = pd.read_csv(sy_file, sep=sep, header='infer',encoding='gbk') 
        self.dz_df = pd.read_csv(dz_file, sep=sep, header='infer',encoding='gbk') 

    def assign_columns(self, columns):
        self.sy_df.columns = columns
        self.dz_df.columns = columns

    def merge_sy_dz_data(self, key):
        self.df_total = self.sy_df.merge(self.dz_df,how='outer',on=key)
    def to_csv(self, filename):
        self.df_total.to_csv(filename, index=False)
    
    def get_unit_brand(self, unit_brand_file):
        unit_brand_df = pd.read_csv(unit_brand_file,sep='\t',header='infer',encoding='gbk')
        unit_brand_df.columns = ['unitid','brand']  
        unit_brand_df = unit_brand_df[unit_brand_df.brand!="%2D"] 
        unitid_brand_dic =  dict(zip(unit_brand_df['unitid'], unit_brand_df['brand'])) 
        
        self.df_total['brand'] = self.df_total['unitid'].apply(lambda x:unitid_brand_dic.get(int(x), '1'))
        
    
    def parse_columns(self, info_column, sep, names):
        idx = 0
        for  name in names:
            self.df_total[name] = self.df_total[info_column].apply(lambda x:x.split(sep)[idx]) 
            idx += 1

if __name__ == "__main__":
    # execute only if run as a script
    sy_file = '/Users/fanlinpeng/Desktop/rele_data/sy.csv'
    dz_file = '/Users/fanlinpeng/Desktop/rele_data/dz.csv'
    comdData = ComData(sy_file,dz_file,'\t')
    #comdData.assign_columns(['key','charge','acp','roiq'])
    #comdData.assign_columns(['match_type','unitid','charge','clk','trans','trans_ratio','avg_obid','cpa'])
    comdData.assign_columns(['brand','unitid', 'userid', 'price', 'clk', 'trans_num', 'trans_ratio', 'avg_obid', 'cpa'])
    #comdData.assign_columns(['userid','brand', 'date', 'price'])
    #comdData.assign_columns(['event_day','unitid','brand', 'show' ,'clk' ,'price', 'ctr', 'acp'])

    #unit_brand_file = '/Users/fanlinpeng/Desktop/rele_data/3485497.csv'

    comdData.merge_sy_dz_data('brand')

    #comdData.parse_columns('key','_', ['unitid','hour']) 
    #comdData.df_total['unitid'] = comdData.df_total['key'].apply(lambda x:x.split('_')[0])
    #comdData.df_total['hour'] = comdData.df_total['key'].apply(lambda x:x.split('_')[1])
    
    #comdData.get_unit_brand(unit_brand_file) 
  
    comdData.df_total.to_csv('/Users/fanlinpeng/Desktop/rele_data/diff.csv',encoding='gbk', index=False)

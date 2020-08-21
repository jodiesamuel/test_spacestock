#!/usr/bin/env python
# coding: utf-8

# complex

import pandas as pd
import numpy as np
import json
from sqlalchemy import create_engine

df = open('/home/jodie/Downloads/test/de_task (1)/complex.json')
data = df.read()

df = data.replace('ObjectId(','').\
replace('NumberLong(','').\
replace(')','').\
replace('\n','').\
replace('/* ', '')

i = 0
while i < 10:
    df = df.replace(str(i)+' */','')
    i += 1

i = 0
while i < 10:
    df = df.replace(str(i)+'{','{')
    df = df.replace('}{','}\n{')
    i += 1

complex = pd.read_json(df,lines=True)
complex = complex.fillna('')

complex['unit_rent_total']=np.where(complex['unit_rent_total']=='', 0,0)
complex['unit_sell_total']=np.where(complex['unit_sell_total']=='', 0,0)
complex['status']=np.where(complex['status']=='', 1,0)
complex['service_types'] = [','.join(map(str, l)) for l in complex['service_types']]
complex['premium_listing_available']=np.where(complex['premium_listing_available']=='', 0,0)

complex['_id'] = complex['_id'].astype('string') 
complex['category'] = complex['category'].astype('string') 
complex['name'] = complex['name'].astype('string') 
complex['developer_name'] = complex['developer_name'].astype('string') 
complex['address_street'] = complex['address_street'].astype('string') 
complex['address_city'] = complex['address_city'].astype('string') 
complex['address_subdistrict'] = complex['address_subdistrict'].astype('string') 
complex['address_urban'] = complex['address_urban'].astype('string') 
complex['address_province'] = complex['address_province'].astype('string') 
complex['address_zip'] = complex['address_zip'].astype('int64') 
complex['address_coordinate'] = complex['address_coordinate'].astype('string') 
complex['create_by_uid'] = complex['create_by_uid'].astype('string') 
complex['facilities'] = complex['facilities'].astype('string') 
complex['images'] = complex['images'].astype('string') 
complex['id'] = complex['id'].astype('string') 
complex['tower_total'] = complex['tower_total'].astype('int64') 
complex['branches'] = complex['branches'].astype('string') 
complex['unit_rent_total'] = complex['unit_rent_total'].astype('int64') 
complex['unit_sell_total'] = complex['unit_sell_total'].astype('int64') 
complex['developer_legal_name'] = complex['developer_legal_name'].astype('string') 
complex['land_size'] = complex['land_size'].astype('int64') 
complex['last_update_at'] = complex['last_update_at'].astype('datetime64[ns]') 
complex['last_update_by_uid'] = complex['last_update_by_uid'].astype('string') 
complex['address_country'] = complex['address_country'].astype('string') 
complex['surrounding_area'] = complex['surrounding_area'].astype('string') 
complex['address_area'] = complex['address_area'].astype('string') 
complex['create_at'] = complex['create_at'].astype('string') 
complex['status'] = complex['status'].astype('int64') 
complex['code'] = complex['code'].astype('string') 
complex['service_types'] = complex['service_types'].astype('string') 
complex['premium_listing_available'] = complex['premium_listing_available'].astype('int64') 

complex['images'] = complex['images'].astype(str).str.replace("'",'"', regex=False)
complex['facilities'] = complex['facilities'].astype(str).str.replace("'",'"', regex=False)
complex['images'] = complex['images'].astype(str).str.replace("None",'"None"', regex=False)
complex['images'] = complex['images'].astype(str).str.replace('Children"s','childrens', regex=False)

engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')
complex.to_sql('complex',engine, if_exists='replace', method=None)

# tower

df = open('/home/jodie/Downloads/test/de_task (1)/tower.json')
data = df.read()

df=data.replace('ObjectId(','').\
replace('NumberLong(','').\
replace(')','').\
replace('\n','').\
replace('/* ', '')

i = 0
while i < 10:
    df = df.replace(str(i)+' */','')
    i += 1

i = 0
while i < 10:
    df = df.replace(str(i)+'{','{')
    df = df.replace('}{','}\n{')
    i += 1

tower = pd.read_json(df,lines=True)
tower = tower.fillna('')

tower['unit_rent_total']=np.where(tower['unit_rent_total']=='', 0,0)
tower['unit_sell_total']=np.where(tower['unit_sell_total']=='', 0,0)
tower['service_charge']=np.where(tower['service_charge']=='', 0,0)
tower['average_floor_plate']=np.where(tower['average_floor_plate']=='', 0,0)
tower['ceiling_height']=np.where(tower['ceiling_height']=='', 0,0)
tower['commercial_terms']=np.where(tower['commercial_terms']=='', 0,0)
tower['land_size']=np.where(tower['land_size']=='', 0,0)
tower['max_zone_per_floor']=np.where(tower['max_zone_per_floor']=='', 0,0)
tower['office_hours']=np.where(tower['office_hours']=='', 0,0)
tower['power_line']=np.where(tower['power_line']=='', 0,0)
tower['semi_gross_area']=np.where(tower['semi_gross_area']=='', 0,0)
tower['sinking_fund']=np.where(tower['sinking_fund']=='', 0,0)
tower['create_at']=np.where(tower['create_at']=='', 0,0)
tower['status']=np.where(tower['status']=='', 1,0)
tower['include_scsf']=np.where(tower['include_scsf']=='', 0,0)
tower['total_unit_primary']=np.where(tower['total_unit_primary']=='', 0,0)

tower['_id'] = tower['_id'].astype('string') 
tower['complex_id'] = tower['complex_id'].astype('string') 
tower['create_by_id'] = tower['create_by_id'].astype('string') 
tower['last_update_at'] = tower['last_update_at'].astype('int64') 
tower['category'] = tower['category'].astype('string') 
tower['name'] = tower['name'].astype('string') 
tower['year_completion'] = tower['year_completion'].astype('string') 
tower['year_renovation'] = tower['year_renovation'].astype('string') 
tower['floor_count'] = tower['floor_count'].astype('int64') 
tower['description'] = tower['description'].astype('string') 
tower['parking'] = [','.join(map(str, l)) for l in tower['parking']]
tower['parking'] = tower['parking'].astype('string')
tower['lift'] = [','.join(map(str, l)) for l in tower['lift']]
tower['lift'] = tower['lift'].astype('string') 
tower['internet'] = tower['internet'].astype('string') 
tower['images'] = tower['images'].astype('string') 
tower['unit_total'] = tower['unit_total'].astype('int64') 
tower['id'] = tower['id'].astype('string') 
tower['branches'] = tower['branches'].astype('string') 
tower['unit_rent_total'] = tower['unit_rent_total'].astype('int64') 
tower['unit_sell_total'] = tower['unit_sell_total'].astype('int64') 
tower['architect'] = tower['architect'].astype('string') 
tower['certificate'] = tower['certificate'].astype('string') 
tower['contractor'] = tower['contractor'].astype('string') 
tower['fee_component'] = [','.join(map(str, l)) for l in tower['fee_component']]
tower['fee_component'] = tower['fee_component'].astype('string') 
tower['last_update_by_uid'] = tower['last_update_by_uid'].astype('string') 
tower['promo'] = tower['promo'].astype('string') 
tower['rent_commission'] = tower['rent_commission'].astype('int64') 
tower['sell_commission'] = tower['sell_commission'].astype('int64') 
tower['year_completed_estimation'] = tower['year_completed_estimation'].astype('int64') 
tower['year_construction'] = tower['year_construction'].astype('int64')
tower['building_type'] = [','.join(map(str, l)) for l in tower['building_type']]
tower['building_type'] = tower['building_type'].astype('string') 
tower['service_charge'] = tower['service_charge'].astype('int64') 
tower['auto_description'] = tower['auto_description'].astype('bool') 
tower['is_leads_agent'] = tower['is_leads_agent'].astype('bool') 
tower['average_floor_plate'] = tower['average_floor_plate'].astype('int64') 
tower['ceiling_height'] = tower['ceiling_height'].astype('int64') 
tower['commercial_terms'] = tower['commercial_terms'].astype('int64') 
tower['condition'] = tower['condition'].astype('string') 
tower['electricity'] = tower['electricity'].astype('string') 
tower['fire_safety'] = tower['fire_safety'].astype('string') 
tower['grade'] = tower['grade'].astype('string') 
tower['land_size'] = tower['land_size'].astype('int64') 
tower['max_zone_per_floor'] = tower['max_zone_per_floor'].astype('int64') 
tower['office_hours'] = tower['office_hours'].astype('int64') 
tower['power_line'] = tower['power_line'].astype('int64') 
tower['selling_point'] = tower['selling_point'].astype('string') 
tower['semi_gross_area'] = tower['semi_gross_area'].astype('int64') 
tower['sinking_fund'] = tower['sinking_fund'].astype('int64') 
tower['complex'] = tower['complex'].astype('string') 
tower['create_at'] = tower['create_at'].astype('int64') 
tower['status'] = tower['status'].astype('int64') 
tower['include_scsf'] = tower['include_scsf'].astype('int64') 
tower['total_unit_primary'] = tower['total_unit_primary'].astype('int64') 

engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')
tower.to_sql('tower', engine, if_exists='replace', method=None)



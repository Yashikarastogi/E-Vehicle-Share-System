#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:05:17 2022

@author: shengyunXu
"""
from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.charts import HeatMap
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts.charts import Pie, Timeline
from pyecharts.globals import ThemeType
from pyecharts.charts import Sankey  #for sankey chart
import numpy as np
import pandas as pd
import manager


def limitedTimedVehicleNumber(dataframeO, dataframeV, start_time : str, end_time : str, vehicleTypeName: str) -> int:
 
    dataframeM = pd.merge(dataframeO, dataframeV, how='inner', left_on='vehicleId', right_on='vehicleID')
    #print(dataframeM)
    vehicledataframe = dataframeM[dataframeM['vehicleTypeName'] == vehicleTypeName]
    #print(vehicledataframe)
    targetData = [str(ind) for ind in vehicledataframe['orderTimestamp'] if start_time < str(ind) < end_time]
    
    return len(targetData)


def image1(dataframeO, dataframeV):
    ## image1
    # The Order statistics function
    x_data = ["Jan.","Feb.","Mar.","Apr.","May.",
              "Jun.","Jul.","Aug.","Sep.","Oct.",
              "Nov.","Dec."]

    list_bike = [limitedTimedVehicleNumber(dataframeO, dataframeV, "2022-"+str(i+1).zfill(2)+"-00 00:00:00", "2022-"+str(i+2).zfill(2)+"-00 00:00:00", "bike") for i in range(12)]
    list_scooter = [limitedTimedVehicleNumber(dataframeO, dataframeV, "2022-"+str(i+1).zfill(2)+"-00 00:00:00", "2022-"+str(i+2).zfill(2)+"-00 00:00:00", "scooter") for i in range(12)]
    monthly_bike_earn = [i * 2.5 for i in list_bike]
    monthly_scooter_earn = [i * 2.5 for i in list_scooter]
    list_total_earn = np.sum([monthly_bike_earn + monthly_scooter_earn], axis=0).tolist()
    bar = (        Bar()        
           .add_xaxis(x_data)        
           .add_yaxis( 
               "bike",  
               list_bike, # bike_list
               yaxis_index=0,            
               color="#d14a61",        )        
           .add_yaxis(            
               "scooter",            
               list_scooter,  #scooter_list          
               yaxis_index=1,            
               color="#5793f3",        )        
           .extend_axis(            
               yaxis=opts.AxisOpts(                
                   name="bike",                
                   type_="value",                
                   min_=0,                
                   max_=250,                
                   position="right",                
                   axisline_opts=opts.AxisLineOpts(                    
                       linestyle_opts=opts.LineStyleOpts(color="#d14a61")                ),                
                   axislabel_opts=opts.LabelOpts(formatter="{value} "),            )        )        
           .extend_axis(            
               yaxis=opts.AxisOpts(                
                   type_="value",                
                   name="   Revenue from orders for the month",                
                   min_=0,                 #the field of Revenue
                   max_=500,                
                   position="left",     
                   axisline_opts=opts.AxisLineOpts(                    
                       linestyle_opts=opts.LineStyleOpts(color="#675bba")                ),
                   axislabel_opts=opts.LabelOpts(formatter="{value}£ "),                
                   splitline_opts=opts.SplitLineOpts(                    
                       is_show=True, 
                       linestyle_opts=opts.LineStyleOpts(opacity=1)                ),            )        )
           .set_global_opts(            
               yaxis_opts=opts.AxisOpts(                
                   name="scooter",                
                   min_=0,                
                   max_=250,                
                   position="right",                
                   offset=40,                
                   axisline_opts=opts.AxisLineOpts(                    
                       linestyle_opts=opts.LineStyleOpts(color="#5793f3")                ), 
                   axislabel_opts=opts.LabelOpts(formatter="{value}  "),            ),
               title_opts=opts.TitleOpts(title="The Order statistics"),            
           tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),        )    )
    line = (        Line()
            .add_xaxis(x_data)        
            .add_yaxis(            " Revenue for this month",
                       list_total_earn,    #list_total_earn        
                       yaxis_index= 2,            
                       color="#675bba",            
                       label_opts=opts.LabelOpts(is_show=False),        )    )
    bar.overlap(line)
    return bar.render(path='image1.html')
     
def image2(dataframeO, dataframeV):
    ## image 2
    # The Number of Vehicles Used during the period
    temp = [["2022-10-"+str(i+24).zfill(2)+" "+str(j*3).zfill(2)+":00:00",
        "2022-10-"+str(i+24).zfill(2)+" "+str(j*3+3).zfill(2)+":00:00"]
        for i in range(7) for j in range(8)]

    Vehicle_Number =[limitedTimedVehicleNumber(dataframeO, dataframeV, str(i[0]), str(i[1]),"bike") for i in temp] 
    Vehicle_Number_ijlist = [[i, j,Vehicle_Number[i*j] ]for i in range(8) for j in range(7) ]

    x_label = ["12am","3am","6am","9am",
              "12pm","3pm","6pm","9pm","12pm"]
    y_label = ["Mon.","Tues","Wed.","Thur.","Fri.","Sat.","Sun."]
    # 示例数据   
    heat = (HeatMap()        
            .add_xaxis(x_label)        
            .add_yaxis("The Number of Vehicles Used during the period",                    
                       y_label,                    
                       Vehicle_Number_ijlist,           #Vehicle_Number,                   
                       label_opts=opts.LabelOpts(is_show=True, position="inside"))        
            .set_global_opts(            
                title_opts=opts.TitleOpts(title="Peak heat map of vehicle usage", subtitle="bike"),            
                visualmap_opts=opts.VisualMapOpts(max_=10, min_=0),            
                legend_opts=opts.LegendOpts(is_show=False))       )
    heat.render_notebook()
    return heat.render(path='image2.html') #.render_notebook()  

def image3(dataframeO, dataframeV, tablename):
    ## image3
    #move off the data of data of vehicle in using currently
    dataframeM = pd.merge(dataframeO, dataframeV, how='inner', left_on='vehicleId', right_on='vehicleID')
    dataframeM = dataframeM.dropna(subset=['returnCityLocationId'],inplace=False) 
    dataframeM['returnCityLocationId'] = dataframeM['returnCityLocationId'].astype(int)
    dataframeM = dataframeM.loc[:,['timeOrder','rentCityLocationId','returnCityLocationId','vehicleTypeName']]


    # get the structure of Sankey data
    import numpy as np
    vehicle_analysis_datalist = []
    for i in range(3):
        for j in range(3):
            vehicledata = dataframeM[(dataframeM['rentCityLocationId'] == i+1) & (dataframeM['returnCityLocationId']==j+1)]
            vehicledata['timeThreshold'] = vehicledata['timeOrder'] // 10
            temp_list = vehicledata['timeThreshold'].value_counts()
            temp_list = temp_list.tolist()
            temp_list.extend(0 for _ in range(4-len(temp_list))) #append(0*(t)))  #补全list 4位
            
            sum_temp_list = np.sum(temp_list)
            temp_list = [
                        {"source": "rentCityLocationName: block"+str(i+1), "target": "returnCityLocationName: block"+str(j+1), "value": index/sum_temp_list*100 }
                        for index in temp_list]
            vehicle_analysis_datalist +=temp_list
                            
    links = vehicle_analysis_datalist


    nodes = [
         {"name": "rentCityLocationName: block1"},
         {"name": "rentCityLocationName: block2"},
         {"name": "rentCityLocationName: block3"},
         {"name": "returnCityLocationName: block1"},
         {"name": "returnCityLocationName: block2"},
         {"name": "returnCityLocationName: block3"} ]
    
    sankey = (
        Sankey(init_opts=opts.InitOpts(width="2000px", height="800px"))
        .add(
            tablename,
            nodes,
            links,
            pos_top="10%",
            node_width = 30,  
            node_gap= 12,  #gap between two datas
            is_draggable = True,
            layout_iterations = 5,

            # focus_node_adjacency=True,
            itemstyle_opts=opts.ItemStyleOpts(border_width=2, border_color="#aaa"),
            linestyle_opt=opts.LineStyleOpts(opacity=0.8, curve=0.5, color='source'),
            label_opts=opts.LabelOpts(position='right'),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Distribution of return locations (in %)"))
    )
    return sankey.render("image3.html") 

def image4_test(dataframeO, dataframeV):
    ## image4
    # Vehicle usage by region function
    data = [len(dataframeO[dataframeO["rentCityLocationId"]==1]),
            len(dataframeO[dataframeO["rentCityLocationId"]==2]),
            len(dataframeO[dataframeO["rentCityLocationId"]==3])]
    #province = ['Scotland', 'England', 'Wales', 'Northern Ireland']
    province = ['London','Glasgow','Birmingham']
    key_value_list = [(province[i], data[i]) for i in range(len(province))]  
    geo = (Geo(init_opts=opts.InitOpts(
            bg_color='#42e5ff',))   
           .add_coordinate(
                name='London',
                longitude = -4.25763,
                latitude = 55.86515, 
)
           .add_coordinate(
                name='Glasgow',
                longitude =  -0.127647,
                latitude = 51.507322,
)
           .add_coordinate(
                name='Birmingham',
                longitude =  -1.898575,
                latitude = 52.489471, 
)
           .add_schema(maptype="英国")        ##
           .add("车辆数", key_value_list,            
                type_=ChartType.HEATMAP)
           
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))        
           .set_global_opts(           
               visualmap_opts=opts.VisualMapOpts(max_=350, min_=200),            
               legend_opts=opts.LegendOpts(is_show=False),            
               title_opts=opts.TitleOpts(title="Vehicle usage by region"))      
          )
    return geo.render(path='image4.html')

def image5(dataframeO, dataframeV):
    ## image5()
    # Proportion of vehicle status in each block (available, damaged)
    bike_list, scooter_list = [], []
    for i in range(3):
        avaiable_damaged_list = manager.Manager(0).vehicleAnalysis("scooter", i)
        scooter_list.append(avaiable_damaged_list)
    for i in range(3):
        avaiable_damaged_list = manager.Manager(0).vehicleAnalysis("bike",i)
        bike_list.append(avaiable_damaged_list)
    attr = ["Availble Vehicle", "Damaged Vehicle"]
    list1 = [ "block1", "block2", "block3"]
    #嵌套列表
    list2 = bike_list+scooter_list
    
    data = {'x': attr,
            '时长': dict(zip(list1, list2))   
            }
    def timeline_bar1() -> Timeline:
        x = data['x']
        tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        for i in list1:
            c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))     #主题风格
        .add("",   [list(z) for z in zip(attr,data['时长'][i])],radius=["25%", "75%"],rosetype="radius")
        .set_global_opts(title_opts=opts.TitleOpts(title="Proportion of vehicle status in each block (available, damaged)",pos_top="top",pos_left="left"),
                        legend_opts=opts.LegendOpts(pos_left="right", orient="vertical"))       # 设置标题   
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%')))    # 显示百分比
            tl.add(c, "{}".format(i))
        return tl

    return timeline_bar1().render(path='image5.html')


import folium
from folium.plugins import Draw
import cd_funcoes

m = folium.folium.Map(location=(-27.291316, -50.575125), tiles='OpenStreetMap', zoom_start=8, crs='EPSG3857')

fg_2 = folium.map.FeatureGroup(name='1-Unidades').add_to(m)
fg_4 = folium.map.FeatureGroup(name='2-Aglomerados subnormais', show=False).add_to(m)
fg_6 = folium.map.FeatureGroup(name='3-Escolas estaduais', show=False).add_to(m)

#1-Unidades
for i in range(0, len(cd_funcoes.df_2)):
    html_2 = cd_funcoes.popup_html_2(i)
    local_2 = [cd_funcoes.df_2['latitude'].iloc[i], cd_funcoes.df_2['longitude'].iloc[i]]
    popup_2 = folium.map.Popup(html_2)
    icon_2 = folium.plugins.BeautifyIcon(
        icon='building',
        icon_shape='marker',
        border_width=2,
        border_color='#566573',
        text_color='#000000',
        background_color='#CFEA13',
        spin=True)
    marcadores_2 = folium.map.Marker(location=local_2, popup=popup_2, icon=icon_2).add_to(m)
    fg_2.add_child(marcadores_2)

#2-Favelas
style_fc_4 = lambda x: {'color': '#5DADE2', 'weight': 2, 'fillcolor': '#5DADE2', 'fillOpacity': 0.4}
style_ttp_4 = "background-color: #5DADE2; color: #000000; border-radius: 10px; font-family: arial; font-size: 10px; padding: 8px;"
tooltip_fav_4 = folium.features.GeoJsonTooltip(fields=["NM_AGSN"], aliases=['Aglomerado subnormal de '], style=style_ttp_4)
st_catr_4 = folium.features.GeoJson(data=cd_funcoes.df_4, style_function=style_fc_4, name='Cidades', smooth_factor=0.1, tooltip=tooltip_fav_4)
fg_4.add_child(st_catr_4)

#3-Escolas
for i in range(0, len(cd_funcoes.df_6)):
    html_6 = cd_funcoes.popup_html_6(i)
    local_6 = [cd_funcoes.df_6['Latitude'].iloc[i], cd_funcoes.df_6['Longitude'].iloc[i]]
    popup_6 = folium.map.Popup(html_6)
    icon_6 = folium.plugins.BeautifyIcon(
        icon='graduation-cap',
        icon_shape='marker',
        border_width=2,
        border_color='#85929E',
        text_color='#000000',
        background_color='#B2BABB',
        spin=True)
    marcadores_6 = folium.map.Marker(location=local_6, popup=popup_6, icon=icon_6).add_to(m)
    fg_6.add_child(marcadores_6)

#4-Coroplético
idhm = folium.features.Choropleth(
    geo_data=cd_funcoes.df_5,
    data=cd_funcoes.df_5a, 
    columns=['Município', 'IDHM'],
    key_on='feature.properties.name', 
    fill_color='YlOrRd', 
    fill_opacity=0.6, 
    line_weight=0.5, 
    line_opacity=0.5,
    legend_name='Índice de desenvolvimento humano',
    name='4-IDHM',
    highlight=True).add_to(m)
                           
folium.plugins.Draw(export=True, position='topleft', draw_options=None, edit_options=None).add_to(m)
folium.plugins.Fullscreen(position='topright', title='tela cheia', title_cancel='sair da tela cheia').add_to(m)
folium.plugins.FloatImage('sap.jpg', bottom=5, left=78).add_to(m)                         
                                             
folium.map.LayerControl(position='bottomleft', collapsed=True, autoZIndex=True).add_to(m)

m.save('mapa.html')
import pandas
import geopandas

df_2 = pandas.read_json('dease_sc.json')
df_4 = geopandas.read_file('favelas_sc.geojson', driver='GeoJson')
df_5 = geopandas.read_file('borders_sc.geojson', driver='GeoJson')
df_5a = pandas.read_json('dados_sc.json')
df_6 = pandas.read_json('escolas.json')

def popup_html_2(row):
    i = row
    foto = df_2['picpath'].iloc[i]
    unidade = df_2['unidade'].iloc[i]
    regional = df_2['regional'].iloc[i]
    superintendente = df_2['superintendente'].iloc[i]
    coordenador = df_2['coordenador'].iloc[i]
    gestor = df_2['gestor'].iloc[i]
    email = df_2['email'].iloc[i]
    telefone = df_2['telefone'].iloc[i]
    rua = df_2['rua'].iloc[i]
    bairro = df_2['bairro'].iloc[i]
    cidade = df_2['cidade'].iloc[i]
    left_col_color = "#1E8449"
    right_col_color = "#78BF96"

    html_2 = """
    <!DOCTYPE html>
    <html>
       <center><table style = "height: 200px; width: 200px;">
            <center><img src=\"""" + str(foto) + """\" alt="logo_2" width=200 height=200 ></center>
            <tbody>
                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Unidade</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + unidade + """</td>
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Regional</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + regional + """</td>
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Superintendente</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + superintendente + """</td>
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Coordenador</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(coordenador) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Gestor</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(gestor) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Email</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(email) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Telefone</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(telefone) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Rua</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(rua) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Bairro</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(bairro) + """
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Cidade</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">{}</td>""".format(cidade) + """
                </tr>
            </tbody>
        </table></center>
    </html>
    """
    return html_2

def popup_html_6(row):
    i = row
    escola = df_6['Escola'].iloc[i]
    endereco = df_6['Endereço'].iloc[i]
    cidade = df_6['Cidade'].iloc[i]
    
    left_col_color = "#85929E"
    right_col_color = "#B2BABB"

    html_6 = """
    <!DOCTYPE html>
    <html>
       <center><table style = "height: 200px; width: 200px;">
            <tbody>
                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Escola</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + str(escola) + """</td>
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Endereço</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + str(endereco) + """</td>
                </tr>

                <tr>
                <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Cidade</span></td>
                <td style="width: 300px;background-color: """ + right_col_color + """;">""" + str(cidade) + """</td>
                </tr>
            </tbody>
        </table></center>
    </html>
    """
    return html_6
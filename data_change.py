import gspread
from google.oauth2.service_account import Credentials

# Autorizaciones
def apertura_sheet():
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    sheets = {
        "2021": {
            "key": "1GIwmH7gg0OgtK24grCzbzN_REroYNcNFfapEaKetNZw",
            "gid": 875568155
        },
        "2022": {
            "key": "1Os9JuRyWy2hQJNmv49pF_FtaRO2mVWUcWVTMbP4PuZo",
            "gid": 875568155
        },
        "2023": {
            "key": "1oXNjsSZMFR4Q4C_vo-Ho6TN1jsXrhUa_wsA-un5Mirk",
            "gid": 875568155
        },
        "2024": {
            "key": "10_IWrDUQZhExqI2wf4bK0M2B_BkhF6WeOXr2SyB2RBM",
            "gid": 875568155
        },
        "2025": {
            "key": "1AmBvNnBN8htAlwLT_6y3BPFuVH9tZsZHA2_H0CmC1p8",
            "gid": 1973933532
        },
    }
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    gc = gspread.authorize(creds)
    for anio, datos in sheets.items():
        print(f"Procesando {anio}...")
        sh = gc.open_by_key(datos["key"])
        hoja = sh.get_worksheet_by_id(datos["gid"])
        rango_nombres = hoja.get("E2:E")
        rango_asuntos = hoja.get("I2:I")

        modificar_nombres(hoja, rango_nombres)
        modificar_asuntos(hoja, rango_asuntos)
    
def modificar_nombres(hoja, rango):
    nuevos_valores = []
    
    for i in range(len(rango)):
        valor_celda = rango[i][0] if rango[i] else ""
        valor_celda = valor_celda.strip('"').strip("'")
        partes = valor_celda.split(" ", 1)
        nombre = partes[0]
        apellido = " ".join(partes[1:])
        apellido_iniciales = "".join(palabra[0] for palabra in apellido.split())
        nuevo_valor_celda = f"{nombre} {apellido_iniciales}"
        nuevos_valores.append([nuevo_valor_celda])
    
    hoja.update(nuevos_valores, "E2:E")

def modificar_asuntos(hoja, rango):
    nuevos_valores = []
    
    for i in range(len(rango)):
        nuevo_valor = f"Asunto n° {i+1}"
        nuevos_valores.append([nuevo_valor])
        
    hoja.update(nuevos_valores, "I2:I")

apertura_sheet()
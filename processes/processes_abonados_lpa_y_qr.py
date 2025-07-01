import pandas as pd
from current_month import n_month_int 
from gcp_paths import path_abonos_lpa_y_qr as ss
from gcp_utils import read, parkings_current_info


def main():

    events = []

    sheet_map = {'Pagos': 'LPA PARK', 'QR': 'QR'}

    for parking_name, [parking_id, _, _] in parkings_current_info.items():

        pairs = {}
        
        for sheet_name in ['Pagos', 'QR']:

            try: df = read(ss, 'excel_sheet', sheet_name)
            except: continue
            
            df['date'] = pd.to_datetime(df['date'], errors='coerce')

            df = df[df['date'].dt.month == n_month_int]

            mask = df['description'].str.contains(parking_name.upper(), na=False)
            df_parking = df[mask]

            operaciones = len(df_parking)
            if operaciones == 0: continue
            recaudacion = df_parking['amount'].sum()
            
            pairs[f'Operaciones {sheet_map.get(sheet_name)}'] = operaciones
            pairs[f'Recaudación {sheet_map.get(sheet_name)}'] = recaudacion

        if pairs: events.append([parking_id, pairs])

    return events

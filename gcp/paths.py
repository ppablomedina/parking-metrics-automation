from current_month import date, year


PROJECT_ID = 'bigdata-fase2'

# BigQuery
DATASET             = f'{PROJECT_ID}.parkings_datamart'
TABLE_EVENTS        = f'{DATASET}.events'
TABLE_PARKINGS      = f'{DATASET}.parkings'
TABLE_PARKINGS_STATES = f'{DATASET}.parkings_states'

# Cloud Storage
BUCKET_NAME        =  'sagulpa-datalake'
PATH_DATALAKE_DOCS =  'parkings-off_street/documents'
PATH_INBOX         = f'parkings-off_street/inbox/{date}'
PATH_OPEN_DATA     =  'parkings-off_street/open_data'


path_abonados_en_banco   = f'{PATH_DATALAKE_DOCS}/financiero.abonados-en-banco'             + f'.{date}.xlsx'
path_recaudacion         = f'{PATH_DATALAKE_DOCS}/financiero.gestion-directa-aparcamientos' + f'.{date}.xls'
path_rincon_estadisticas = f'{PATH_DATALAKE_DOCS}/{year}/aparcamientos.rincon-estadisticas' + f'.{date}.xlsx'
path_abonos_lpa_y_qr     = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.abonados-qr-lpa'          + f'/{date}.xlsx'
path_ocupacion           = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion'                + f'/{date}.csv'
path_ocupacion_ld        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-ld'             + f'/{date}.csv'
path_ocupacion_lv        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-lv'             + f'/{date}.csv'
path_ocupacion_sd        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-sd'             + f'/{date}.csv'
path_transparencia       = f'{PATH_OPEN_DATA}/transparency'                                 + f'/{date}.xlsx'


def get_path(doc_type, parking):
    """Obtiene el path del archivo correspondiente a un aparcamiento y tipo de documento."""
    parkings_alias = {
        'Elder':           'elder',
        'Mata':            'mata',
        'Metropol':        'metropol',
        'Nuevos Juzgados': 'nuevos-juzgados',
        'Rincón':          'rincon',
        'San Bernardo':    'san-bernardo',
        'Sanapú':          'sanapu',
        'Vegueta':         'vegueta'
    }


    parking_norm = parkings_alias.get(parking)

    path_map = {
        0: f'{PATH_DATALAKE_DOCS}/{year}/aparcamientos.informes-filtrados/{date}.{parking_norm}.pdf',
        1: f'{PATH_DATALAKE_DOCS}/{year}/sistemas.abonados/{date}.{parking_norm}.xlsx',
        2: f'{PATH_DATALAKE_DOCS}/{year}/sistemas.rotacion/{date}.{parking_norm}.xlsx',
    }

    return path_map.get(doc_type)

from gcp_paths import *
from gcp_utils import get_bucket, get_blobs, move_blob, parkings_current_info, delete_previous_version


def main():

    bucket = get_bucket()
    
    for blob in get_blobs(bucket):
        file_name = blob.name.split('/')[-1]
        source_path = blob.name

        if file_name.startswith('Abonados WPS'):
            delete_previous_version(bucket, path_abonados_en_banco)
            move_blob(bucket, source_path, path_abonados_en_banco)

        elif file_name.startswith('GESTION'):
            delete_previous_version(bucket, path_recaudacion)
            move_blob(bucket, source_path, path_recaudacion)

        elif file_name.upper().startswith('RINC') or file_name.upper().startswith('ESTADÍSTICAS - RINC'):
            delete_previous_version(bucket, path_rincon_estadisticas, yearly=True)
            move_blob(bucket, source_path, path_rincon_estadisticas)
    
        elif file_name.startswith('Ocupac'):                       move_blob(bucket, source_path, path_ocupacion)

        elif file_name.startswith('Estadísticas Ocupación Todos'): move_blob(bucket, source_path, path_ocupacion_ld)

        elif file_name.startswith('Estadísticas Ocupación L-V'):   move_blob(bucket, source_path, path_ocupacion_lv)

        elif file_name.startswith('Estadísticas Ocupación S-D'):   move_blob(bucket, source_path, path_ocupacion_sd)

        elif file_name.startswith('Abonos'):                       move_blob(bucket, source_path, path_abonos_lpa_y_qr)

        elif file_name.startswith('Informe filtrado'):             move_blob(bucket, source_path, get_path(0, get_parking(file_name)))

        elif file_name.startswith('Abonados'):                     move_blob(bucket, source_path, get_path(1, get_parking(file_name)))

        elif file_name.startswith('Rotación'):                     move_blob(bucket, source_path, get_path(2, get_parking(file_name)))

        else:                                                      raise ValueError(f"Archivo no reconocido: {file_name}")


def get_parking(file_name):
    mapping = {'SB': 'San Bernardo', 'JUZGADOS': 'Nuevos Juzgados'}
    parking_map = {delete_accents(p).upper(): p for p in parkings_current_info.keys()}
    file_name_normalizado = delete_accents(file_name).upper()

    for parking_norm, parking_original in parking_map.items():
        if parking_norm in file_name_normalizado:
            return parking_original

    for key, value in mapping.items():
        if key in file_name_normalizado:
            return value

    raise ValueError(f"Parking no encontrado en {file_name}")

def delete_accents(text):
    replacements = str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
    return text.translate(replacements)

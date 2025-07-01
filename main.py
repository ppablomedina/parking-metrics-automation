from processes import router, ocupacion, abonados_en_banco, abonados_lpa_y_qr, recaudacion, rincon_estadisticas, abonados_y_rotacion, informes_filtrados, ratios
from gcp.utils import insert_events

def entry_point(request):

    router.main()

    modules = [
        processes_ocupacion,
        processes_abonados_en_banco,
        processes_recaudacion,
        processes_rincon_estadisticas,
        processes_abonados_lpa_y_qr,
        processes_informes_filtrados,
        processes_abonados_y_rotacion
    ]

    all_events = []
    for module in modules:
        feeds = module.main()
        all_events.extend(feeds)

    insert_events(processes_ratios.main(all_events))

    return "ETL ejecutado correctamente\n", 200

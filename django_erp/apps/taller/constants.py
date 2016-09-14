from django.utils.translation import ugettext_lazy as _

# STATUS OF VEHICLE
CODE_STATUS_RENTED = 'TA1-1'
CODE_STATUS_MAINTENANCE = 'TA1-2'
CODE_STATUS_AVAILABLE = 'TA1-3'
SIS_STATUS_RENTED_STRING = (CODE_STATUS_RENTED, _('Alquilado'))
SIS_STATUS_MAINTENANCE_STRING = (CODE_STATUS_MAINTENANCE, _('Mantenimient Income'))
SIS_STATUS_AVAILABLE_STRING = (CODE_STATUS_AVAILABLE, _('Disponible'))

STATUS_VEHICLE_OPTIONS = (
    SIS_STATUS_RENTED_STRING, SIS_STATUS_MAINTENANCE_STRING, SIS_STATUS_AVAILABLE_STRING
)

# TYPE OF FUEL
CODE_TYPE_FUEL_OUTPUT = 'TA2-1'
CODE_TYPE_FUEL_INCOME = 'TA2-2'
SIS_TYPE_FUEL_OUTPUT_STRING = (CODE_TYPE_FUEL_OUTPUT, _('Fuel Output'))
SIS_TYPE_FUEL_INCOME_STRING = (CODE_TYPE_FUEL_INCOME, _('Fuel Income'))

TYPE_COMBUSTIBLE_OPTIONS = (
    SIS_TYPE_FUEL_OUTPUT_STRING, SIS_TYPE_FUEL_INCOME_STRING
)

# STATUS OF ORDER
CODE_STATUS_ORDER_CHECKLIST = 'TA3-1'
CODE_STATUS_ORDER_SOLICITUDE_MAINTENANCE = 'TA3-2'
CODE_STATUS_ORDER_DIAGNOSIS_REALIZED = 'TA3-3'

# STATUS OF ORDER DETAIL
CODE_STATUS_ORDER_PENDING = 'TA3-4'
CODE_STATUS_ORDER_IN_PROCESS = 'TA3-5'
CODE_STATUS_ORDER_FINISHED = 'TA3-6'

SIS_STATUS_ORDER_CHECKLIST_STRING = (CODE_STATUS_ORDER_CHECKLIST, 'Checklist')
SIS_STATUS_ORDER_SOLICITUDE_MAINTENANCE_STRING = (CODE_STATUS_ORDER_SOLICITUDE_MAINTENANCE, 'Solicitud de Mantenimiento')
SIS_STATUS_ORDER_DIAGNOSIS_REALIZED_STRING = (CODE_STATUS_ORDER_DIAGNOSIS_REALIZED, 'Diagnostico Realizado')
SIS_STATUS_ORDER_PENDING_STRING = (CODE_STATUS_ORDER_PENDING, 'Pendiente')
SIS_STATUS_ORDER_IN_PROCESS_STRING = (CODE_STATUS_ORDER_IN_PROCESS, 'En Proceso')
SIS_STATUS_ORDER_FINISHED_STRING = (CODE_STATUS_ORDER_FINISHED, 'Finalizado')

STATUS_ORDER_OPTIONS = [
    SIS_STATUS_ORDER_CHECKLIST_STRING, SIS_STATUS_ORDER_SOLICITUDE_MAINTENANCE_STRING,
    SIS_STATUS_ORDER_DIAGNOSIS_REALIZED_STRING,
]

STATUS_ORDER_DETAIL_OPTIONS = [
    SIS_STATUS_ORDER_PENDING_STRING, SIS_STATUS_ORDER_IN_PROCESS_STRING,
    SIS_STATUS_ORDER_FINISHED_STRING
]
STATUS_GLOBAL_OPTION = STATUS_ORDER_OPTIONS + STATUS_ORDER_DETAIL_OPTIONS

# TYPE OF ORDER
CODE_TYPE_MAINTENANCE = 'TA4-1'
CODE_TYPE_RENTAL = 'TA4-2'
CODE_TYPE_SUPERVISION = 'TA4-3'
SIS_TYPE_MAINTENANCE_STRING = (CODE_TYPE_MAINTENANCE, 'Alquiler')
SIS_TYPE_RENTAL_STRING = (CODE_TYPE_RENTAL, 'Mantenimiento')
SIS_TYPE_SUPERVISION_STRING = (CODE_TYPE_SUPERVISION, 'Supervision')

TYPE_ORDER_OPTIONS = (
    SIS_TYPE_MAINTENANCE_STRING, SIS_TYPE_RENTAL_STRING, SIS_TYPE_SUPERVISION_STRING
)

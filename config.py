import os

MIN_HEIGHT = 640
MIN_WIDTH = 960

ELEMENT_PADDING = 2
FRAME_PADDING = 6
FRAME_BORDER_WIDTH = 2
FRAME_RELIEF = 'groove'

CONFIG_FILE = 'config.json'
SUBROUTINE_FILE = 'subroutine.for'
PARAM_FILE = 'aba_param_dp.inc'

KEY_MODEL_NAME = u'name'
KEY_VARIABLE_NAME = u'name'
KEY_VARIABLES = u'variables'
KEY_IDENTIFIER = u'identifier'
KEY_UNIT = u'unit'
KEY_DESCRIPTION = u'description'
KEY_HOLDER = u'holder'


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = os.path.join(ROOT_DIR, 'models')
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
HOME_DIR = os.path.expanduser('~')

ABSOLUTE_ZERO = 0.0
STEFAN_BOLTZMANN = 5.670367e-8
MESH_DEVIATION_FACTOR = 0.05
MESH_MIN_SIZE_FACTOR = 0.1
NUM_INTERVALS = 100

TOOLTIP_DELAY = 500

ELASTIC_MODULUS = 'elastic_modulus'
POISSON_RATIO = 'poisson_ratio'
DENSITY = 'density'
THERM_CONDUCTIVITY = 'thermal_conductivity'
HEAT_CAPACITY = 'heat_capacity'
INELASTIC_HEAT = 'inelastic_heat_fraction'

SUBROUTINE_PATH = 'subroutine_path'
NAME = 'model_name'
BASIC_PROPERTIES = 'basic_properties'
MODEL_PROPERTIES = 'model_properties'

VERSION = '0.1'

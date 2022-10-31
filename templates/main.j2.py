from cobra.tools.gdal import GdalJob
from cobra.tools.gdal import GdalEngine
from cobra.helper.logging import Logger

l = Logger('Gdal - main')

l.info('Gdal, main')

ge = GdalEngine()
ge.listen()


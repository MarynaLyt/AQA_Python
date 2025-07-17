import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger('__name__')


def find_timing_exbytes_incoming(xml_file, group_number):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        group = root.find(f".//group[number='{group_number}']")
        if group is not None:
            incoming = group.find(".//timingExbytes/incoming")
            if incoming is not None:
                logger.info(f"Група #{group_number}: timingExbytes/incoming = {incoming.text}")
            else:
                logger.warning(f"Група #{group_number}: елемент 'incoming' відсутній")
        else:
            logger.warning(f"Група #{group_number}: не знайдена в XML")
    except Exception as e:
        logger.error(f"Помилка обробки XML: {e}")


find_timing_exbytes_incoming('work_with_xml/groups.xml', '5')

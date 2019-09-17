# -*- coding: utf-8 -*-
from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from datetime import datetime

processor = Processor('client_file.csv', delimiter=";")

res_partner_mapping = {
    'id': mapper.m2o('my_import_res_partner', mapper.concat('_', 'name', 'Birthdate', 'phone', 'email', 'website')),
    'name': mapper.val('id', postprocess=lambda x: "Partner %s" % x),
    'birthdate': mapper.val('Birthdate', postprocess=lambda x: datetime.strftime(x, "%d/%m/%y").strftime("%Y-%m-%d 00:00:))")),
    'phone': mapper.val('phone', postprocess=lambda x: "855%s" % (int(x) * 10)),
    'email': mapper.val('email', postprocess=lambda x: "Email %s" % x),
    'website': mapper.val('website', postprocess=lambda x: "website %s" % x)
}

processor.process(res_partner_mapping, 'res.partner.csv', {'model': 'res.partner', 'context': "{'tracking_disable': True}", 'worker': 2, 'batch_size': 20})
processor.write_to_file("res_partner.sh", python_exe='', path='')
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Certificate(models.Model):
    _name = 'print_certificate'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="Template")
    template = fields.Html(string="Certificate Content")


class Cert(models.Model):
    _inherit = 'hr.employee'

    tem = fields.Many2one('print_certificate', string="Certificate content")
    cer = fields.Html(related="tem.template", string="contact")

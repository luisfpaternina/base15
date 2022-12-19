# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    # person_type = fields.Selection(
    #    selection=[('legal', 'Persona Juridica y Asimilada'), ('natural', 'Persona Natural y Asimilada')], string='Tipo de Persona')

    # campo = fields.Char(string="Campito")

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProjectTask(models.Model):

    _inherit = 'project.task'

    name = fields.Char(
        required=False)
    other_exp = fields.Char(
        string='Titulo',
        readonly=True,
        compute="_onchange_concat_title")
    is_project = fields.Boolean(
        string="Autocomplete",
        compute="_depend_cond_name")
    is_create = fields.Boolean(
        string="Ruteado/FHC(no Shipper)")

    def _onchange_concat_title(self):
        for record in self:
            if record.other_exp == False:
                if record.x_studio_modalidad == 'Marítimo':
                    concat = "IDO:%s /SHIP:%s /CNEE:%s /POL:%s -POD:%s /OC/REF:%s" % (
                        record.x_studio_referencia_ido if record.x_studio_referencia_ido else "",
                        record.x_studio_nombre_6.name if record.x_studio_nombre_6.name else "",
                        record.x_studio_nombre_7.name if record.x_studio_nombre_7.name else "",
                        record.x_studio_field_Q3rFE.x_name if record.x_studio_field_Q3rFE.x_name else "",
                        record.x_studio_field_kpUmT.x_name if record.x_studio_field_kpUmT.x_name else "",
                        record.fields_OCREF if record.fields_OCREF else ""
                    )
                    record.other_exp = concat
                elif record.x_studio_modalidad == 'Aéreo':
                    concat = "IDO: %s/SHIP: %s/CNEE: %s/AOL:%s-AOD: %s/OC/REF: %s" % (
                        record.x_studio_referencia_ido if record.x_studio_referencia_ido else "",
                        record.x_studio_nombre_6.name if record.x_studio_nombre_6.name else "",
                        record.x_studio_nombre_7.name if record.x_studio_nombre_7.name else "",
                        record.x_studio_field_vXL0U.x_name if record.x_studio_field_vXL0U.x_name else "",
                        record.x_studio_field_kpCe2.x_name if record.x_studio_field_kpCe2.x_name else "",
                        record.fields_OCREF if record.fields_OCREF else ""
                    )
                    record.other_exp = concat
                elif record.x_studio_modalidad == 'Terrestre':
                    concat = "IDO:%s /SHIP:%s /CNEE:%s /COL:%s -COD:%s /OC/REF:%s" % (
                        record.x_studio_referencia_ido if record.x_studio_referencia_ido else "",
                        record.x_studio_nombre_6.name if record.x_studio_nombre_6.name else "",
                        record.x_studio_nombre_7.name if record.x_studio_nombre_7.name else "",
                        record.x_studio_field_MxS5e.x_name if record.x_studio_field_MxS5e.x_name else "",
                        record.x_studio_field_QQgxt.x_name if record.x_studio_field_QQgxt.x_name else "",
                        record.fields_OCREF if record.fields_OCREF else ""
                    )
                    record.other_exp = concat
                else:
                     concat = "IDO:%s /SHIP:%s /CNEE:%s /OC/REF:%s" % (
                        record.x_studio_referencia_ido if record.x_studio_referencia_ido else "",
                        record.x_studio_nombre_6.name if record.x_studio_nombre_6.name else "",
                        record.x_studio_nombre_7.name if record.x_studio_nombre_7.name else "",
                        record.fields_OCREF if record.fields_OCREF else ""
                    )
                record.other_exp = concat  
                     
            else:
                record.other_exp = record.name

    @api.depends('project_id')
    def _depend_cond_name(self):
        for record in self:
            record.is_project = True if record.project_id and record.project_id[
                0].name == 'IMPORTs' else False

   
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BomTotalValueField(models.Model):
    _inherit = 'mrp.bom'

    custom_val = fields.Char(string="Campo de Prueba", required=False, )
    valor_total = fields.Monetary(string="Valor Total", required=False)


class WorkorderTotalValueField(models.Model):
    _inherit = 'mrp.workorder'

    custom_val = fields.Char(string="Campo de Prueba", required=False, )
    valor_total = fields.Monetary(string="Valor Total", required=False)


class ProductionTotalValueField(models.Model):
    _inherit = 'mrp.production'

    custom_val = fields.Char(string="Campo de Prueba", required=False, )
    valor_total = fields.Monetary(string="Valor Total", required=False)
    valor_total_ex_ex = fields.Char(string="Valor TotalEx", compute='_compute_valor_total', store=True)

    @api.depends('product_id.price', 'product_uom_qty')
    def _compute_valor_total(self):
        for record in self:
            record.x_valor_total_ex_ex = record.product_id.price * record.product_uom_qty

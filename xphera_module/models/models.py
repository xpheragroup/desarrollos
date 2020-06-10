# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BomTotalValueField(models.Model):
    _name = 'mrp.bom'
    _inherit = 'mrp.bom'

    x_custom_val = fields.Char(string="Campo de Prueba", required=False, )
    x_valor_total = fields.Monetary(string="Valor Total", required=False)


class WorkorderTotalValueField(models.Model):
    _name = 'mrp.workorder'
    _inherit = 'mrp.workorder'

    x_custom_val = fields.Char(string="Campo de Prueba", required=False, )
    x_valor_total = fields.Monetary(string="Valor Total", required=False)


class ProductionTotalValueField(models.Model):
    _name = 'mrp.production'
    _inherit = 'mrp.production'

    x_custom_val = fields.Char(string="Campo de Prueba", required=False, )
    x_valor_total = fields.Monetary(string="Valor Total", required=False)
    x_valor_total_ex_ex = fields.Char(string="Valor TotalEx", compute='_compute_valor_total', store=True)

    @api.depends('product_id.price', 'product_uom_qty')
    def _compute_valor_total(self):
        for record in self:
            record['x_valor_total'] = record.product_id.price * record.product_uom_qty

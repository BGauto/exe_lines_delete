# -*- coding: utf-8 -*-

from odoo import models, fields, api


class exe_lines_delete(models.Model):
    _inherit = 'sale.order'

    def action_clear(self):
        for rec in self:
            rec.write({'order_line': [(5, 0, 0)]})
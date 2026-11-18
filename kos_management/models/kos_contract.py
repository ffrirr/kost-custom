from odoo import models, fields

class KosContract(models.Model):
    _name = 'kos.contract'
    _description = 'Kontrak Sewa Kos'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='No Kontrak', required=True, copy=False, default='Baru')
    partner_id = fields.Many2one('res.partner', string='Penyewa', required=True)
    room_id = fields.Many2one('kos.room', string='Kamar', required=True)
    start_date = fields.Date(string='Tanggal Mulai', default=fields.Date.today, required=True)
    end_date = fields.Date(string='Tanggal Selesai')
    monthly_rent = fields.Float(string='Biaya Sewa', related='room_id.price', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Aktif'),
        ('done', 'Selesai'),
        ('cancel', 'Dibatalkan')
    ], string='Status', default='draft', tracking=True)

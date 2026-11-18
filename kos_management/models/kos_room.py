from odoo import models, fields

class KosRoom(models.Model):
    _name = 'kos.room'
    _description = 'Kamar Kos'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nomor Kamar', required=True, tracking=True)
    floor = fields.Integer(string='Lantai', default=1)
    room_type = fields.Selection([
        ('std', 'Standard'),
        ('dlx', 'Deluxe'),
        ('vip', 'VIP')
    ], string='Tipe Kamar', default='std', required=True)
    price = fields.Float(string='Harga Sewa / Bulan', required=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Tersedia'),
        ('occupied', 'Terisi'),
        ('maintenance', 'Perbaikan')
    ], string='Status', default='draft', tracking=True)

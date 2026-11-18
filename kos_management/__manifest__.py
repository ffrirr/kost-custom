{
    'name': 'Smart Kost Management',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Manajemen Kamar dan Kontrak Sewa Kos-kosan',
    'author': 'Feri Irawan',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/kos_room_views.xml',
        'views/kos_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

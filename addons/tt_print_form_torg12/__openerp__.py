{
    'name' : 'Torg12 Print Form',
    'version' : '1.0',
    'category' : 'Extra Reports',
    'author'  : 'Transparent Technologies',
    'license' : 'AGPL-3',
    'depends' : ['base',
                 'jasper_reports',
                 'l10n_ru',
                 'account',
                 'tt_acc_invoice_line_subtotal_gross',
                 'tt_account_invoice_report_extensions',
                 'tt_print_forms_names',],
    'data' : [
        'torg_form_data.xml',
        'torg_form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'description': '''
This module adds Torg12 Print Form.
============================================================
    '''
}
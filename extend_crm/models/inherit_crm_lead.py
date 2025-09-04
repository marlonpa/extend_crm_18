from odoo import models, fields, api
import datetime
import logging

_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    category_list = (
        [
            ('residencial', 'Residencial'),
            ('empresarial', 'Empresarial'),
            ('gubernamental', 'Gubernamental')
        ]
    )

    x_lead_category = fields.Selection(
        category_list,
        string="Categoria",
        tracking=True,
        default="residencial"
    )

    x_delivery_deadline = fields.Datetime(
        string='Fecha límite lead',
        tracking=True
    )

    x_approved_date = fields.Datetime(
        string='Fecha de aprobación',
        tracking=True,
        null=True,
        blank=True
    )

    x_approved_by = fields.Many2one(
        'res.users',
        string='Aprobado por',
        domain="[ ('is_company', '=', False), ('active', '=', True)]",
        tracking=True,
        null =True,
        blank = True
    )

    x_duration_since_approved = fields.Integer(
        string="Duracion desde la aprobación(Horas)",
        compute="_compute_since_approved",
        store=True,
        readonly=True
    )

    x_installation_required = fields.Boolean(
        string="¿Intalación postventa?",
        tracking = True
    )

    x_installation_date = fields.Datetime(
        string='Fecha de instalación',
        tracking=True
    )

    x_contract_reference = fields.Char(
        string="Numero referencia  contrato",
        tracking=True,
    )

    x_support_required = fields.Boolean(
        string="¿Soporte postventa?",
        tracking=True,
    )

    @api.depends('x_approved_date')
    def _compute_since_approved(self):
        """
            1. Calcula tiempo transcurrido desde que se aprobó la orden
        """
        for record in self:
            if record.x_approved_date:
                now = fields.Datetime.now()
                _logger.info(f"ENTRE now {now}")
                range_time = now - record.x_approved_date
                _logger.info(f"ENTRE range_time {range_time}")
                record.x_duration_since_approved = range_time.total_seconds() / 3600.0
                _logger.info(f"ENTRE record.x_duration_since_approved {record.x_duration_since_approved}")
            else:
                record.x_duration_since_approved = 0


    @api.model
    def _cron_update_duration_since_approved(self):
        """
        Cron que recalcula las horas transcurridas para todos los leads con aprobación.
        """
        leads = self.search([("x_approved_date", "!=", False)])
        for lead in leads:
            lead._compute_since_approved()

    def action_approve_lead(self):
        for lead in self:
            lead.write({
                'x_approved_by': self.env.user.id,
                'x_approved_date': fields.Datetime.now(),
            })

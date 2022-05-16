from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index="True")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'the title of the course should not be the description'),

        ('name_unique',
         'UNIQUE(name)',
         'The course title must be unique'),
    ]
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Sessions'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade',
                                string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(string="Taken Seats", compute='_taken_seats')
    active = fields.Boolean(default=True)
    color = fields.Integer()
    end_date = fields.Date(string="END Date", store=True, compute='_get_end_date', inverse='_set_end_date')

    attendees_count = fields.Integer(string="Attendees Count", compute="_get_attendees_count", store=True)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")

    @api.constrains('seats', 'attendee_ids')
    def _check_valid_seats(self):
        if self.seats < 0:
            raise ValidationError("The number of available seats may not be negative")

        if self.seats < len(self.attendee_ids):
            raise ValidationError("Increase seats or remove excess attendees")

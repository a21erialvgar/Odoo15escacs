# -*- coding: utf-8 -*-

# from odoo import models, fields, api





from odoo import models, fields, api


class torneigs(models.Model):
    _name = 'escacs.torneigs'
    _description = 'Defineix les dades dels torneigs d escacs'

    nomTorneig = fields.Char('NomTorneig', required=True)
    ciutat = fields.Char(string='Ciutat')
    descripcio = fields.Text('Descripcio')
    dataIni = fields.Date('Data inici')
    dataFi = fields.Date('Data fi')

    # Relacio amb partides
    partides_ids = fields.Many2many('escacs.partides', string='Partides')


class partides(models.Model):
    _name = 'detectius.partides'
    _description = 'Defineix les dades de les partides dels torneigs'

    nomBlanques = fields.Char('NomBlanques', required=True)
    nomNegres = fields.Char('NomNegres', required=True)
    resultat = fields.Char('Resultat', required=True)
    nomTorneig = fields.Char('NomTorneig', required=True)
    numJugades = fields.Integer('NumJugades', required=True)
    notacio = fields.Char('notacioAlgebraica', required=True)
    # Relacions
    torneigs_ids = fields.One2many('escacs.torneigs', 'NomTorneig', string='Torneigs')

    # Relació amb jugadors
    jugadors_ids = fields.Many2many('escacs.jugadors', string='Jugadors')


class jugadors(models.Model):
    _name = 'escacs.jugadors'
    _description = 'Defineix les dades dels jugadors'

    nomJugador = fields.Char('NomJugador', required=True)
    dataNaixement = fields.Date('DataNaixement')
    eloFide = fields.Integer('EloFIDE', required=True)
    numPartides = fields.Integer('NumPartides')

    # Relació amb informe
    partides = fields.Many2one('escacs.partides', string='Partides')

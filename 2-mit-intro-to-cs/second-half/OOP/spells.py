#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:21:40 2023

@author: flarnrules
"""

class Spell (object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
    
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)
        
class Accio (Spell):
    def __init__(self):
        Spell.__init__(self,'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
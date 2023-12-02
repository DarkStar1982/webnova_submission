'''
Bojan Seirovski
bojan.seirovski@exodusorbitals.com
Exodus Orbitals
'''

class TimesOnTarget:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
    def __str__ (self):
        return f"TimesOnTarget[ start_time: {self.start_time} end_time: {self.end_time} )"

###############################################################################
# Copyright 2015-2020 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

import nacc.uds3

### BEGIN non-generated code
# WARNING: When generating new forms, do not overwrite this section
from datetime import date

# WARNING: When generating new forms, use CURRENT_YEAR instead of "2014"
# WARNING: When generating new forms, use CURRENT_YEAR-15 instead of "1999"
CURRENT_YEAR = date.today().year

### END non-generated code


def header_fields():
    fields = {}
    fields['FORMVER'] = nacc.uds3.Field(name='FORMVER', typename='Num', position=(906, 907), length=2, inclusive_range=(10, 10), allowable_values=[], blanks=[])
    fields['ADCID'] = nacc.uds3.Field(name='ADCID', typename='Num', position=(1, 2), length=2, inclusive_range=(2, 43), allowable_values=[], blanks=[])
    fields['PTID'] = nacc.uds3.Field(name='PTID', typename='Char', position=(4, 13), length=10, inclusive_range=None, allowable_values=[], blanks=[])
    return fields


class FormNP(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields = header_fields()
        self.fields['NPFORMMO'] = nacc.uds3.Field(name='NPFORMMO', typename='Num', position=(15, 16), length=2, inclusive_range=(1, 12), allowable_values=[], blanks=[])
        self.fields['NPFORMDY'] = nacc.uds3.Field(name='NPFORMDY', typename='Num', position=(18, 19), length=2, inclusive_range=(1, 31), allowable_values=[], blanks=[])
        self.fields['NPFORMYR'] = nacc.uds3.Field(name='NPFORMYR', typename='Num', position=(21, 24), length=4, inclusive_range=(2001, CURRENT_YEAR), allowable_values=[], blanks=[])
        self.fields['NPID'] = nacc.uds3.Field(name='NPID', typename='Char', position=(26, 35), length=10, inclusive_range=(), allowable_values=[], blanks=[])
        self.fields['NPSEX'] = nacc.uds3.Field(name='NPSEX', typename='Num', position=(37, 37), length=1, inclusive_range=(1, 2), allowable_values=[], blanks=[])
        self.fields['NPDAGE'] = nacc.uds3.Field(name='NPDAGE', typename='Num', position=(39, 41), length=3, inclusive_range=(0, 130), allowable_values=[], blanks=[])
        self.fields['NPDODMO'] = nacc.uds3.Field(name='NPDODMO', typename='Num', position=(43, 44), length=2, inclusive_range=(1, 12), allowable_values=[], blanks=[])
        self.fields['NPDODDY'] = nacc.uds3.Field(name='NPDODDY', typename='Num', position=(46, 47), length=2, inclusive_range=(1, 31), allowable_values=[], blanks=[])
        self.fields['NPDODYR'] = nacc.uds3.Field(name='NPDODYR', typename='Num', position=(49, 52), length=4, inclusive_range=(1984, CURRENT_YEAR), allowable_values=[], blanks=[])
        self.fields['NPPMIH'] = nacc.uds3.Field(name='NPPMIH', typename='Num', position=(54, 57), length=4, inclusive_range=(0, 98.9), allowable_values=['99.9'], blanks=[])
        self.fields['NPFIX'] = nacc.uds3.Field(name='NPFIX', typename='Num', position=(59, 59), length=1, inclusive_range=(1, 2), allowable_values=['7'], blanks=[])
        self.fields['NPFIXX'] = nacc.uds3.Field(name='NPFIXX', typename='Char', position=(61, 90), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 8 NPFIX ne 7 (Other)'])
        self.fields['NPWBRWT'] = nacc.uds3.Field(name='NPWBRWT', typename='Num', position=(92, 95), length=4, inclusive_range=(100, 2500), allowable_values=['9999'], blanks=[])
        self.fields['NPWBRF'] = nacc.uds3.Field(name='NPWBRF', typename='Num', position=(97, 97), length=1, inclusive_range=(1, 2), allowable_values=['8'], blanks=[])
        self.fields['NPGRCCA'] = nacc.uds3.Field(name='NPGRCCA', typename='Num', position=(99, 99), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPGRLA'] = nacc.uds3.Field(name='NPGRLA', typename='Num', position=(101, 101), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPGRHA'] = nacc.uds3.Field(name='NPGRHA', typename='Num', position=(103, 103), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPGRSNH'] = nacc.uds3.Field(name='NPGRSNH', typename='Num', position=(105, 105), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPGRLCH'] = nacc.uds3.Field(name='NPGRLCH', typename='Num', position=(107, 107), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPAVAS'] = nacc.uds3.Field(name='NPAVAS', typename='Num', position=(109, 109), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTAN'] = nacc.uds3.Field(name='NPTAN', typename='Num', position=(111, 111), length=1, inclusive_range=(1, 4), allowable_values=['7', '8'], blanks=[])
        self.fields['NPTANX'] = nacc.uds3.Field(name='NPTANX', typename='Char', position=(113, 142), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 10a NPTAN ne 7 (Other)'])
        self.fields['NPABAN'] = nacc.uds3.Field(name='NPABAN', typename='Num', position=(144, 144), length=1, inclusive_range=(1, 2), allowable_values=['7', '8'], blanks=[])
        self.fields['NPABANX'] = nacc.uds3.Field(name='NPABANX', typename='Char', position=(146, 175), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 10b NPABAN ne 7 (Other)'])
        self.fields['NPASAN'] = nacc.uds3.Field(name='NPASAN', typename='Num', position=(177, 177), length=1, inclusive_range=(1, 2), allowable_values=['7', '8'], blanks=[])
        self.fields['NPASANX'] = nacc.uds3.Field(name='NPASANX', typename='Char', position=(179, 208), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 10c NPASAN ne 7 (Other)'])
        self.fields['NPTDPAN'] = nacc.uds3.Field(name='NPTDPAN', typename='Num', position=(210, 210), length=1, inclusive_range=(1, 2), allowable_values=['7', '8'], blanks=[])
        self.fields['NPTDPANX'] = nacc.uds3.Field(name='NPTDPANX', typename='Char', position=(212, 241), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 10d NPTDPAN ne 7 (Other)'])
        self.fields['NPHISMB'] = nacc.uds3.Field(name='NPHISMB', typename='Num', position=(243, 243), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPHISG'] = nacc.uds3.Field(name='NPHISG', typename='Num', position=(245, 245), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPHISSS'] = nacc.uds3.Field(name='NPHISSS', typename='Num', position=(247, 247), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPHIST'] = nacc.uds3.Field(name='NPHIST', typename='Num', position=(249, 249), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPHISO'] = nacc.uds3.Field(name='NPHISO', typename='Num', position=(251, 251), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPHISOX'] = nacc.uds3.Field(name='NPHISOX', typename='Char', position=(253, 282), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 10e5 NPHISO ne 1 (Yes)'])
        self.fields['NPTHAL'] = nacc.uds3.Field(name='NPTHAL', typename='Num', position=(284, 284), length=1, inclusive_range=(0, 5), allowable_values=['8', '9'], blanks=[])
        self.fields['NPBRAAK'] = nacc.uds3.Field(name='NPBRAAK', typename='Num', position=(286, 286), length=1, inclusive_range=(0, 9), allowable_values=[], blanks=[])
        self.fields['NPNEUR'] = nacc.uds3.Field(name='NPNEUR', typename='Num', position=(288, 288), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPADNC'] = nacc.uds3.Field(name='NPADNC', typename='Num', position=(290, 290), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPDIFF'] = nacc.uds3.Field(name='NPDIFF', typename='Num', position=(292, 292), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPAMY'] = nacc.uds3.Field(name='NPAMY', typename='Num', position=(294, 294), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPINF'] = nacc.uds3.Field(name='NPINF', typename='Num', position=(296, 296), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 12a NPINF ne 0 then skip to Question 12b NPHEMO'])
        self.fields['NPINF1A'] = nacc.uds3.Field(name='NPINF1A', typename='Num', position=(298, 299), length=2, inclusive_range=(0, 87), allowable_values=['88', '99'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)'])
        self.fields['NPINF1B'] = nacc.uds3.Field(name='NPINF1B', typename='Num', position=(301, 304), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 121a NPINF1A = 0', 'Blank if Question 121a NPINF1A = 88', 'Blank if Question 121a NPINF1A = 99'])
        self.fields['NPINF1D'] = nacc.uds3.Field(name='NPINF1D', typename='Num', position=(306, 309), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 121a NPINF1A = 0', 'Blank if Question 121a NPINF1A = 1', 'Blank if Question 121a NPINF1A = 88', 'Blank if Question 121a NPINF1A = 99'])
        self.fields['NPINF1F'] = nacc.uds3.Field(name='NPINF1F', typename='Num', position=(311, 314), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 121a NPINF1A = 0', 'Blank if Question 121a NPINF1A = 1', 'Blank if Question 121a NPINF1A = 2', 'Blank if Question 121a NPINF1A = 88', 'Blank if Question 121a NPINF1A = 99'])
        self.fields['NPINF2A'] = nacc.uds3.Field(name='NPINF2A', typename='Num', position=(316, 317), length=2, inclusive_range=(0, 87), allowable_values=['88', '99'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)'])
        self.fields['NPINF2B'] = nacc.uds3.Field(name='NPINF2B', typename='Num', position=(319, 322), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 122a NPINF1A = 0', 'Blank if Question 122a NPINF1A = 88', 'Blank if Question 121a NPINF1A = 99'])
        self.fields['NPINF2D'] = nacc.uds3.Field(name='NPINF2D', typename='Num', position=(324, 327), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 122a NPINF1A = 0', 'Blank if Question 122a NPINF1A = 1', 'Blank if Question 122a NPINF1A = 88', 'Blank if Question 122a NPINF1A = 99'])
        self.fields['NPINF2F'] = nacc.uds3.Field(name='NPINF2F', typename='Num', position=(329, 332), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 122a NPINF1A = 0', 'Blank if Question 122a NPINF1A = 1', 'Blank if Question 122a NPINF1A = 2', 'Blank if Question 122a NPINF1A = 88', 'Blank if Question 122a NPINF1A = 99'])
        self.fields['NPINF3A'] = nacc.uds3.Field(name='NPINF3A', typename='Num', position=(334, 335), length=2, inclusive_range=(0, 87), allowable_values=['88', '99'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)'])
        self.fields['NPINF3B'] = nacc.uds3.Field(name='NPINF3B', typename='Num', position=(337, 340), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 123a NPINF1A = 0', 'Blank if Question 123a NPINF1A = 88', 'Blank if Question 123a NPINF1A = 99'])
        self.fields['NPINF3D'] = nacc.uds3.Field(name='NPINF3D', typename='Num', position=(342, 345), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 123a NPINF1A = 0', 'Blank if Question 123a NPINF1A = 1', 'Blank if Question 123a NPINF1A = 88', 'Blank if Question 123a NPINF1A = 99'])
        self.fields['NPINF3F'] = nacc.uds3.Field(name='NPINF3F', typename='Num', position=(347, 350), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 123a NPINF1A = 0', 'Blank if Question 123a NPINF1A = 1', 'Blank if Question 123a NPINF1A = 2', 'Blank if Question 123a NPINF1A = 88', 'Blank if Question 123a NPINF1A = 99'])
        self.fields['NPINF4A'] = nacc.uds3.Field(name='NPINF4A', typename='Num', position=(352, 353), length=2, inclusive_range=(0, 87), allowable_values=['88', '99'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)'])
        self.fields['NPINF4B'] = nacc.uds3.Field(name='NPINF4B', typename='Num', position=(355, 358), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 124a NPINF1A = 0', 'Blank if Question 124a NPINF1A = 88', 'Blank if Question 124a NPINF1A = 99'])
        self.fields['NPINF4D'] = nacc.uds3.Field(name='NPINF4D', typename='Num', position=(360, 363), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 124a NPINF1A = 0', 'Blank if Question 124a NPINF1A = 1', 'Blank if Question 124a NPINF1A = 88', 'Blank if Question 124a NPINF1A = 99'])
        self.fields['NPINF4F'] = nacc.uds3.Field(name='NPINF4F', typename='Num', position=(365, 368), length=4, inclusive_range=(0, 20), allowable_values=['88.8', '99.9'], blanks=['Blank if Question 12a NPINF ne 1 (Yes)', 'Blank if Question 124a NPINF1A = 0', 'Blank if Question 124a NPINF1A = 1', 'Blank if Question 124a NPINF1A = 2', 'Blank if Question 124a NPINF1A = 88', 'Blank if Question 124a NPINF1A = 99'])
        self.fields['NPHEMO'] = nacc.uds3.Field(name='NPHEMO', typename='Num', position=(370, 370), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 12b NPHEMO ne 1 then skip to Question 12c NPOLD'])
        self.fields['NPHEMO1'] = nacc.uds3.Field(name='NPHEMO1', typename='Num', position=(372, 372), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank if Question 12b NPINF ne 1 (Yes)'])
        self.fields['NPHEMO2'] = nacc.uds3.Field(name='NPHEMO2', typename='Num', position=(374, 374), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank if Question 12b NPINF ne 1 (Yes)'])
        self.fields['NPHEMO3'] = nacc.uds3.Field(name='NPHEMO3', typename='Num', position=(376, 376), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank if Question 12b NPINF ne 1 (Yes)'])
        self.fields['NPOLD'] = nacc.uds3.Field(name='NPOLD', typename='Num', position=(378, 378), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 12c NPOLD ne 1 then skip to Question 12d NPOLDD'])
        self.fields['NPOLD1'] = nacc.uds3.Field(name='NPOLD1', typename='Num', position=(380, 380), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12c NPOLD ne 1 (Yes)'])
        self.fields['NPOLD2'] = nacc.uds3.Field(name='NPOLD2', typename='Num', position=(382, 382), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12c NPOLD ne 1 (Yes)'])
        self.fields['NPOLD3'] = nacc.uds3.Field(name='NPOLD3', typename='Num', position=(384, 384), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12c NPOLD ne 1 (Yes)'])
        self.fields['NPOLD4'] = nacc.uds3.Field(name='NPOLD4', typename='Num', position=(386, 386), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12c NPOLD ne 1 (Yes)'])
        self.fields['NPOLDD'] = nacc.uds3.Field(name='NPOLDD', typename='Num', position=(388, 388), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 12d NPOLDD ne 1 then skip to Question 12e NPARTER'])
        self.fields['NPOLDD1'] = nacc.uds3.Field(name='NPOLDD1', typename='Num', position=(390, 390), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12d NPOLDD ne 1 (Yes)'])
        self.fields['NPOLDD2'] = nacc.uds3.Field(name='NPOLDD2', typename='Num', position=(392, 392), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12d NPOLDD ne 1 (Yes)'])
        self.fields['NPOLDD3'] = nacc.uds3.Field(name='NPOLDD3', typename='Num', position=(394, 394), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12d NPOLDD ne 1 (Yes)'])
        self.fields['NPOLDD4'] = nacc.uds3.Field(name='NPOLDD4', typename='Num', position=(396, 396), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 12d NPOLDD ne 1 (Yes)'])
        self.fields['NPARTER'] = nacc.uds3.Field(name='NPARTER', typename='Num', position=(398, 398), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPWMR'] = nacc.uds3.Field(name='NPWMR', typename='Num', position=(400, 400), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPATH'] = nacc.uds3.Field(name='NPPATH', typename='Num', position=(402, 402), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 12g NPPATH ne 1 then skip to Question 13 NPLBOD'])
        self.fields['NPNEC'] = nacc.uds3.Field(name='NPNEC', typename='Num', position=(404, 404), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH2'] = nacc.uds3.Field(name='NPPATH2', typename='Num', position=(406, 406), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH3'] = nacc.uds3.Field(name='NPPATH3', typename='Num', position=(408, 408), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH4'] = nacc.uds3.Field(name='NPPATH4', typename='Num', position=(410, 410), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH5'] = nacc.uds3.Field(name='NPPATH5', typename='Num', position=(412, 412), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH6'] = nacc.uds3.Field(name='NPPATH6', typename='Num', position=(414, 414), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH7'] = nacc.uds3.Field(name='NPPATH7', typename='Num', position=(416, 416), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH8'] = nacc.uds3.Field(name='NPPATH8', typename='Num', position=(418, 418), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH9'] = nacc.uds3.Field(name='NPPATH9', typename='Num', position=(420, 420), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH10'] = nacc.uds3.Field(name='NPPATH10', typename='Num', position=(422, 422), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATH11'] = nacc.uds3.Field(name='NPPATH11', typename='Num', position=(424, 424), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATHO'] = nacc.uds3.Field(name='NPPATHO', typename='Num', position=(426, 426), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)'])
        self.fields['NPPATHOX'] = nacc.uds3.Field(name='NPPATHOX', typename='Char', position=(428, 457), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank If Question 12g NPPATH ne 1 (Yes)', 'Blank If Question 1212 NPPATHO ne 1 (Yes)'])
        self.fields['NPLBOD'] = nacc.uds3.Field(name='NPLBOD', typename='Num', position=(459, 459), length=1, inclusive_range=(0, 5), allowable_values=['8', '9'], blanks=[])
        self.fields['NPNLOSS'] = nacc.uds3.Field(name='NPNLOSS', typename='Num', position=(461, 461), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPHIPSCL'] = nacc.uds3.Field(name='NPHIPSCL', typename='Num', position=(463, 463), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTDPA'] = nacc.uds3.Field(name='NPTDPA', typename='Num', position=(465, 465), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTDPB'] = nacc.uds3.Field(name='NPTDPB', typename='Num', position=(467, 467), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTDPC'] = nacc.uds3.Field(name='NPTDPC', typename='Num', position=(469, 469), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTDPD'] = nacc.uds3.Field(name='NPTDPD', typename='Num', position=(471, 471), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPTDPE'] = nacc.uds3.Field(name='NPTDPE', typename='Num', position=(473, 473), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPFTDTAU'] = nacc.uds3.Field(name='NPFTDTAU', typename='Num', position=(475, 475), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 17a NPFTDTAU ne 1 then skip to Question 17c NPFTDTDP'])
        self.fields['NPPICK'] = nacc.uds3.Field(name='NPPICK', typename='Num', position=(477, 477), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT2'] = nacc.uds3.Field(name='NPFTDT2', typename='Num', position=(479, 479), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPCORT'] = nacc.uds3.Field(name='NPCORT', typename='Num', position=(481, 481), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPPROG'] = nacc.uds3.Field(name='NPPROG', typename='Num', position=(483, 483), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT5'] = nacc.uds3.Field(name='NPFTDT5', typename='Num', position=(485, 485), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT6'] = nacc.uds3.Field(name='NPFTDT6', typename='Num', position=(487, 487), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT7'] = nacc.uds3.Field(name='NPFTDT7', typename='Num', position=(489, 489), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT8'] = nacc.uds3.Field(name='NPFTDT8', typename='Num', position=(491, 491), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT9'] = nacc.uds3.Field(name='NPFTDT9', typename='Num', position=(493, 493), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDT10'] = nacc.uds3.Field(name='NPFTDT10', typename='Num', position=(495, 495), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17a NPFTDTAU ne 1 (Yes)'])
        self.fields['NPFTDTDP'] = nacc.uds3.Field(name='NPFTDTDP', typename='Num', position=(497, 497), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPALSMND'] = nacc.uds3.Field(name='NPALSMND', typename='Num', position=(499, 499), length=1, inclusive_range=(0, 5), allowable_values=['8', '9'], blanks=[])
        self.fields['NPOFTD'] = nacc.uds3.Field(name='NPOFTD', typename='Num', position=(501, 501), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['If Question 17e FPOFTD ne 1 then skip to Question 18a NPPDXA'])
        self.fields['NPOFTD1'] = nacc.uds3.Field(name='NPOFTD1', typename='Num', position=(503, 503), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17e NPOFTD ne 1 (Yes)'])
        self.fields['NPOFTD2'] = nacc.uds3.Field(name='NPOFTD2', typename='Num', position=(505, 505), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17e NPOFTD ne 1 (Yes)'])
        self.fields['NPOFTD3'] = nacc.uds3.Field(name='NPOFTD3', typename='Num', position=(507, 507), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17e NPOFTD ne 1 (Yes)'])
        self.fields['NPOFTD4'] = nacc.uds3.Field(name='NPOFTD4', typename='Num', position=(509, 509), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17e NPOFTD ne 1 (Yes)'])
        self.fields['NPOFTD5'] = nacc.uds3.Field(name='NPOFTD5', typename='Num', position=(511, 511), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=['Blank If Question 17e NPOFTD ne 1 (Yes)'])
        self.fields['NPPDXA'] = nacc.uds3.Field(name='NPPDXA', typename='Num', position=(513, 513), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXB'] = nacc.uds3.Field(name='NPPDXB', typename='Num', position=(515, 515), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXC'] = nacc.uds3.Field(name='NPPDXC', typename='Num', position=(517, 517), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXD'] = nacc.uds3.Field(name='NPPDXD', typename='Num', position=(519, 519), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXE'] = nacc.uds3.Field(name='NPPDXE', typename='Num', position=(521, 521), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXF'] = nacc.uds3.Field(name='NPPDXF', typename='Num', position=(523, 523), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXG'] = nacc.uds3.Field(name='NPPDXG', typename='Num', position=(525, 525), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXH'] = nacc.uds3.Field(name='NPPDXH', typename='Num', position=(527, 527), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXI'] = nacc.uds3.Field(name='NPPDXI', typename='Num', position=(529, 529), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXJ'] = nacc.uds3.Field(name='NPPDXJ', typename='Num', position=(531, 531), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXK'] = nacc.uds3.Field(name='NPPDXK', typename='Num', position=(533, 533), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXL'] = nacc.uds3.Field(name='NPPDXL', typename='Num', position=(535, 535), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXM'] = nacc.uds3.Field(name='NPPDXM', typename='Num', position=(537, 537), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXN'] = nacc.uds3.Field(name='NPPDXN', typename='Num', position=(539, 539), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXO'] = nacc.uds3.Field(name='NPPDXO', typename='Num', position=(541, 541), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXP'] = nacc.uds3.Field(name='NPPDXP', typename='Num', position=(543, 543), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXQ'] = nacc.uds3.Field(name='NPPDXQ', typename='Num', position=(545, 545), length=1, inclusive_range=(0, 1), allowable_values=['8', '9'], blanks=[])
        self.fields['NPPDXR'] = nacc.uds3.Field(name='NPPDXR', typename='Num', position=(547, 547), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPPDXRX'] = nacc.uds3.Field(name='NPPDXRX', typename='Char', position=(549, 578), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank If Question 18r NPPDXR = 0 (No)'])
        self.fields['NPPDXS'] = nacc.uds3.Field(name='NPPDXS', typename='Num', position=(580, 580), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPPDXSX'] = nacc.uds3.Field(name='NPPDXSX', typename='Char', position=(582, 611), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank If Question 18s NPPDXS = 0 (No)'])
        self.fields['NPPDXT'] = nacc.uds3.Field(name='NPPDXT', typename='Num', position=(613, 613), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=[])
        self.fields['NPPDXTX'] = nacc.uds3.Field(name='NPPDXTX', typename='Char', position=(615, 644), length=30, inclusive_range=(), allowable_values=[], blanks=['Blank If Question 18t NPPDXT = 0 (No)'])
        self.fields['NPBNKA'] = nacc.uds3.Field(name='NPBNKA', typename='Num', position=(646, 646), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKB'] = nacc.uds3.Field(name='NPBNKB', typename='Num', position=(648, 648), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKC'] = nacc.uds3.Field(name='NPBNKC', typename='Num', position=(650, 650), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKD'] = nacc.uds3.Field(name='NPBNKD', typename='Num', position=(652, 652), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKE'] = nacc.uds3.Field(name='NPBNKE', typename='Num', position=(654, 654), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKF'] = nacc.uds3.Field(name='NPBNKF', typename='Num', position=(656, 656), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPBNKG'] = nacc.uds3.Field(name='NPBNKG', typename='Num', position=(658, 658), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPFAUT'] = nacc.uds3.Field(name='NPFAUT', typename='Num', position=(660, 660), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=[])
        self.fields['NPFAUT1'] = nacc.uds3.Field(name='NPFAUT1', typename='Char', position=(662, 721), length=60, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 19h NPFAUT ne 1 (Yes)'])
        self.fields['NPFAUT2'] = nacc.uds3.Field(name='NPFAUT2', typename='Char', position=(723, 782), length=60, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 19h NPFAUT ne 1 (Yes)'])
        self.fields['NPFAUT3'] = nacc.uds3.Field(name='NPFAUT3', typename='Char', position=(784, 843), length=60, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 19h NPFAUT ne 1 (Yes)'])
        self.fields['NPFAUT4'] = nacc.uds3.Field(name='NPFAUT4', typename='Char', position=(845, 904), length=60, inclusive_range=(), allowable_values=[], blanks=['Blank if Question 19h NPFAUT ne 1 (Yes)'])
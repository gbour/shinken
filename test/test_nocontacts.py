#!/usr/bin/env python2.6
#Copyright (C) 2009-2010 :
#    Gabes Jean, naparuba@gmail.com
#    Gerhard Lausser, Gerhard.Lausser@consol.de
#
#This file is part of Shinken.
#
#Shinken is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Shinken is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

#
# This file is used to test reading and processing of config files
#

#It's ugly I know....
from shinken_test import *


class TestNoContact(ShinkenTest):
    #Uncomment this is you want to use a specific configuration
    #for your test
    def setUp(self):
        self.setup_with_file('etc/nagios_nocontacts.cfg')

    
    # Seems that Nagios allow non contacts elements, just warning
    # and not error. Should do the same.
    def test_nocontact(self):
        host = self.sched.hosts.find_by_name("test_host_0")
        self.assert_(host.contacts == [])
        svc = self.sched.services.find_srv_by_name_and_hostname("test_host_0", "test_ok_0")
        self.assert_(svc.contacts == [])
        self.assert_(self.sched.conf.is_correct)


if __name__ == '__main__':
    unittest.main()


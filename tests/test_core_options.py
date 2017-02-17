# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

from __future__ import absolute_import
import unittest2 as unittest
from src.core.options import Options
from src.core.options.exceptions import OptionsError

class TestOptions(unittest.TestCase):
    """TestOptions class"""

    def test_get_arg_values_exception(self):
        """ Arguments.get_arg_values() exception test """

        with self.assertRaises(OptionsError) as context:
            Options().get_arg_values()
        self.assertTrue(OptionsError == context.expected)
        
if __name__ == "__main__":
    unittest.main()

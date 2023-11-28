# -*- coding: utf-8 -*-
from pattern_library.monkey_utils import override_tag

from cib_navigation.templatetags.navigation_tags import register

override_tag(register, name="primarynav")
override_tag(register, name="footernav")

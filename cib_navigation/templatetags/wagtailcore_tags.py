# -*- coding: utf-8 -*-
from pattern_library.monkey_utils import override_tag

from wagtail.templatetags.wagtailcore_tags import register

override_tag(register, name="include_block")
override_tag(register, name="pageurl")
override_tag(register, name="slugurl")

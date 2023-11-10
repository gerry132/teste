from wagtail import blocks


class BaseBlockLinkContext(blocks.StructBlock):
    """
    Base block to get link context.
    """
    def get_context(self, value, parent_context=None):
        """
        Get context helper
        """
        context = super().get_context(value, parent_context=parent_context)
        try:
            # A block may not have a page or url field
            if value["url"]:
                context["link_url"] = value["url"]
            elif value["page"]:
                context["link_url"] = value["page"].url

        except KeyError:
            context["link_url"] = None

        try:
            if value["title"]:
                context["link_title"] = value["title"]
            else:
                if value["page"]:
                    context["link_title"] = value["page"].title
                elif value["url"]:
                    context["link_title"] = value["title"]

        except KeyError:
            context["link_title"] = None

        return context

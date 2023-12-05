from wagtail.core import blocks


class VideoBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=False, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["embed"]
        self.max_length = 360

    class Meta:  # noqa
        template = "patterns/blocks/video.html"
        icon = "edit"
        label = "Video"

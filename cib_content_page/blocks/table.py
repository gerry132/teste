from wagtailtinymce.blocks import TinyMCEBlock

from wagtail_localize.segments import StringSegmentValue

from bs4 import BeautifulSoup

__all__ = [
    "TinyMCETableBlock",
]


class TinyMCETableBlock(TinyMCEBlock): # noqa
    custom_mce_config = {
        "plugins": "table link",
        "menubar": "",
        "toolbar": "bold italic link unlink | table tablecaption tablecolheader tablerowheader | tablecellprops tablemergecells tablesplitcells | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol",
        "table_appearance_options": False,
        "table_default_attributes": {},
        "table_default_styles": {"border-collapse": "collapse", "width": "100%"},
        "table_sizing_mode": "relative",
        "table_advtab": False,
        "table_cell_advtab": False,
        "table_row_advtab": False,
        "language": "en",
    }

    class Meta:
        label = "Table"
        icon = "table"

    allowed_tags = [
        "table",
        "thead",
        "tbody",
        "br",
        "colgroup",
        "col",
        "caption",
        "tr",
        "th",
        "td",
        "p",
        "strong",
        "b",
        "em",
        "i",
        "a",
    ]

    allowed_attributes = {
        "table": ["class", "id", "style"],
        "col": ["span", "class"],
        "th": [
            "align",
            "valign",
            "class",
            "scope",
            "abbr",
            "colspan",
            "rowspan",
            "headers",
        ],
        "td": ["align", "valign", "class", "colspan", "rowspan", "headers"],
        "a": ["class", "href", "target", "title"],
    }

    allowed_styles = ["width", "border-collapse"]

    def get_translatable_segments(self, data, **kwargs):
        duplicate_elements = []
        segments = []
        soup = BeautifulSoup(data, features="lxml")
        tables = soup.find_all('table')
        col = 0
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                for elem in cols:
                    if elem.text.strip() not in duplicate_elements and not elem.find("table"):
                        segments.append(StringSegmentValue("", elem.text.strip(), order=col))
                        duplicate_elements.append(elem.text.strip())
                    col += 1

        return segments

    def sort_segment(self, segments) -> list:
        seg_dict = {}
        first_list = []
        for s in segments:
            seg_dict[s.order] = s
            first_list.append(s.order)
        first_list.sort()
        return [seg_dict[elem] for elem in first_list]

    def restore_translated_segments(self, block_value, segments):
        duplicate_elements = {}
        soup = BeautifulSoup(block_value, "html.parser")
        tables = soup.find_all('table')
        cell = 0
        sorted_segment = self.sort_segment(segments)

        if tables:
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    for ele in cols:
                        if ele.text.strip() != "" and not ele.find("table"):
                            try:
                                if not ele.text.strip() in duplicate_elements and \
                                 not ele.text.strip() in duplicate_elements.values():
                                    duplicate_elements[ele.text.strip()] = sorted_segment[cell].string.data
                                    ele.string.replace_with(sorted_segment[cell].string.data)
                                    cell += 1
                                elif not ele.text.strip() in duplicate_elements.values():
                                    ele.string.replace_with(duplicate_elements[ele.text.strip()])
                            except Exception as e:
                                print(e)

            return str(soup)

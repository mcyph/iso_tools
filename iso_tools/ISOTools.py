from iso_tools.isotools_classes.defines import NONE, LANG, SCRIPT, TERRITORY, VARIANT
from iso_tools.isotools_classes.ISOGuesser import ISOGuesser
from iso_tools.isotools_classes.ISOToolsBase import ISOToolsBase
from iso_tools.isotools_classes.LikelySubtags import LikelySubtags
from iso_tools.isotools_classes.SupplementalData import SupplementalData
from iso_tools.isotools_classes.LangGroups import LangGroups


class ISOTools(ISOToolsBase, LangGroups):
    def __init__(self):
        ISOToolsBase.__init__(self)
        LikelySubtags.__init__(self)
        SupplementalData.__init__(self)
        ISOGuesser.__init__(self)


ISOTools = ISOTools()

if __name__ == '__main__':
    # TODO: Add a test for various functions!
    print((ISOTools.verify_iso('en')))

    # Remove specific properties
    print((ISOTools.get_L_removed('en_Latn', [SCRIPT])))
    print((ISOTools.removed('ja_Jpan', LANG | SCRIPT)))

    # Miscellaneous
    print((ISOTools.get_lang_props('en')))
    print((ISOTools.guess_omitted_info('en')))

    # Locale->ISO
    print((ISOTools.locale_to_iso('en-US')))
    print((ISOTools.locale_to_iso('en-GB')))

    # Remove implied/unecessary information (or recover it)
    print((ISOTools.pack_iso('ja_Jpan')))
    print((ISOTools.remove_unneeded_info('ja_Jpan')))
    print((ISOTools.unpack_iso('ja')))

    # Split/join ISO code information
    print((ISOTools.join(part3='en', script='Latn')))
    print((ISOTools.split('ja')))
    print((ISOTools.split_into_from_to('ja_-_en')))

    # Fileame escape/de-escape
    print((ISOTools.filename_escape('en')))
    print((ISOTools.filename_split('en')))

    # URL escape/de-escape
    print((ISOTools.url_join('ja', 'en')))
    print((ISOTools.url_split('ja_-_en')))
    print((ISOTools.url_escape('ja_Jpan')))
    print((ISOTools.url_unescape('ja_Jpan')))

    #from iso_tools.iso_codes import ISOCodes
    #ISOCodes.

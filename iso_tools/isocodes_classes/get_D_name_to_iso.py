


def get_D_name_to_iso():
    from iso_tools.ISOCodes import ISOCodes
    D = {}

    for part3 in ISOCodes:
        DISO = ISOCodes.get_D_iso(part3, add_alternates=True)

        if 'part1' in DISO:
            part3 = DISO['part1'] # HACK: shorten the code!!!


        D[DISO['short_name'].lower()] = part3
        D[DISO['long_name'].lower()] = part3

        DAlt = DISO['DAlt']
        if 'language name' in DAlt:
            DLangNames = DAlt['language name']
            for k, v in list(DLangNames.items()):
                D[k.lower()] = part3

                if 'alternate language name' in v:
                    DAltNames = v['alternate language name']
                    for k2 in DAltNames:
                        D[k2.lower()] = part3

    for k in list(D.keys()):
        # HACK: Always use the generic "zh"
        # Chinese code for Mandarin Chinese!
        if D[k] == 'cmn':
            D[k] = 'zh'

        # HACK: Fix e.g. "chinese, hakka" -> "hakka"
        if ', ' in k:
            _, _, lang = k.partition(', ')
            if not lang in D:
                D[lang] = D[k]

    D['cantonese'] ='yue'
    D['mandarin'] = 'zh' # HACK!
    D['translingual'] = 'mul'

    # Codes from Wiktionary headers with more than
    # ~400 entries that aren't in the above data
    DExc = {
        'middle english': 'enm',  # 21579,
        'ancient greek': 'grc',  # 19189,
        #'norman': 'nrf',  # 10941,
        'old english': 'ang',  # 8847,
        'old french': 'fro',  # 7636,
        'old armenian': 'xcl',  # 6945,
        'khmer': 'khm',  # 4121,
        'middle french': 'frm',  # 4049,
        'interlingua': 'ina',  # 3212,
        'livonian': 'liv',  # 2995,
        'old irish': 'sga',  # 2920,
        'west frisian': 'fry',  # 2865,
        # 'westrobothnian': 2735,
        'egyptian': 'egy',  # 2622,
        'old church slavonic': 'chu',  # 2419,
        'middle dutch': 'dum',  # 1958,
        'aramaic': 'arc',  # 1755,
        'alemannic german': 'gsw',  # 1585,
        'swazi': 'ssw',  # 1408,
        'vilamovian': 'wym',  # 1385,
        'old high german': 'goh',  # 1334,
        'tocharian b': 'txb',  # 1258,
        'punjabi': 'pan',  # 1240,
        'ottoman turkish': 'ota',  # 1106,
        'saterland frisian': 'stq',  # 1085,

        'german low german': 'nds',  # 945,
        'haitian creole': 'hat',  # 913,
        'chichewa': 'nya',  # 881,
        'mauritian creole': 'mfe',  # 852,
        'dupaningan agta': 'duo',  # 702,
        'zazaki': 'zza',  # 688,
        # 'old swedish': 640,
        'bikol central': 'bcl',  # 607,
        # 'tarantino': 593,
        'old occitan': 'pro',  # 580,
        # 'old portuguese': 573,
        'north frisian': 'frr',  # 567,
        # 'bourguignon': 539,
        'taos': 'twf',  # 523,
        'romani': 'rom',  # 494,
        # 'central franconian': 486,
        'okinawan': 'ryu',  # 429,
        'ojibwe': 'oji',  # 403,
    }

    for lang_name, part3 in DExc.items():
        DISO = ISOCodes.get_D_iso(part3, add_alternates=True)

        if 'part1' in DISO:
            # Shorten the code
            DExc[lang_name] = DISO['part1']

    D.update(DExc)
    return D


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_D_name_to_iso())


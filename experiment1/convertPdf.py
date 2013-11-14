import convert
convert.convert_pdf('Starbucks.pdf', outtype = 'txt')

def convert_pdf(path, outtype='txt', opts=[]):
    import sys
    from layout.pdfparser import PDFDocument, PDFParser
    from layout.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
    from layout.pdfdevice import PDFDevice, TagExtractor
    from layout.converter import XMLConverter, HTMLConverter, TextConverter
    from layout.cmapdb import CMapDB
    from layout.layout import LAParams
    import getopt

    outfile = path[:-3] + outtype
    outdir = '/'.join(path.split('/')[:-1])

    # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    # ?outfile = None
    # ?outtype = None
    # outdir = None
    #layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    showpageno = True
    laparams = LAParams()
    for (k, v) in opts:
        if k == '-d': debug += 1
        elif k == '-p': pagenos.update( int(x)-1 for x in v.split(',') )
        elif k == '-m': maxpages = int(v)
        elif k == '-P': password = v
        elif k == '-o': outfile = v
        elif k == '-n': laparams = None
        elif k == '-A': laparams.all_texts = True
        elif k == '-V': laparams.detect_vertical = True
        elif k == '-M': laparams.char_margin = float(v)
        elif k == '-L': laparams.line_margin = float(v)
        elif k == '-W': laparams.word_margin = float(v)
        elif k == '-F': laparams.boxes_flow = float(v)
        elif k == '-Y': layoutmode = v
        elif k == '-O': outdir = v
        elif k == '-t': outtype = v
        elif k == '-c': codec = v
        elif k == '-s': scale = float(v)
    #
    #PDFDocument.debug = debug
    #PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
    #
    rsrcmgr = PDFResourceManager()

    outtype = 'text'

    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)


    fp = file(path, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password,
                    check_extractable=True)
    fp.close()
    device.close()
    outfp.close()
    return
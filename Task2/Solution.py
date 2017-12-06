import requests
import sys
from lxml import html
from lxml import cssselect

# Constants
ERROR_CLASS_NAME = "errormsg"

class CVEDetails(object):
    def __init__(self):
        pass

def get_command_line_arguments():
    return sys.argv[1:]


def build_URL_by_CVE_id(cveId):
    return ("https://www.cvedetails.com/cve/" + cveId)


def get_page_from_url(url):
    return requests.get(url)


def check_for_error(tree):
    error_divs = tree.find_class(ERROR_CLASS_NAME)
    if (len(error_divs) != 0):
        print ("Error:" + error_divs[0].text_content())
        return False
    return True

def parse_CVEDetails(tree):
    # TODO create a CVEDetails object here, now it's just parsed fields

    CVSS_Score = tree.cssselect('#cvssscorestable > tbody > tr:nth-child(1) > td > div')
    # CVSS_Score = tree.xpath('//*[@id="cvssscorestable"]/tbody/tr[1]/td/div/text()')
    Confidentiality_Impact = tree.xpath('//*[@id="cvssscorestable"]/tbody/tr[2]/td/span[1]/text()')
    Integrity_Impact = tree.xpath("//*[@id=\"cvssscorestable\"]/tbody/tr[3]/td/span[1]/text()")
    Availability_Impact = tree.xpath("//*[@id=\"cvssscorestable\"]/tbody/tr[4]/td/span[1]")
    # Access_Complexity = tree.xpath("")
    # Authentication = tree.xpath("")
    # Gained_Access = tree.xpath("")
    ##list
    # Vulnerability_type = tree.xpath("")
    # CWE_ID = tree.xpath("")
    # Products_affected = tree.xpath("")
    # Vendor = tree.xpath()


    print ("CVSS_Score :{}".format(CVSS_Score))
    print ("Confidentiality_Impact :{}".format(Confidentiality_Impact))


if __name__ == "__main__":
    cve_id_list = get_command_line_arguments()

    if (len(cve_id_list) == 0):
        print ("Error.No argumnets passed. Pass at least one CVE id in script parameters")

    for cveId in cve_id_list:
        url = build_URL_by_CVE_id(cveId)
        page = get_page_from_url(url)
        # convert to html tree
        tree = html.fromstring(page.content)
        if(check_for_error(tree)):
            parse_CVEDetails(tree)



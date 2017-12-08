import requests
import sys
from lxml import html
from lxml import cssselect
import CveDetails

# Constants
ERROR_CLASS_NAME = "errormsg"

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
    cv_details_dictionary = {}
    cv_details_dictionary["CVSS_Score"] = tree.xpath('//*[@id="cvssscorestable"]/tr[1]/td/div/text()')
    cv_details_dictionary["Confidentiality_Impact"] = tree.xpath('//*[@id="cvssscorestable"]/tr[2]/td/span[1]/text()')
    cv_details_dictionary["Integrity_Impact"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[3]/td/span[1]/text()")
    cv_details_dictionary["Availability_Impact"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[4]/td/span[1]")
    cv_details_dictionary["Access_Complexity"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[5]/td/span[1]")
    cv_details_dictionary["Authentication"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[6]/td/span[1]")
    cv_details_dictionary["Gained_Access"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[7]/td/span")
    cv_details_dictionary["Vulnerability_type"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[8]/td/span[1]")
    cv_details_dictionary["CWE_ID"] = tree.xpath('//*[@id="cvssscorestable"]/tr[9]/td')
    cv_details_dictionary["Products_affected"] = tree.xpath("//*[@id=\"vulnprodstable\"]")
    # it's a table
    cv_details_dictionary["Vendor"] = tree.xpath('//*[@id="addvendsuppdata"]/tr[2]/td[1]/a')
    cveDetails = CVEDetails(cv_details_dictionary)

    return cveDetails


if __name__ == "__main__":
    cve_id_list = get_command_line_arguments()

    if (len(cve_id_list) == 0):
        print ("Error.No argumnets passed. Pass at least one CVE id in script parameters")

    for cveId in cve_id_list:
        url = build_URL_by_CVE_id(cveId)
        page = get_page_from_url(url)
        # convert to html tree
        tree = html.fromstring(page.content)
        if (check_for_error(tree)):
            print (parse_CVEDetails(tree))